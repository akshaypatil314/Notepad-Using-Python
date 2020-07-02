from tkinter import *
from tkinter import filedialog
import wikipedia
import speech_recognition as sr
from tkinter.font import Font

class notepad:
    current_open_file="no_file"

    def open_me(self):
        self.text_area.delete(1.0,END)
        open_return=filedialog.askopenfile(initialdir="C:/Users/Akshay/Desktop",filetypes=(("text files",".txt"),("All files","*.*")))
        for line in open_return: 
            self.text_area.insert(END,line)
        self.current_open_file=open_return.name
        open_return.close()
        

    def save_me(self):
        save_return=filedialog.asksaveasfile(mode="w",initialdir="C:/Users/Akshay/Desktop",defaultextension=(".txt"))
        if(save_return is None):
            return
        text2save=self.text_area.get(1.0,END)
        self.current_open_file=save_return.name
        save_return.write(text2save)
        save_return.close()

    def save(self):
        if(self.current_open_file=="no_file"):
            self.save_me()
        else:
            text3save=open(self.current_open_file,mode="w+")
            text3save.write(self.text_area.get(1.0,END))
            text3save.close()
            
    def new_file(self):
          self.text_area.delete(1.0,END)
          self.current_open_file="no file"

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")


    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
        
    def click_me(self):
        entry_value=self.entry.get()
        self.answer.delete(1.0,END)
        try:
            answer_value=wikipedia.summary(entry_value)
        except:
            self.answer.insert(INSERT,"Put some input or check what you enter")
        self.answer.insert(INSERT,answer_value)

    def search_me(self):
        self.master=Tk()
        self.frame=Frame(self.master)
        self.entry=Entry(self.frame)
        self.entry.pack()
        self.b1=Button(self.frame,text="Serach",command=self.click_me).pack()
        self.frame.pack(side=TOP)
        self.frame1=Frame(self.master)
        self.answer=Text(self.frame1,wrap=WORD,width=30,height=15)
        self.answer.pack()
        self.frame1.pack(side=BOTTOM)
        self.master.mainloop()

    def speek_me(self):
        r1=sr.Recognizer()
        r1.energy_threshold=8000
        with sr.Microphone() as source:
            print("Speek Anything")
            audio=r1.listen(source)
            try:
                text=r1.recognize_google(audio)
                print(self.text_area.insert(INSERT,text))
            except:
                print("Sorry could not recognize your voice")

        
        
    def __init__(self,master):
        self.master=master
        self.master.title("Notepad")
        self.customfont=Font(family="Helvetica",size=12)
        self.menu_font=('Verdana',10)
        self.text_area=Text(font=self.customfont)
        self.text_area.pack(fill=BOTH,expand=1)
        
        self.main_menu=Menu(self.master,font=self.menu_font)
        self.master.config(menu=self.main_menu)

        self.file_menu=Menu(self.main_menu,tearoff=False,font=self.menu_font)
        self.main_menu.add_cascade(label="File",menu=self.file_menu,font=self.menu_font)
        self.file_menu.add_command(label="New",command=self.new_file,font=self.menu_font)
        self.file_menu.add_command(label="Open",command=self.open_me,font=self.menu_font)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save",command=self.save,font=self.menu_font)
        self.file_menu.add_command(label="Save as",command=self.save_me,font=self.menu_font)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="exit",command=self.master.quit)

        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu,font=self.menu_font)
        self.edit_menu.add_command(label="Copy",command=self.copy_text,font=self.menu_font)
        self.edit_menu.add_command(label="Cut",command=self.cut_text,font=self.menu_font)
        self.edit_menu.add_command(label="Paste",command=self.paste_text,font=self.menu_font)

        self.wikipedia_menu=Menu(self.main_menu,tearoff=False,font=self.menu_font)
        self.main_menu.add_cascade(label="Wikipedia",menu=self.wikipedia_menu,font=self.menu_font)
        self.wikipedia_menu.add_command(label="Search",command=self.search_me,font=self.menu_font)        

        self.Speek_menu=Menu(self.main_menu,tearoff=False,font=self.menu_font)
        self.main_menu.add_cascade(label="Speek Now",menu=self.Speek_menu,font=self.menu_font)
        self.Speek_menu.add_command(label="Start",command=self.speek_me,font=self.menu_font) 
 

root=Tk()
te=notepad(root)
root.mainloop()
