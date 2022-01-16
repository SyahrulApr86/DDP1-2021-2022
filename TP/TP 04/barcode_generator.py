# import module
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter.font import Font

# create class BardcodeGenerator
class BardcodeGenerator:
    
    # constructor
    def __init__(self, master):
        self.master = master
        master.title("EAN-13 [by Syahrul A.]")
        master.geometry("550x680")
        self.create_widgets()

    
    def create_widgets(self):
        """Place widget in GUI"""
        label_main_font = Font(family= "Helvetica", size = 20, weight = "bold")
        entry_font_file = Font(family= "Helvetica", size = 20)
        entry_font_code = Font(family= "Helvetica", size = 17)
        self.label_save = tk.Label(self.master, text="Save barcode to PS file [eg: EAN13.eps]:", font = label_main_font)
        self.label_code = tk.Label(self.master, text="Enter code (first 12 decimal digits):", font = label_main_font)
        
        self.file = tk.StringVar()
        self.code = tk.StringVar()
        self.ent_file = tk.Entry(self.master, textvariable = self.file, width=17, font = entry_font_file)
        self.ent_code = tk.Entry(self.master, textvariable = self.code, width=17, font = entry_font_code)
        
        self.canvas = tk.Canvas(self.master, width=415, height=500, bg="white")

        self.label_save.pack()
        self.ent_file.pack()
        self.label_code.pack()
        self.ent_code.pack()
        self.canvas.pack(expand=True)
        self.master.bind('<Return>', self.validator)

    
    def validator(self, event):
        """Function for validate input from user"""

        # forbidden filename
        if self.file.get()[:-3] in ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 
                                    'COM0', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9', 'LPT0']:
            tkmsg.showerror("Contain Forbidden filename", 'Your filename is forbidden.')

        elif self.file.get()[:-4] in ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 
                                    'COM0', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9', 'LPT0']:
            tkmsg.showerror("Contain Forbidden filename", 'Your filename is forbidden.')

        # invalid file extension 
        elif self.file.get()[-3:] == ".ps" or self.file.get()[-4:] == ".eps":
            for i in self.file.get():
                if i in ['/', '\\', '?', '%', '*', ':', '|', '\"', "\'", '<', '>', '    ', ]:                   # illegal character
                    tkmsg.showerror("Contain Illegal Character", "Your input contains illegal character.")
                    break
            else:
                if (not self.code.get().isdecimal()) or (len(self.code.get()) != 12):                           # invalid code
                    tkmsg.showerror(title = "Wrong Input!", message="Please enter correct input code.")
                else:
                    self.create_barcode()

        else:
            tkmsg.showerror(title = "Invalid Extension", message="Please enter a valid filename extension.")
    
    
    def create_barcode(self):
        """Create barcode in canvas"""

        self.canvas.delete("all")
        canvas = self.canvas
        raw_code = self.code.get()
        
        x = (int(raw_code[0])*1 + int(raw_code[1])*3 + int(raw_code[2])*1 + int(raw_code[3])*3  +               # calculte checkdigit
            int(raw_code[4])*1 + int(raw_code[5])*3 + int(raw_code[6])*1 + int(raw_code[7])*3 + 
            int(raw_code[8])*1 + int(raw_code[9])*3 + int(raw_code[10])*1 + int(raw_code[11])*3) % 10

        checkdigit=""
        if x != 0:
            checkdigit = str(10-x)
        else:
            checkdigit = str(x)

        code = raw_code + checkdigit
        bit1 = ""                           # will be filled with bitstring digits 2 to 7
        bit2 = ""                           # will be filled with bitstring digits 8 to 13

        lst_pattern = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]        # pattern list determine by first digit
        l_encode = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
        r_encode = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
        g_encode = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]

        pattern = lst_pattern[int(code[0])]

        # convert to bitstring
        for i in range(6):                              # digit 2-7
            if pattern[i] == "L":
                bit1 += l_encode[int(code[1+i])]
            if pattern[i] == "G":
                bit1 += g_encode[int(code[1+i])]

        for i in range(6):                              # digit 8-13
            bit2 += r_encode[int(code[7+i])]

        canvas.create_text(220,90,font="Halvetica 20 bold",
                        text="EAN-13 Barcode:")
        
        # showing bar on canvas
        canvas.create_line(90,130,90,300, fill="blue",width=3)                  # start marker (101)     
        canvas.create_line(93,130,93,300, fill="white",width=3)
        canvas.create_line(96,130,96,300, fill="blue",width=3)

        canvas.create_text(75,315,font="Halvetica 20 bold", text= code[0])     # show the first digit of code on canvas 
    
        x = 99
        for i in bit1:                                                         # show bar digit 2-7
            filling = ""
            if i == "0":
                filling = "white"
            elif i == "1":
                filling = "green"
            canvas.create_line(x,130,x,285, fill=filling,width=3)
            x += 3
        
        x = 109
        for i in code[1:7]:                                                    # show the code on canvas (2-7)
            canvas.create_text(x,315,font="Halvetica 20 bold", text= i)
            x += 21

        canvas.create_line(225,130,225,300, fill="white",width=3)              # center marker (01010)
        canvas.create_line(228,130,228,300, fill="blue",width=3)
        canvas.create_line(231,130,231,300, fill="white",width=3)
        canvas.create_line(234,130,234,300, fill="blue",width=3)
        canvas.create_line(237,130,237,300, fill="white",width=3)
        
        x = 240                    
        for i in bit2:                                                         # show bar digit 8-13
            filling = ""
            if i == "0":
                filling = "white"
            elif i == "1":
                filling = "green"
            canvas.create_line(x,130,x,285, fill=filling,width=3)
            x += 3

        x = 250
        for i in code[7:]:                                                     # show the code on canvas (8-13)
            canvas.create_text(x,315,font="Halvetica 20 bold", text= i)
            x += 21

        canvas.create_line(366,130,366,300, fill="blue",width=3)               # end marker (101)
        canvas.create_line(369,130,369,300, fill="white",width=3)
        canvas.create_line(372,130,372,300, fill="blue",width=3)

        canvas.create_text(220,355,font="Halvetica 20 bold", text= f"Check Digit: {code[-1]}", fill="orange")      # Show the checkdigit of code
    
        self.canvas.postscript(file=self.file.get(), colormode="color")                                             # write canvas in postscript file

# main function
def main():
    root = tk.Tk()
    my_gui = BardcodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# contributor : Muhammad Naufal Zaky Alsar (2106752041)
