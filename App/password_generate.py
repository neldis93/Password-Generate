from tkinter import *
from tkinter import messagebox
import random
#import hashlib
from werkzeug.security import generate_password_hash


class Application(Frame):

    def __init__(self, password=None, master=None):
        super().__init__(master,width=350, height=250)
        self.master = master
        self.create_widgets() 
        self.pack()
        self.password = password

    def password_generate(self):
        # Clear entry box
        self.pw_entry.delete(0,END) 
        try:
            # Get PW length and convert to integer
            pw_length = int(self.my_entry.get())
            # Create a variable to hold our password 
            self.password = ''
            # Loop through password length
            for _ in range(pw_length):
                self.password += chr(random.randint(33,126))
            self.pw_entry.insert(0,self.password)

        except ValueError:
            messagebox.showerror('Error', 'Empty field, please enter a value')
        
    def encrypt_password(self):
        self.pw_entry2.delete(0,END)
        try:
            encrypt_pass = generate_password_hash(self.password)
            self.pw_entry2.insert(0,encrypt_pass) 
        except TypeError:
            messagebox.showerror('Error', 'Empty field, please enter a value')

    def clipper_pass(self):
        # Clear the clipboard
        root.clipboard_clear()
        # Copy to clipboard
        root.clipboard_append(self.pw_entry.get())
        
    def clipper_encrypt(self):
        root.clipboard_clear()
        root.clipboard_append(self.pw_entry2.get())

    def create_widgets(self):
        # Label frame
        self.lf = LabelFrame(root,text='How many characters?')
        self.lf.pack(pady=20)

        # Create entry box to designate number of character
        self.my_entry = Entry(self.lf,font=('Helvetica',24))
        self.my_entry.pack(pady=20,padx=20)

        # Create entry box for our returned password 
        self.pw_entry = Entry(root, text = '', font = ('Helvetica',24), bd=0, background = 'lightGrey')
        self.pw_entry.pack(pady=20)

        self.pw_entry2 = Entry(root, text = '', font = ('Helvetica',24), bd=0, background = 'lightGrey')
        self.pw_entry2.pack(pady=20)

        # Password button
        self.my_button = Button(self, text='Generate Password', command = lambda:self.password_generate()) 
        self.my_button.grid(row=0, column=0, padx=10)

        self.my_button2 = Button(self,text='Encrypt Password', command = lambda:self.encrypt_password())
        self.my_button2.grid(row=0, column=1, padx=10)

        # Clip button
        self.clip_button = Button(self, text='Copy password', command = lambda: self.clipper_pass())
        self.clip_button.grid(row=0, column=2, padx=10)

        self.clip_button2 = Button(self, text='Copy Encrypt password', command = lambda: self.clipper_encrypt())
        self.clip_button2.grid(row=0, column=3, padx=10)


if __name__ == '__main__':
    root = Tk()
    root.title('Password Generator')
    app=Application(master=root)
    app.mainloop()
