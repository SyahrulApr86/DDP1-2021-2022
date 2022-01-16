# recommended python version: >= 3.8

import tkinter as tk
import tkinter.messagebox


GUARDIAN_BAR_HEIGHT = 100
BAR_HEIGHT = 80
BAR_WIDTH = 3

# ean akan menggambarkan sebanyak 12 digit kode, masing-masing diwakili oleh 7 normal bars
NORMAL_BAR_WIDTH = BAR_WIDTH * 7 * 12
# guardian bar samping terdiri atas 3 bars. guardian bar tengah terdiri atas 5 bars
GUARDIAN_BAR_WIDTH = BAR_WIDTH * (3 + 5 + 3)

BARCODE_WIDTH = NORMAL_BAR_WIDTH + GUARDIAN_BAR_WIDTH

BARCODE_HEIGHT = GUARDIAN_BAR_HEIGHT
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 400

# posisi (x,y) untuk top-left corner sang barcode
BARCODE_X_POS = (CANVAS_WIDTH - BARCODE_WIDTH) // 2
BARCODE_Y_POS = (CANVAS_HEIGHT - BARCODE_HEIGHT) // 2


def main():
    window = tk.Tk()
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#ffffff")

    label_1 = tk.Label(text="Save Barcode to PS file [eg: EAN13.eps]:", font=('Helvetica', 17, 'bold'))
    input_1_field = tk.Entry(window, font=('Helvetica', 14))
    label_1.pack()
    input_1_field.pack()

    label_2 = tk.Label(text="Enter code (first 12 decimal digits):", font=('Helvetica', 17, 'bold'))
    input_2_field = tk.Entry(window, font=('Helvetica', 14))
    label_2.pack()
    input_2_field.pack()

    def input_handle(event):
        nama_file = input_1_field.get()
        yang_mau_diencode = input_2_field.get()
        print(repr(yang_mau_diencode))

        if len(set(nama_file) & set('\\/:*?"<>|')):
            tk.messagebox.showerror(title="Invalid file name",
                                    message="nama file tidak boleh mengandung karakter terlarang")
            return
        if nama_file[-4:].lower() != ".eps" and nama_file[-3:].lower() != ".ps":
            tk.messagebox.showerror(title="Invalid file name", message="File extension harus .eps atau .ps")
            return
        if len(set(yang_mau_diencode) - set("0123456789")):
            tk.messagebox.showerror(title="Invalid ean code",
                                    message="Ean code hanya boleh berisi digit-digit antara 0 sampai 9")
            return
        if len(yang_mau_diencode) != 12:
            tk.messagebox.showerror(title="Invalid ean code",
                                    message="Ean code harus berisi sebanyak 12 digit")
            return
        draw_barcode(canvas, yang_mau_diencode)
        canvas.postscript(file=nama_file)

    input_1_field.bind("<Return>", input_handle)
    input_2_field.bind("<Return>", input_handle)

    canvas.pack(pady=10)
    window.mainloop()


FONT = ('Calibri', '24',  'bold')
FIRST_TEXT_OFFSET = 50  # offset relatif terhadap barcode
SECOND_TEXT_OFFSET = 50
FIRST_TEXT_Y_POS = BARCODE_Y_POS - FIRST_TEXT_OFFSET
SECOND_TEXT_Y_POS = BARCODE_Y_POS + GUARDIAN_BAR_HEIGHT + SECOND_TEXT_OFFSET


def draw_barcode(canvas, digits: str):
    canvas.delete('all')

    check_digit = BarcodeDrawer.get_check_sum(digits)
    canvas.create_text(CANVAS_WIDTH//2, FIRST_TEXT_Y_POS, font=FONT, fill="#6baeff", anchor="s",
                       text="EAN-13 Barcode:")
    canvas.create_text(CANVAS_WIDTH//2, SECOND_TEXT_Y_POS, font=FONT, fill="#6baeff", anchor="n",
                       text=f"Check Digit: {check_digit}")

    barcode_drawer = BarcodeDrawerWithDigit(canvas,
                                            BARCODE_X_POS,
                                            BARCODE_Y_POS,
                                            BAR_WIDTH,
                                            BAR_HEIGHT,
                                            guardian_bar_height=GUARDIAN_BAR_HEIGHT)
    barcode_drawer.draw_barcode_from_digits(digits)
    canvas.update()


