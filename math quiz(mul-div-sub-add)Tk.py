from tkinter import *
import random
from PIL import Image, ImageTk
#------------Define the functions------------
def sub():
    def restart():
        def handle_click(button):
            if str(button.cget("text")) == str(third_number_result):
                button.config(background="green")
            else:
                button.config(background="red")
                for other_button in [bt1, bt2, bt3]:
                    if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                        other_button.config(background="green")
                

        first_number_question=random.randint(20,10000)
        second_number_question=random.randint(20,10000)
        counter1=random.randint(-5,5)
        counter2=random.randint(2,10)

        first_number_result=first_number_question-second_number_question+counter1
        second_number_result=first_number_question-second_number_question+counter2
        third_number_result=first_number_question-second_number_question
            
        x=[first_number_result,second_number_result,third_number_result]
        random.shuffle(x)
            
        en.config(state="normal")
        en.delete(0,END)
        en.insert(0,str(first_number_question)+"-"+str(second_number_question))
        en.config(state="disabled")
            
        bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
        bt1.place(x=40,y=130)

        bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
        bt2.place(x=156,y=130)

        bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
        bt3.place(x=270,y=130)



    #----------Numbers---------------
    first_number_question=random.randint(20,10000)
    second_number_question=random.randint(20,10000)

    counter1=random.randint(2,10)
    counter2=random.randint(-5,5)

    first_number_result=first_number_question-second_number_question+counter1
    second_number_result=first_number_question-second_number_question+counter2
    third_number_result=first_number_question-second_number_question

    x=[first_number_result,second_number_result,third_number_result]
    random.shuffle(x)


    def handle_click(button):
        if str(button.cget("text")) == str(third_number_result):
            button.config(background="green")
        else:
            button.config(background="red")
            for other_button in [bt1, bt2, bt3]:
                if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                    other_button.config(background="green")
    #----------Design the window-----------
    pro=Tk()
    pro.title("Subtraction training")
    pro.geometry('400x300')
    pro.config(background="#232946")

    lbl=Label(pro,text="Find the solution!",bg="#232946",fg="#fffffe")
    lbl.place(x=145,y=50)

    en=Entry(pro,font="arial",bg="#7D8787",fg="#343626")
    en.place(x=87,y=90)
    en.insert(0,str(first_number_question)+"-"+str(second_number_question))
    en.config(state="disabled")

    bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
    bt1.place(x=40,y=130)

    bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
    bt2.place(x=156,y=130)

    bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
    bt3.place(x=270,y=130)

    bt4=Button(pro,text="<<Next",bg="#eebbc3",fg="#232946",command=restart)
    bt4.place(x=20,y=220)

    pro.mainloop()

def add():
    def restart():
        def handle_click(button):
            if str(button.cget("text")) == str(third_number_result):
                button.config(background="green")
            else:
                button.config(background="red")
                for other_button in [bt1, bt2, bt3]:
                    if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                        other_button.config(background="green")
                

        first_number_question=random.randint(20,10000)
        second_number_question=random.randint(20,10000)
        counter1=random.randint(-5,5)
        counter2=random.randint(2,10)

        first_number_result=first_number_question+second_number_question+counter1
        second_number_result=first_number_question+second_number_question+counter2
        third_number_result=first_number_question+second_number_question
            
        x=[first_number_result,second_number_result,third_number_result]
        random.shuffle(x)
            
        en.config(state="normal")
        en.delete(0,END)
        en.insert(0,str(first_number_question)+"+"+str(second_number_question))
        en.config(state="disabled")
            
        bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
        bt1.place(x=40,y=130)

        bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
        bt2.place(x=156,y=130)

        bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
        bt3.place(x=270,y=130)



    #----------Numbers---------------
    first_number_question=random.randint(20,10000)
    second_number_question=random.randint(20,10000)

    counter1=random.randint(2,10)
    counter2=random.randint(-5,5)

    first_number_result=first_number_question+second_number_question+counter1
    second_number_result=first_number_question+second_number_question+counter2
    third_number_result=first_number_question+second_number_question

    x=[first_number_result,second_number_result,third_number_result]
    random.shuffle(x)


    def handle_click(button):
        if str(button.cget("text")) == str(third_number_result):
            button.config(background="green")
        else:
            button.config(background="red")
            for other_button in [bt1, bt2, bt3]:
                if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                    other_button.config(background="green")
    #----------Design the window-----------
    pro=Tk()
    pro.title("Addition training")
    pro.geometry('400x300')
    pro.config(background="#232946")

    lbl=Label(pro,text="Find the solution!",bg="#232946",fg="#fffffe")
    lbl.place(x=145,y=50)

    en=Entry(pro,font="arial",bg="#7D8787",fg="#343626")
    en.place(x=87,y=90)
    en.insert(0,str(first_number_question)+"+"+str(second_number_question))
    en.config(state="disabled")

    bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
    bt1.place(x=40,y=130)

    bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
    bt2.place(x=156,y=130)

    bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
    bt3.place(x=270,y=130)

    bt4=Button(pro,text="<<Next",bg="#eebbc3",fg="#232946",command=restart)
    bt4.place(x=20,y=220)

    pro.mainloop()

