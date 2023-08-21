from tkinter import*
r=Tk()
r.geometry("600x500")
r.title("To_do_list")
r.configure(bg="maroon")
r.resizable(0,0)

#defining function for adding tasks
def addtask():
         task=label_task_entry.get()
         listbox_tasks.insert(END,task)


def edittask():
        label_task_entry.delete( 0,END)
        
#defining function for clear task one by one
def cleartask():
         task=label_task_entry.get()
         listbox_tasks.delete(END)
  
#defining functions for clear all task
def deltask():
         task=label_task_entry.get()
         listbox_tasks.delete(0,END)
        
head=Label(r,text="    TO DO LIST    ",bg="Maroon",fg="white",width=40,height=1,font=("segoe print",20,"bold"))
head.pack()

listbox_tasks=Listbox(r,width=40,height=24,bg="black",fg="PINK")
listbox_tasks.place(x=300,y=100)

label=Label(r,text="ENTER THE TASK:-",bg="maroon",fg="white",font=("segoe print",15,"bold"))
label.place(x=30,y=100)
label_task_entry=Entry(r,bg="GREY",fg="white",font=20)
label_task_entry.place(x=30,y=140)

add_task=Button(r,text="ADD TASK",width=20,height=1,bg="black",fg="white",font=("source sans pro semibold",15,"bold"),command=lambda:addtask() )
add_task.place(x=30,y=200)

Edit_task=Button(r,text="EDIT TASK",width=20,height=1,bg="black",fg="white",font=("source sans pro semibold",15,"bold"),command=lambda:edittask())
Edit_task.place(x=30,y=260)

clear_task=Button(r,text="CLEAR TASK",width=20,height=1,bg="black",fg="white",font=("source sans pro semibold",15,"bold"),command=lambda:cleartask())
clear_task.place(x=30,y=320)

del_task=Button(r,text="DELETE ALL TASK",width=20,height=1,bg="black",fg="white",font=("source sans pro semibold",15,"bold"),command=lambda:deltask())
del_task.place(x=30,y=380)

EXIT=Button(r,text="EXIT",width=20,bg="black",height=1,fg="white",font=("source sans pro semibold",15,"bold"),command=lambda:exit())
EXIT.place(x=30,y=440)




