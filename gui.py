def wide(groups):
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
    frame7 = tk.Frame(root)

    for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7):
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
    qualified_teams= []
    def groupFrame(id, parent_frame):
        show_frame(parent_frame)
        frame = tk.LabelFrame(parent_frame, text=f'Group {id+1}').place(x=120, y=250)

        entries= []
        for i in range(6):
            l = tk.Label(frame,text=f'{groups[id].matches[i][0]} VS {groups[id].matches[i][1]}',font=('Helvetica bold', 22)).place(x=200 + (400) * (i //3), y=40+120*(i%3))
            e = tk.Entry(frame,width=20)
            e.place(x=200 + (400) * (i //3), y=100+120*(i%3),height=50,width=300)
            entries.append(e)
        
        def play(id):
            for i in range(6):
                result = entries[i].get().split('-')
                groups[id].play(groups[id].matches[i], result)
            
            qualified_teams.append(groups[id].top()[0][0])
            qualified_teams.append(groups[id].top()[1][0])
            show_frame(frame2)
   
        b = tk.Button(frame,text='Save',font=('Helvetica bold', 26),command=lambda:play(id)).place(x=400, y=500)
        b = tk.Button(frame,text='Back',font=('Helvetica bold', 26),command=lambda:show_frame(frame2)).place(x=600, y=500)

    

    #create buttons for each group in groups
    for i in range(4):
        b = tk.Button(frame2,text=f'Group {i+1}',font=('Helvetica bold', 26),command=lambda i=i:groupFrame(i, frame7)).place(x=350, y=150+120*i)
    
    for i in range(4, 8):
        b = tk.Button(frame2,text=f'Group {i+1}',font=('Helvetica bold', 26),command=lambda i=i:groupFrame(i, frame7)).place(x=350 + 200, y=150+120*(i-4))

    frame2_txt = tk.Label(frame2,text='Choose A Group',font=('Helvetica bold', 36)).place(x=350,y=30)
    frame2_btn = tk.Button(frame2, text='Next',command=lambda:show_frame(frame3)).pack(fill='x', ipady=25,side='bottom')











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

    frame2_btn = tk.Button(frame4, text='Next',command=lambda:show_frame(frame5)).pack(fill='x', ipady=15)










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