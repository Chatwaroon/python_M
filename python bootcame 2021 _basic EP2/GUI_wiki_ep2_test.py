import wikipedia
wikipedia.set_lang('th')
from tkinter import*
from tkinter import ttk
GUI = Tk()
GUI.title('โปรแกรม wiki น้องมิ้นท์')
GUI.geometry('400x300')

FONT1 = ('Angsana New',15)



v_search = StringVar()
E1 = ttk.Entry(GUI,textvariable = v_search,font = FONT1 , width = 40)
E1.pack(pady=20)

def search():
     keyword = v_search.get()
     try:
          wiki(keywork,language)
     except:
          messagebox.showwarning('keyword Error', 'กรุณากรอกคำค้นหาใหม่')

B1 = ttk.Button(GUI,text = 'search',command = search)
B1.pack(ipadx=20,ipady=10)

GUI.mainloop()

