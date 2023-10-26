from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_convert():
    print("Convert")

root = Tk()

root.title('DCT FILE')
root.iconbitmap('favicon1.ico')

root.geometry('350x500')

root.configure(background='#0096DC')
img = Image.open('logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text='DCT File Converter',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

status_lable = Label(root,text='Loading...',fg='white',bg='#0096DC')
status_lable.pack(pady=(20,5))
status_lable.config(font=('verdana',12))

message_lable = Label(root,text='Your File is Converted',fg='white',bg='#0096DC')
message_lable.pack(pady=(20,5))
message_lable.config(font=('verdana',12))


login_btn = Button(root,text='Convert Data',bg='white',fg='black',width=20,height=2,command=handle_convert)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))



root.mainloop()