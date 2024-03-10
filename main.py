import customtkinter
from tkinter import *
from PIL import ImageTk, Image


def main():
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue") 
    root = customtkinter.CTk()
    gui = Window(root)
    gui.root.mainloop()
    

class Window:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1150x500')
        self.root.resizable(0, 0)
        self.root.title("AI Lecture Buddy")
        
        # Create frames
        top_frame = customtkinter.CTkFrame(root, width=400, height=200)
        top_frame.grid(row=0, column=0, sticky='ns', padx=10, pady=5)

        bottom_frame = customtkinter.CTkFrame(root, width=650, height=1000)
        bottom_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=5)

        
        # Create record, clear, and save buttons
        top_frame.saveB=customtkinter.CTkButton(top_frame, text="Save", command=self.save).grid(row=1, column=0, padx=20, pady=(20, 10))
        self.button3=customtkinter.CTkButton(top_frame, text="Clear", command=self.clear).grid(row=2, column=0, padx=20, pady=(20, 10))
        self.button3=customtkinter.CTkButton(top_frame, text="Record", command=self.record).grid(row=3, column=0, padx=20, pady=(20, 10))
        logo_label = customtkinter.CTkLabel(top_frame, text="AI Notetaker", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create transcript textspace
        bottom_frame.textspace = customtkinter.CTkTextbox(bottom_frame, padx=5, pady=5, width=400,height=470, wrap=WORD)
        bottom_frame.textspace.grid(row=0, column=0, padx=10, pady=10)

        # Load and display the image for the search button
        image = Image.open("right-arrow.jpg")
        img = image.resize((50, 50))  # Resize the image
        img = ImageTk.PhotoImage(img)
        test=customtkinter.CTkImage(light_image=Image.open("right-arrow.jpg"), size=(50,50))
        customtkinter.CTkButton(bottom_frame,text="", image=test, command=self.search,width=50).grid(row=0, column=1, padx=5, pady=0)

        # Create note textspace
        bottom_frame.notetextspace = customtkinter.CTkTextbox(bottom_frame, padx=5, pady=5, width=400,height=470, wrap=WORD)
        bottom_frame.notetextspace.grid(row=0, column=2, padx=10, pady=10)
		
    def clear(self):
        print("todo")
    
    def search(self):
        print("todo")
		
	
    def save(self):
        print("todo")

    def openfile(self):
        print("todo")
    
    def record(self):
        print("todo")
    
    
    
    
    
    
    
main()