def div():
    def restart():
        def handle_click(button):
            if str(button.cget("text")) == str(third_number_result):
                button.config(background="green")
            else:
                button.config(background="red")
                for other_button in [bt1, bt2, bt3]:
                    if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                        other_button.config(background="green")
                

        first_number_question=random.randint(2,200)
        second_number_question=random.randint(2,30)
        counter1=random.random()
        counter2=random.random()

        first_number_result=first_number_question/second_number_question+counter1
        second_number_result=first_number_question/second_number_question+counter2
        third_number_result=first_number_question/second_number_question
            
        x=[first_number_result,second_number_result,third_number_result]
        random.shuffle(x)
            
        en.config(state="normal")
        en.delete(0,END)
        en.insert(0,str(first_number_question)+"/"+str(second_number_question))
        en.config(state="disabled")
            
        bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
        bt1.place(x=40,y=130)

        bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
        bt2.place(x=156,y=130)

        bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
        bt3.place(x=270,y=130)



    #----------Numbers---------------
    first_number_question=random.randint(2,200)
    second_number_question=random.randint(2,30)

    counter1=random.random()*2
    counter2=random.random()

    first_number_result=first_number_question/second_number_question+counter1
    second_number_result=first_number_question/second_number_question+counter2
    third_number_result=first_number_question/second_number_question

    x=[first_number_result,second_number_result,third_number_result]
    random.shuffle(x)


    def handle_click(button):
        if str(button.cget("text")) == str(third_number_result):
            button.config(background="green")
        else:
            button.config(background="red")
            for other_button in [bt1, bt2, bt3]:
                if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                    other_button.config(background="green")
    #----------Design the window-----------
    pro=Tk()
    pro.title("Division training")
    pro.geometry('400x300')
    pro.config(background="#232946")

    lbl=Label(pro,text="Find the solution!",bg="#232946",fg="#fffffe")
    lbl.place(x=145,y=50)

    en=Entry(pro,font="arial",bg="#7D8787",fg="#343626")
    en.place(x=87,y=90)
    en.insert(0,str(first_number_question)+"/"+str(second_number_question))
    en.config(state="disabled")

    bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
    bt1.place(x=40,y=130)

    bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
    bt2.place(x=156,y=130)

    bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
    bt3.place(x=270,y=130)

    bt4=Button(pro,text="<<Next",bg="#eebbc3",fg="#232946",command=restart)
    bt4.place(x=20,y=220)

    pro.mainloop()

def mul():
    def restart():
        def handle_click(button):
            if str(button.cget("text")) == str(third_number_result):
                button.config(background="green")
            else:
                button.config(background="red")
                for other_button in [bt1, bt2, bt3]:
                    if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                        other_button.config(background="green")
                

        first_number_question=random.randint(2,30)
        second_number_question=random.randint(2,30)
        counter1=random.randint(-5,5)
        counter2=random.randint(2,10)

        first_number_result=first_number_question*second_number_question+counter1
        second_number_result=first_number_question*second_number_question+counter2
        third_number_result=first_number_question*second_number_question
            
        x=[first_number_result,second_number_result,third_number_result]
        random.shuffle(x)

        en.config(state="normal")    
        en.delete(0,END)
        en.insert(0,str(first_number_question)+"*"+str(second_number_question))
        en.config(state="disabled")
            
        bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
        bt1.place(x=40,y=130)

        bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
        bt2.place(x=156,y=130)

        bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
        bt3.place(x=270,y=130)



    #----------Numbers---------------
    first_number_question=random.randint(2,20)
    second_number_question=random.randint(2,20)

    counter1=random.randint(2,10)
    counter2=random.randint(-5,5)

    first_number_result=first_number_question*second_number_question+counter1
    second_number_result=first_number_question*second_number_question+counter2
    third_number_result=first_number_question*second_number_question

    x=[first_number_result,second_number_result,third_number_result]
    random.shuffle(x)


    def handle_click(button):
        if str(button.cget("text")) == str(third_number_result):
            button.config(background="green")
        else:
            button.config(background="red")
            for other_button in [bt1, bt2, bt3]:
                if other_button != button and str(other_button.cget("text")) == str(third_number_result):
                    other_button.config(background="green")
    #----------Design the window-----------
    pro=Tk()
    pro.title("Multiplication training")
    pro.geometry('400x300')
    pro.config(background="#232946")

    lbl=Label(pro,text="Find the solution!",bg="#232946",fg="#fffffe")
    lbl.place(x=145,y=50)

    en=Entry(pro,font="arial",bg="#7D8787",fg="#343626")
    en.place(x=87,y=90)
    en.insert(0,str(first_number_question)+"*"+str(second_number_question))
    en.config(state="disabled")

    bt1=Button(pro,text=x[0],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt1))
    bt1.place(x=40,y=130)

    bt2=Button(pro,text=x[1],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt2))
    bt2.place(x=156,y=130)

    bt3=Button(pro,text=x[2],width=15,height=2,relief=RAISED,command=lambda: handle_click(bt3))
    bt3.place(x=270,y=130)

    bt4=Button(pro,text="<<Next",bg="#eebbc3",fg="#232946",command=restart)
    bt4.place(x=20,y=220)

    pro.mainloop()


pro=Tk()
pro.geometry('400x400')
pro.title("Quizera")
pro.config(bg="#0f0e17")
pro.resizable(False,False)


lbl30=Label(pro,text="Welcome to our program(Quizera)",font=("Arial",14),bg="#0f0e17",fg="#fffffe")
lbl30.pack()

bt30=Button(pro,text="Subtraction training",bg="#ff8906",fg="#fffffe",width=18,height=4,command=sub)
bt30.place(x=140,y=40)

bt31=Button(pro,text="Addition training",bg="#ff8906",fg="#fffffe",width=18,height=4,command=add)
bt31.place(x=140,y=120)

bt32=Button(pro,text="Division training",bg="#ff8906",fg="#fffffe",width=18,height=4,command=div)
bt32.place(x=140,y=200)

bt33=Button(pro,text="Multiplication training",bg="#ff8906",fg="#fffffe",width=18,height=4,command=mul)
bt33.place(x=140,y=280)

pro.mainloop()