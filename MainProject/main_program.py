from Tkinter import *
import tkMessageBox

from AESEncDec import *
from MD5Hashing import *
from RSAEncDec import *

color = 'lightblue' #color our background


class Application(Frame):

    def __init__(self, root=None):

        Frame.__init__(self, root)
        self.frame_width = 700
        self.frame_height = 400

        # Set configuration our frame
        self.config(width = self.frame_width, height = self.frame_height, bg = color) 
        self.pack()

        # Create textBox for input data
        self.textbox_one = Text()
        self.textbox_one.place(x = 30, y = 170, height = 200, width = 300 )

        # Create textBox for result
        self.textbox_two = Text()
        self.textbox_two.place(x = 370, y = 170, height = 200, width = 300 )

        label_input_text = Label( text = "Input text: ", bg = color)
        label_input_text.place(x = 30, y = 155, height = 10, width = 70 )

        label_output_text = Label( text = "Result: ", bg = color)
        label_output_text.place(x = 370, y = 155, height = 10, width = 50 )

        # IntVar help to detect, what radioButton was chosen
        self.var = IntVar()

        # Create radioButton for AES
        self.AES_radiobutton = Radiobutton(text = 'AES algorithm', bg = color, variable=self.var, value=0)
        self.AES_radiobutton.place(x = 100, y = 20, height = 30, width = 100 )

        # Create radioButton for DSA
        self.DSA_radiobutton = Radiobutton(text = 'DSA algorithm', bg = color, variable=self.var, value=1)
        self.DSA_radiobutton.place(x = 100, y = 70, height = 30, width = 100 )

        # Create radioButton for Hash function
        self.HF_radiobutton = Radiobutton(text = 'Hash function', bg = color, variable=self.var, value=2)
        self.HF_radiobutton.place(x = 100, y = 120, height = 30, width = 100 )

        # Create label
        self.lable_for_ask_bits = Label(text = 'Input size of bits:', bg = color)
        self.lable_for_ask_bits.place(x = 210, y = 70, height = 30, width = 100 )

        # Create textBox for input bits
        self.input_bits = Text()
        self.input_bits.place(x = 310, y = 75, height = 20, width = 50 )
        self.input_bits.insert(INSERT, '16')
        
        # Create button to encrypt text
        self.encrypt_button = Button(root, text = "Encrypt text", command = self.encrypt_text)
        self.encrypt_button.place(x = 420, y = 20, height = 80, width = 100 )

        # Create button to decrypt text
        self.decrypt_button = Button(root, text = "Decrypt text", command = self.decrypt_text)
        self.decrypt_button.place(x = 540, y = 20, height = 80, width = 100 )

        # Create button to hash
        self.hash_button = Button(root, text = "Hash text", command = self.hashing )
        self.hash_button.place(x = 420, y = 120, height = 30, width = 220)

        # Create AES object, keyword "this is a very strong key"
        # You can change keyword
        self.AES = AESEncDec('this is a very strong key')

        # Save bits
        self.bit_length = 16
        # Create RSA object
        self.RSA = RSAEncDec(self.bit_length)


    def encrypt_text(self):
        self.textbox_two.delete("1.0", END)
        # Get radioButton selection
        selection = self.var.get()
        # if chosen AES
        if selection == 0:
            # Read text from input
            message = self.textbox_one.get("1.0", END)
            encrypt_message = self.AES.encrypt(message)
            # Output result
            self.textbox_two.insert(INSERT, encrypt_message)
        # if chosen RSA
        elif selection == 1:
            try:
                # Read number of bits
                tmp_bits = int(self.input_bits.get("1.0", END))
                # if bits not in range from 4 to 32 print error message
                if tmp_bits < 4 or tmp_bits > 32:
                    tkMessageBox.showerror(message ='Bits must be in range from 4 to 32')
                else:
                    # else, if tmp_bits not = self.bit_length: create new object
                    if tmp_bits != self.bit_length:
                        self.bit_length = tmp_bits
                        self.RSA = RSAEncDec(self.bit_length)
            except:
                tkMessageBox.showerror(message ='You must input integer number')

            # Find max number
            max_number = self.RSA.get_max_value_to_encrypt()

            try:
                # Read text from input (myst be number)
                message = int(self.textbox_one.get("1.0", END))
                if message < 0 or message > max_number:
                    tkMessageBox.showerror(message ='Input text must be number in range from 0 to ' + str(max_number))
                else:
                    encrypt_message = self.RSA.encrypt(message)
                    # Output result
                    self.textbox_two.insert(INSERT, encrypt_message)
            except:
                tkMessageBox.showerror(message ='Input text must be number in range from 0 to ' + str(max_number))
        else:
            tkMessageBox.showinfo(message ='You must select "AES" or "RSA" radioButton')
            

    def decrypt_text(self):
        self.textbox_two.delete("1.0", END)
        # Get radioButton selection
        selection = self.var.get()
        # if chosen AES
        if selection == 0:
            # Read text from input
            message = self.textbox_one.get("1.0", END)
            decrypt_message = self.AES.decrypt(message)
            # Output result
            self.textbox_two.insert(INSERT, decrypt_message)
        elif selection == 1:
            # Read text from input
            message = int(self.textbox_one.get("1.0", END))
            decrypt_message = self.RSA.decrypt(message)
            # Output result
            self.textbox_two.insert(INSERT, decrypt_message)
        else:
            tkMessageBox.showinfo(message ='You must select "AES" or "RSA" radioButton')

    def hashing(self):
        # Get radioButton selection
        selection = self.var.get()
        # if chosen Hash function
        if selection == 2:
            # Read text from input
            message = self.textbox_one.get("1.0", END)
            # Hashing
            hashing_message = Hashing(message)
            # Output result
            self.textbox_two.insert(INSERT, hashing_message)
        else:
            tkMessageBox.showinfo(message ='You must select "Hash function" radioButton')
        

#create object TK class
the_window = Tk(className = " Cryptographic")
#create object Application
app = Application(the_window)
#run our Application
app.mainloop()