# term yang digunakan:
#   guardian bar: bar yang panjang. Biasanya ada di tengah atau di pinggir
#   normal bar:   bar yang relatif lebih pendek. Bar yang merepresentasikan kode dari barcode tersebut
class BarcodeDrawer:
    EAN_L_CODES = {
        0: 0b_0001101,
        1: 0b_0011001,
        2: 0b_0010011,
        3: 0b_0111101,
        4: 0b_0100011,
        5: 0b_0110001,
        6: 0b_0101111,
        7: 0b_0111011,
        8: 0b_0110111,
        9: 0b_0001011,
    }
    EAN_R_CODES = {
        0: 0b_1110010,
        1: 0b_1100110,
        2: 0b_1101100,
        3: 0b_1000010,
        4: 0b_1011100,
        5: 0b_1001110,
        6: 0b_1010000,
        7: 0b_1000100,
        8: 0b_1001000,
        9: 0b_1110100,
    }
    EAN_G_CODES = {
        0: 0b_0100111,
        1: 0b_0110011,
        2: 0b_0011011,
        3: 0b_0100001,
        4: 0b_0011101,
        5: 0b_0111001,
        6: 0b_0000101,
        7: 0b_0010001,
        8: 0b_0001001,
        9: 0b_0010111,
    }

    # kombinasi encoding dari barcode sisi kiri yang bergantung pada first digit dari kode
    EAN_FIRST_DIGIT_COMBINATION = {
        # 1 = EAN_G_CODES. 0 = EAN_L_CODES
        0: [0, 0, 0, 0, 0, 0],
        1: [0, 0, 1, 0, 1, 1],
        2: [0, 0, 1, 1, 0, 1],
        3: [0, 0, 1, 1, 1, 0],
        4: [0, 1, 0, 0, 1, 1],
        5: [0, 1, 1, 0, 0, 1],
        6: [0, 1, 1, 1, 0, 0],
        7: [0, 1, 0, 1, 0, 1],
        8: [0, 1, 0, 1, 1, 0],
        9: [0, 1, 1, 0, 1, 0],
    }

    def __init__(self, canvas: tk.Canvas,
                 barcode_x_pos,
                 barcode_y_pos,
                 bar_width=3,
                 bar_height=80,
                 bar_color="#000000",
                 guardian_bar_height=100,
                 guardian_bar_color="#0000FF"):
        self.canvas = canvas
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.bar_color = bar_color
        self.guardian_bar_height = guardian_bar_height
        self.guardian_bar_color = guardian_bar_color
        self.x_pointer = 0  # ibarat cursor (offset) dari self.x_pos

        # posisi top-left corner barcode dalam (x,y) relatif terhadap top-left corner canvas
        self.BARCODE_X_POS = barcode_x_pos
        self.BARCODE_Y_POS = barcode_y_pos

    def draw_barcode_from_digits(self, digits: str):
        assert digits.isnumeric()
        assert len(digits) == 12

        digits += str(BarcodeDrawer.get_check_sum(digits))

        first_digit = int(digits[0])
        first_digit_combinations: list = BarcodeDrawer.EAN_FIRST_DIGIT_COMBINATION[first_digit]

        first_six_digit = digits[1:7]  # kelompok digit pertama
        second_six_digit = digits[7:]  # kelompok digit kedua
        self._draw_guardian_bar_side()

        # gambar 6 digit pertama
        for i in range(len(first_six_digit)):
            digit = int(first_six_digit[i])
            current_combination = BarcodeDrawer.EAN_L_CODES
            if first_digit_combinations[i]:
                current_combination = BarcodeDrawer.EAN_G_CODES
            print(digit, ":", end="")
            self._draw_normal_bar(digit, current_combination)

        self._draw_guardian_bar_mid()

        # gambar 6 digit terakhir
        for i in range(len(second_six_digit)):
            digit = int(second_six_digit[i])
            current_combination = BarcodeDrawer.EAN_R_CODES
            print(digit, ":", end="")
            self._draw_normal_bar(digit, current_combination)
        self._draw_guardian_bar_side()

    def _draw_guardian_bar_mid(self, shift_ptr=True):
        self._draw_bars(0b_01010, self.guardian_bar_height, self.guardian_bar_color,
                        number_of_bars=5)
        if shift_ptr:
            self._shift_pointer(5)

    def _draw_guardian_bar_side(self, shift_ptr=True):
        self._draw_bars(0b_101, self.guardian_bar_height, self.guardian_bar_color, number_of_bars=3)
        if shift_ptr:
            self._shift_pointer(3)

    def _draw_normal_bar(self, digit, current_combination, shift_ptr=True):
        self._draw_normal_bar_helper(digit, current_combination)
        if shift_ptr:
            self._shift_pointer()

    def _draw_normal_bar_helper(self, digit: int, eancode: dict):
        assert 0 <= digit <= 9
        assert eancode in (BarcodeDrawer.EAN_L_CODES, BarcodeDrawer.EAN_G_CODES, BarcodeDrawer.EAN_R_CODES)
        digit_code = eancode[digit]
        self._draw_bars(digit_code, self.bar_height, self.bar_color)

    def _draw_bars(self, code: int, bar_height, fill, number_of_bars=7):
        """Menggambar bar sebanyak `number_of_bars` berdasarkan digit kode biner yang diberikan"""

        # Mengubah code (integer) menjadi tuple_code, yakni tuple of integers yang bernilai satu atau nol.
        # Misal jika code=5, number_of_bars=7, maka tuple_code = (0, 0, 0, 0, 1, 0, 1)
        temp = f"{code:0b}".zfill(number_of_bars)
        tuple_code: tuple[int] = tuple(map(int, temp))
        print(temp)

        temp_x_pointer: int = self.BARCODE_X_POS + self.x_pointer
        for digit in tuple_code:
            # x0 y0: koordinat pojok kiri atas dari create_rectangle()
            # x1 y1: koordinat pojok kanan bawha dari create_rectangle()
            x0 = temp_x_pointer
            y0 = self.BARCODE_Y_POS
            x1 = x0 + self.bar_width
            y1 = y0 + bar_height

            if digit:
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="", width=0, fill=fill)
            temp_x_pointer += self.bar_width

    def _shift_pointer(self, number_of_bar: int = 7):
        """Menggeser x_pointer ke kanan sejauh `number_of_bar`"""
        self.x_pointer += self.bar_width * number_of_bar

    def _shift_left_pointer(self, number_of_bar: int = 7):
        """Menggeser x_pointer ke kiri sejauh `number_of_bar`"""
        self.x_pointer -= self.bar_width * number_of_bar

    @staticmethod
    def get_check_sum(digits: str) -> int:
        assert len(digits) == 12
        digit_genap = digits[0::2]
        digit_ganjil = digits[1::2]
        sum_digit_genap = sum(map(int, digit_genap))
        sum_digit_ganjil = sum(map(int, digit_ganjil))
        x = sum_digit_genap*1 + sum_digit_ganjil*3
        x %= 10

        return 0 if x == 0 else 10-x


