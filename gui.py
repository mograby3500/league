import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    
root = tk.Tk()
root.title('World Cup')
root.geometry('1080x720')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0,column=0,sticky='nsew')





    
#==================Frame 1 code

text1 = tk.Label(frame1,text='Welcome to World Cup App',font=('Helvetica bold', 48)).place(x=140, y=100)
text2 = tk.Label(frame1,text='Please Choose',font=('Helvetica bold', 26)).place(x=400, y=200)


button1 = tk.Button(frame1,text='Group Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame2))
button1.place(x=320, y=270, height=100, width=400)

button2 = tk.Button(frame1,text='Knockout Stage',font=('Helvetica bold', 26),state='disabled')
button2.place(x=320, y=390, height=100, width=400)

button3 = tk.Button(frame1,text='Show Winners',font=('Helvetica bold', 26),state='disabled')
button3.place(x=320, y=510, height=100, width=400)












#==================Frame 2 code
Results=[[],[],[],[],[],[],[],[]]

def g_matches(i):
    
    m1 = tk.LabelFrame(frame2, text='match 1').place(x=320, y=390)
    l1 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=350, y=20)
    e1 = tk.Entry(m1,width=20)
    Results[i][0] = e1.get()
    
    m2 = tk.LabelFrame(frame2, text='match 2').place(x=320, y=490)
    l2 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=350, y=40)
    e2 = tk.Entry(m1,width=20)
    Results[i][1] = e2.get()

    m3 = tk.LabelFrame(frame2, text='match 3').place(x=320, y=590)
    l3 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=350, y=60)
    e3 = tk.Entry(m1,width=20)
    Results[i][2] = e3.get()

    m4 = tk.LabelFrame(frame2, text='match 4').place(x=520, y=390)
    l4 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=550, y=20)
    e4 = tk.Entry(m1,width=20)
    Results[i][3] = e4.get()

    m5 = tk.LabelFrame(frame2, text='match 5').place(x=520, y=490)
    l5 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=550, y=40)
    e5 = tk.Entry(m1,width=20)
    Results[i][4] = e5.get()

    m6 = tk.LabelFrame(frame2, text='match 6').place(x=520, y=590)
    l6 = tk.Label(m1,text='MATCH VS MATCH',font=('Helvetica bold', 26)).place(x=550, y=60)
    e6 = tk.Entry(m1,width=20)
    Results[i][5] = e6.get()

    return m1,l1,e1,m2,l2,e2,m3,l3,e3,m4,l4,e4,m5,l5,e5,m6,l6,e6
    




def selc(event):
    if clicked.get() == 'Group A':
        g_matches(0)
    elif clicked.get() == 'Group B':
        g_matches(1)
    elif clicked.get() == 'Group C':
        g_matches(2)
    elif clicked.get() == 'Group D':
        g_matches(3)
    elif clicked.get() == 'Group E':
        g_matches(4)
    elif clicked.get() == 'Group F':
        g_matches(5)
        
        
        
        
        
        
        
        
        
        
t1 = tk.Label(frame2,text='Choose A Group',font=('Helvetica bold', 26)).place(x=350, y=20)

groups = ['Group A','Group B','Group C','Group D','Group E','Group F']
clicked = tk.StringVar()
drop = tk.OptionMenu(frame2, clicked,*groups).place(x=650, y=30)


frame2_btn = tk.Button(frame2, text='Next',command=lambda:show_frame(frame3)).pack(fill='x', side= 'bottom')











#==================Frame 3 code
text3 = tk.Label(frame3,text='Welcome to World Cup App',font=('Helvetica bold', 48)).place(x=140, y=100)
text4 = tk.Label(frame1,text='Please Choose',font=('Helvetica bold', 26)).place(x=400, y=200)


button4 = tk.Button(frame3,text='Group Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame2))
button4.place(x=320, y=270, height=100, width=400)

button5 = tk.Button(frame3,text='Knockout Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame4))
button5.place(x=320, y=390, height=100, width=400)

button6 = tk.Button(frame3,text='Show Winners',font=('Helvetica bold', 26),state='disabled')
button6.place(x=320, y=510, height=100, width=400)













#==================Frame 4 code
frame4_title=  tk.Label(frame4, text='KnockOut', font='times 35', bg='yellow')
frame4_title.pack(fill='both', expand=True)

frame2_btn = tk.Button(frame4, text='Enter',command=lambda:show_frame(frame5)).pack(fill='x', ipady=15)










#==================Frame 5 code
text5 = tk.Label(frame5,text='Welcome to World Cup App',font=('Helvetica bold', 48)).place(x=140, y=100)
text6 = tk.Label(frame5,text='Please Choose',font=('Helvetica bold', 26)).place(x=400, y=200)


button7 = tk.Button(frame5,text='Group Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame2))
button7.place(x=320, y=270, height=100, width=400)

button8 = tk.Button(frame5,text='Knockout Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame4))
button8.place(x=320, y=390, height=100, width=400)

button9 = tk.Button(frame5,text='Show Winners',font=('Helvetica bold', 26),command=lambda:show_frame(frame6))
button9.place(x=320, y=510, height=100, width=400)












#==================Frame 6 code
frame6_title=  tk.Label(frame6, text='Winners', font='times 35', bg='yellow')
frame6_title.pack(fill='both', expand=True)

frame6_btn = tk.Button(frame6, text='Back',command=lambda:show_frame(frame5)).pack(fill='x', ipady=15)


show_frame(frame1)

root.mainloop()