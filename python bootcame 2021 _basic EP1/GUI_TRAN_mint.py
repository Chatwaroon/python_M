#GUI TRA
from tkinter import *
#จากไลบรารีชื่อ tkinter; *ให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk #ttk is theme of tk เพราะว่าการimport จะมาเฉพราะไฟล์เมน เรียกเฉพราะttk


###-------googletrans----------
from googletrans  import Translator
translator = Translator()

     
     


GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry( '500x300' ) #ขนาดหน้าจอ ขยายให้ใหญ่ขึ้น กว้าง*สูง
GUI.title('โปรแกรมแปลภาษา by Uncle Engineer')  #เปลี่ยนชื่อหัวโปรแกรม

#----------config-------------------
FONT = ('Angsana New',15) #เพื่อจะเอ้าfontไปใช้กับจุดอื่นได้


#---------Label------------------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font = FONT)
L.pack()
#---------------Entry (ช่องกรอกข้อความ)------------------
v_vocab = StringVar() #ช่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font = FONT,width=40)
E1.pack(pady=20)



#--------------------------------Button---------------------------------
#สร้างButton ปุ่มแปล ปุ่มต้องมีการผูกกับฟังชัน

def Translate():
     vocab = v_vocab.get() #.get คือให้แสดงผออกมา
     meaning = translator.translate(vocab,dest = 'th')
     print(vocab + ' : ' + meaning.text)
     print(meaning.pronunciation)
     V_result.set(vocab +' : '+meaning.text)
     
B1 = ttk.Button(GUI,text = 'Translate',command = Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10)  #showปุ่มขึ้นมาวางจากบนลงล่าง ipadx,ipady ขนาดของปุ่มกด

#---------Label------------------
L = ttk.Label(GUI,text='คำแปล',font = FONT)
L.pack()

#--------------Result------------------
v_result = Stringvar() #กล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label (GUI,textvariable = V_result,font = FONT2, foreground = 'green')
R1.pack()



GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลา จนกว่าจะปิด ต้องอยู่บรรทัดสุดท้ายเท่านั้น