class BarcodeDrawerWithDigit(BarcodeDrawer):
    def __init__(self, canvas: tk.Canvas,
                 barcode_x_pos,
                 barcode_y_pos,
                 bar_width=3,
                 bar_height=80,
                 bar_color="#000000",
                 guardian_bar_height=100,
                 guardian_bar_color="#0000FF",
                 digit_font_family=('Helvetica', '12'),
                 digit_color="#32a4a8",
                 digit_y_offset=4):
        super().__init__(canvas, barcode_x_pos, barcode_y_pos, bar_width, bar_height,
                         bar_color, guardian_bar_height, guardian_bar_color)
        self.digit_color = digit_color
        self.digit_offset = digit_y_offset
        self.digit_font = digit_font_family
        self.digit_color = digit_color
        self.digit_y_offset = digit_y_offset

    def draw_barcode_from_digits(self, digits: str):  # override
        # gambar angka yang pertama dulu di sebelah kiri guardian bar paling kiri
        self._shift_left_pointer()  # ke kiri selangkah
        self._draw_number(int(digits[0]),
                          self.digit_font, self.digit_color)
        self._shift_pointer()  # balik lagi ke kanan

        super().draw_barcode_from_digits(digits)  # sisanya, lakukan seperti biasanya

    def _draw_normal_bar(self, digit, current_combination, shift_ptr=True):  # override
        self._draw_normal_bar_helper(digit, current_combination)
        self._draw_number(digit, self.digit_font, self.digit_color)

        if shift_ptr:
            self._shift_pointer()

    def _draw_number(self, digit: int,
                     font=('Helvetica', '16'),
                     fill="#000000",
                     digit_x_pos=None, digit_y_pos=None):
        assert 0 <= digit <= 9
        if digit_x_pos is None:
            LEBAR_BARS_UNTUK_TIAP_DIGIT = self.bar_width * 7  # tiap digit kode diwakilkan oleh 7 normal bars
            digit_x_pos = self.BARCODE_X_POS + self.x_pointer + LEBAR_BARS_UNTUK_TIAP_DIGIT / 2
        if digit_y_pos is None:
            digit_y_pos = self.BARCODE_Y_POS + self.bar_height + self.digit_offset
        self.canvas.create_text(digit_x_pos, digit_y_pos, text=str(digit), font=font, fill=fill, anchor='n')


if __name__ == "__main__":
    main()
