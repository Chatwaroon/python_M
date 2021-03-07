from tkinter import *
from tkinter import ttk #ttk is theme of tk
import csv



#CSV file
def writetoCSV(data):
     with open('data.csv','a',newline = '',encoding='utf-8') as file:
          fw = csv.writer(file) # fw = file writer
          fw.writerow(data)
     print('บันทึกไฟล์สำเร็จ')
     

GUI = Tk() #Tk คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมของมิ้นท์สวย')
GUI.geometry('500x300') # 500 = กว้าง,300=สูง


#font
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',20,)


#title 1
L1 = ttk.Label(GUI,text='หัวข้อ', font = FONT1,foreground = 'green')
L1.pack() # นำ L1 ไปติดกับโปรแกรมหลัก


#text box1

V_title = StringVar() #StringVar()  เป็นตัวแปรพิเศษที่เก็บข้อมูลไว้ในGUI  สามารถเปลี่ยนแปลงได้ตลอด
E1 = ttk. Entry(GUI, textvariable = V_title , font = FONT2, width=30)
E1.pack()

#title 1
L2 = ttk.Label (GUI,text ='รายละเอียด',  font = FONT1,foreground = 'green')
L2.pack()




#text box2
V_detail = StringVar()
E2 = Entry(GUI, textvariable = V_detail, font = FONT2,width=40)
E2.pack()


#button1
def SaveButton(event=None):
     title = V_title.get()  # .get() ดึงข้อมูลจากตัวแปร V_title
     detail = V_detail.get()
     print(title)
     print(detail)
     dt = [title,detail]
     writetoCSV(dt)  #dt = data
     print('กำลังบันทึกข้อมูล.....')
     #clear ข้อมูล
     V_title.set('') #สั่งเคลียร์ข้อมูลให้ว่าง
     V_detail.set('') #สั่งเคลียร์ข้อมูลให้ว่าง

     #ทำให้เคอร์เชอร์ไปอยู่ช่องกรอกตำแหน่งแรก
     E1.focus()

E2.bind('<Return>',SaveButton)
#E2.bind เช็คในช่องกรอกที่2 ว่ามีการกดEnter หรือไม่  หากกดให้ทำการเรียกฟังชั่น SaveButton
B1 = Button(GUI,text = 'seve',  font = FONT1, command=SaveButton)
B1.pack(ipadx = 20,ipady=30,pady=20)
#ipadx = ระยะห่างภายในปุ๋ม แนวแกนx
#pady = ระยะห่างด้านนอกปุ่ม ทั้งบนและล่างแกนy










GUI.mainloop()
#GUI.mailloop() จาก GUI จะทำให้โปรแกรมรันตลอด


