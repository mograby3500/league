def wide(groups):
    import tkinter as tk
        
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


    for frame in (frame1, frame2, frame3, frame4, frame5):
        frame.grid(row=0,column=0,sticky='nsew')

    def show_frame(frame):
            frame.tkraise()


        
    #==================Frame 1 code

    text1 = tk.Label(frame1,text='Welcome to World Cup App',font=('Helvetica bold', 48)).place(x=140, y=100)
    text2 = tk.Label(frame1,text='Please Choose',font=('Helvetica bold', 26)).place(x=400, y=200)


    button1 = tk.Button(frame1,text='Group Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame2))
    button1.place(x=320, y=330, height=100, width=400)

    button2 = tk.Button(frame1,text='Knockout Stage',font=('Helvetica bold', 26),state='disabled')
    button2.place(x=320, y=490, height=100, width=400)






    #==================Frame 2 code
    qualified_teams= []
    def groupFrame(id, parent_frame):
        show_frame(parent_frame)
        frame = tk.LabelFrame(parent_frame, text=f'Group {id+1}').place(x=120, y=250)

        entries= []
        for i in range(6):
            l = tk.Label(frame,text=f'{groups[id].matches[i][0]} VS {groups[id].matches[i][1]}',font=('Helvetica bold', 22)).place(x=200 + (400) * (i //3), y=40+120*(i%3))
            e = tk.Entry(frame,width=20, font=('Helvetica bold', 26))
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
        b = tk.Button(frame2,text=f'Group {i+1}',font=('Helvetica bold', 26),command=lambda i=i:groupFrame(i, frame5)).place(x=350, y=150+120*i)
    
    for i in range(4, 8):
        b = tk.Button(frame2,text=f'Group {i+1}',font=('Helvetica bold', 26),command=lambda i=i:groupFrame(i, frame5)).place(x=350 + 200, y=150+120*(i-4))

    frame2_txt = tk.Label(frame2,text='Choose A Group',font=('Helvetica bold', 36)).place(x=350,y=30)
    frame2_btn = tk.Button(frame2, text='Next',command=lambda:show_frame(frame3)).pack(fill='x', ipady=25,side='bottom')







    #==================Frame 3 code

    text3 = tk.Label(frame3,text='Welcome to World Cup App',font=('Helvetica bold', 48)).place(x=140, y=100)
    text4 = tk.Label(frame1,text='Please Choose',font=('Helvetica bold', 26)).place(x=400, y=200)


    button4 = tk.Button(frame3,text='Group Stage',font=('Helvetica bold', 26),command=lambda:show_frame(frame2))
    button4.place(x=320, y=330, height=100, width=400)

    button5 = tk.Button(frame3,text='Knockout Stage',font=('Helvetica bold', 26),command=lambda:showKnockout(Cup(qualified_teams)))
    button5.place(x=320, y=490, height=100, width=400)







    #==================Frame 4 code
    from cup import Cup
    def showKnockout(cup):
        currentFrame= tk.Frame(root)
        currentFrame.grid(row=0,column=0,sticky='nsew')
        currentFrame.tkraise()

        entries = []
        for i in range(len(cup.matches)):
            tk.Label(currentFrame, text=f'{cup.matches[i][0]} VS {cup.matches[i][1]}', font='times 25').place(x=200, y=40*(i+4))
            #Enter result
            e = tk.Entry(currentFrame,width=20, font='times 25')
            e.place(x=700, y=40*(i+4),height=50,width=300)
            entries.append(e)
        
        def play():
            results= []
            for i in range(len(cup.matches)):
                result = entries[i].get().split('-')
                results.append(result)
            cup.play(results)
            #show next stage of knockout
            if len(cup.teams) > 1:
                showKnockout(cup)
            else:
                #show winner
                tk.Label(currentFrame, text=f'Winner: {cup.winner()}', font=('times', 48)).place(x=330, y=400)
                button6.config(state='normal')
                button6.config(command=lambda:show_frame(frame5))
            
        #next button
        tk.Button(currentFrame, text='Next', font='times 25', command=play).pack(fill='x', ipady=25,side='bottom')

        #back button
        tk.Button(currentFrame, text='Back', font='times 25', command=lambda:show_frame(frame3)).place(x='20',y='20')


    show_frame(frame1)

    root.mainloop()