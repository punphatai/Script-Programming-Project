from tkinter import * 
import tkinter.font as font
from PIL import Image,ImageTk
from tkinter import messagebox 
import pygame
import random


def button_click_pic(b, number):
    
    global count, answer_list, answer_dict,whit_image,my_label,score,winner
  
    if b['text'] == ' ' and count < 2: 
        b['image'] = List_of_pic[number]  
        answer_list.append(number)
        answer_dict[b] = List_of_pic[number] 
        count +=1
        print(answer_list)
    if len(answer_list) == 2:
        print(List_of_pic[answer_list[0]])
        print(List_of_pic[answer_list[1]])
        if List_of_pic[answer_list[0]] == List_of_pic[answer_list[1]]:
            
            match_sound()
            
            score += 10
            my_label.config(text='MATCH! SCORE: '+str(score),bg='white',fg='black',font=('Comic sans MS',15,'bold'),relief='solid',bd=3)
          
            for key in answer_dict:        
                key['state'] = 'disable'
                
            count = 0 
            answer_list = [] 
            answer_dict = {}
            
            #when every button match will show winPic(page) that show score
            winner += 1
            print(winner)
            if winner == 12:
                winPic()
            
        else:
            incorrect_sound()
            
            score -= 2 
            if score <= 0:
                score = 0
            my_label.config(text='Incorrect! SCORE: '+str(score),bg='white',fg='black',font=('Comic sans MS',15,'bold'),relief='solid',bd=3)            
            
            #this is problem of program 
            messagebox.showerror('Incorrect','Not Match!!!')

            for key in answer_dict:
                key['image'] = whit_image
                
            count = 0
            answer_list = []
            answer_dict = {}
   
def button_click_num(b, number):
   
    global count, answer_list, answer_dict,whit_image,my_label,score,winner
    
    if b['text'] == ' ' and count < 2: 
        b['image'] = matches[number]  
        answer_list.append(number)
        answer_dict[b] = matches[number] 
        count +=1
        print(answer_list)
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            #play sound when answers are match
            match_sound()
        
            score += 10
            my_label.config(text='MATCH! SCORE: '+str(score),bg='white',fg='black',font=('Comic sans MS',15,'bold'),relief='solid',bd=3)
            for key in answer_dict:        
                key['state'] = 'disable'
                
            count = 0 
            answer_list = [] 
            answer_dict = {}
            winner += 1 
            if winner == 12 :
               winNum()
            
        else:
            incorrect_sound()
            score -= 2 
            if score <= 0:
                score = 0
            my_label.config(text='Incorrect! SCORE: '+str(score),bg='white',fg='black',font=('Comic sans MS',15,'bold'),relief='solid',bd=3)
            messagebox.showerror('Incorrect','Not Match!!!')

            for key in answer_dict:
                key['image'] = whit_image
                
            count = 0
            answer_list = []
            answer_dict = {}

# this function will reset Page game play of pciture
def ResetGamePagePic():
    global w 
    w.withdraw()
    #this function will regenerate and create new window of page_player_pic 
    page_player_pic()

# this function will reset Page game play of number
def ResetGamePageNum():
    global w 
    w.withdraw()
    #this function will regenerate and create new window of page_player_num 
    page_player_number()        

#it's work when all pictures are match
def winPic():
    #global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b18,b19,b20,b21,b22,b23  
    global score
    global whit_image,my_label,bg_no_font,winner,score,w
    ppy.withdraw()
    w = Toplevel(ppy)
    w.geometry("960x540+400+200")
    w.iconbitmap(r'icon_gui.ico')
    w.resizable(False,False)
    
    background_label = Label(w, image = bg_no_font)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    Label(w, text = 'You winn\nYou score is : ' + str(score),fg='black',bg='white',relief='solid',font=('Comic sans MS',20,'bold'),bd=3).place(x = 340,y=100)
    #reset score and count of math(count of winner time when element is math)
    score = 0
    winner = 0
    r = Button(w,text ='Reset',borderwidth=0,cursor="hand2",command = ResetGamePagePic).pack(pady= 20)

#it's work when all pictures are match   
def winNum():
    #global b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b18,b19,b20,b21,b22,b23  
    global score
    global whit_image,my_label,bg_no_font,winner,score,w
    ppy.withdraw()
    w = Toplevel(ppy)
    w.geometry("960x540+400+200")
    w.iconbitmap(r'icon_gui.ico')
    w.resizable(False,False)
    
    background_label = Label(w, image = bg_no_font)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(w, text = 'You winn\nYou score is : ' + str(score),fg='black',bg='white',relief='solid',font=('Comic sans MS',20,'bold'),bd=3).place(x = 340,y=100)
    #reset score and count of match(count of winner time when element is match)
    score = 0
    winner = 0
    r = Button(w,text ='Reset',borderwidth=0,cursor="hand2",command = ResetGamePageNum).pack(pady= 20)
    
def page_player_pic():
    global ppy,whit_image,my_label
    top.withdraw()
    ppy = Toplevel(top)
    ppy.geometry("960x540+400+200")
    ppy.iconbitmap(r'icon_gui.ico')
    ppy.resizable(False,False)
    ppy.config(bg='#ffd09e')
     
    my_frame = Frame(ppy)
    my_frame.pack(pady=10)
    
    b0 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b0, 0))
    b0.bind('<Button-1>',Game_click_sound)
    b1 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b1, 1))
    b1.bind('<Button-1>',Game_click_sound)
    b2 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b2, 2))
    b2.bind('<Button-1>',Game_click_sound)
    b3 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b3, 3))
    b3.bind('<Button-1>',Game_click_sound)
    b4 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b4, 4))
    b4.bind('<Button-1>',Game_click_sound)
    b5 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b5, 5))
    b5.bind('<Button-1>',Game_click_sound)
    b6 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b6, 6))
    b6.bind('<Button-1>',Game_click_sound)
    b7 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b7, 7))
    b7.bind('<Button-1>',Game_click_sound)
    b8 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b8, 8))
    b8.bind('<Button-1>',Game_click_sound)
    b9 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b9, 9))
    b9.bind('<Button-1>',Game_click_sound)
    b10 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b10, 10))
    b10.bind('<Button-1>',Game_click_sound)
    b11 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b11, 11))
    b11.bind('<Button-1>',Game_click_sound)
    b12 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b12, 12))
    b12.bind('<Button-1>',Game_click_sound)
    b13 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b13, 13))
    b13.bind('<Button-1>',Game_click_sound)
    b14 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b14, 14))
    b14.bind('<Button-1>',Game_click_sound)
    b15 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b15, 15))
    b15.bind('<Button-1>',Game_click_sound)
    b16 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b16, 16))
    b16.bind('<Button-1>',Game_click_sound)
    b17 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b17, 17))
    b17.bind('<Button-1>',Game_click_sound)
    b18 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b18, 18))
    b18.bind('<Button-1>',Game_click_sound)
    b19 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b19, 19))
    b19.bind('<Button-1>',Game_click_sound)
    b20 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b20, 20))
    b20.bind('<Button-1>',Game_click_sound)
    b21 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b21, 21))
    b21.bind('<Button-1>',Game_click_sound)
    b22 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b22, 22))
    b22.bind('<Button-1>',Game_click_sound)
    b23 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_pic(b23, 23))
    b23.bind('<Button-1>',Game_click_sound)
    
    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=0,column=4)
    b5.grid(row=0,column=5)
    
    b6.grid(row=1,column=0)
    b7.grid(row=1,column=1)
    b8.grid(row=1,column=2)
    b9.grid(row=1,column=3)
    b10.grid(row=1,column=4)
    b11.grid(row=1,column=5)
    
    b12.grid(row=2,column=0)
    b13.grid(row=2,column=1)
    b14.grid(row=2,column=2)
    b15.grid(row=2,column=3)
    b16.grid(row=2,column=4)
    b17.grid(row=2,column=5)
    
    b18.grid(row=3,column=0)
    b19.grid(row=3,column=1)
    b20.grid(row=3,column=2)
    b21.grid(row=3,column=3)
    b22.grid(row=3,column=4)
    b23.grid(row=3,column=5)
     
    my_label = Label(ppy, text ="")
    my_label.place(x=380,y=480)
   
    btn_back = Button(ppy,image=bt_back,borderwidth=0,cursor="hand2",command=pagePlayYerBack)
    btn_back.bind('<Button-1>',Menu_click_sound)
    btn_back.place(x=10,y=460)
    
    random.shuffle(List_of_pic)
    ppy.protocol('WM_DELETE_WINDOW',close)
 
def page_player_number():
    global ppy,whit_image,my_label
    top.withdraw()
    ppy = Toplevel(top)
    ppy.geometry("960x540+400+200")
    ppy.iconbitmap(r'icon_gui.ico')
    ppy.resizable(False,False)
    ppy.config(bg='#ffd09e')
        
    my_frame = Frame(ppy)
    my_frame.pack(pady=10)
    
    b0 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b0, 0))
    b0.bind('<Button-1>',Game_click_sound)
    b1 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b1, 1))
    b1.bind('<Button-1>',Game_click_sound)
    b2 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b2, 2))
    b2.bind('<Button-1>',Game_click_sound)
    b3 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b3, 3))
    b3.bind('<Button-1>',Game_click_sound)
    b4 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b4, 4))
    b4.bind('<Button-1>',Game_click_sound)
    b5 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b5, 5))
    b5.bind('<Button-1>',Game_click_sound)
    b6 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b6, 6))
    b6.bind('<Button-1>',Game_click_sound)
    b7 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b7, 7))
    b7.bind('<Button-1>',Game_click_sound)
    b8 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b8, 8))
    b8.bind('<Button-1>',Game_click_sound)
    b9 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b9, 9))
    b9.bind('<Button-1>',Game_click_sound)
    b10 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b10, 10))
    b10.bind('<Button-1>',Game_click_sound)
    b11 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b11, 11))
    b11.bind('<Button-1>',Game_click_sound)
    b12 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b12, 12))
    b12.bind('<Button-1>',Game_click_sound)
    b13 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b13, 13))
    b13.bind('<Button-1>',Game_click_sound)
    b14 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b14, 14))
    b14.bind('<Button-1>',Game_click_sound)
    b15 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b15, 15))
    b15.bind('<Button-1>',Game_click_sound)
    b16 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b16, 16))
    b16.bind('<Button-1>',Game_click_sound)
    b17 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b17, 17))
    b17.bind('<Button-1>',Game_click_sound)
    b18 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b18, 18))
    b18.bind('<Button-1>',Game_click_sound)
    b19 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b19, 19))
    b19.bind('<Button-1>',Game_click_sound)
    b20 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b20, 20))
    b20.bind('<Button-1>',Game_click_sound)
    b21 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b21, 21))
    b21.bind('<Button-1>',Game_click_sound)
    b22 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b22, 22))
    b22.bind('<Button-1>',Game_click_sound)
    b23 = Button(my_frame,text = ' ',image = whit_image,relief='flat',bd=2,command = lambda: button_click_num(b23, 23))
    b23.bind('<Button-1>',Game_click_sound)
    
    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=0,column=4)
    b5.grid(row=0,column=5)
    
    b6.grid(row=1,column=0)
    b7.grid(row=1,column=1)
    b8.grid(row=1,column=2)
    b9.grid(row=1,column=3)
    b10.grid(row=1,column=4)
    b11.grid(row=1,column=5)
    
    b12.grid(row=2,column=0)
    b13.grid(row=2,column=1)
    b14.grid(row=2,column=2)
    b15.grid(row=2,column=3)
    b16.grid(row=2,column=4)
    b17.grid(row=2,column=5)
    
    b18.grid(row=3,column=0)
    b19.grid(row=3,column=1)
    b20.grid(row=3,column=2)
    b21.grid(row=3,column=3)
    b22.grid(row=3,column=4)
    b23.grid(row=3,column=5)
    
    my_label = Label(ppy, text ="")
    my_label.place(x=380,y=480)
    
    btn_back = Button(ppy,image=bt_back,borderwidth=0,cursor="hand2",command=pagePlayYerBack)
    btn_back.bind('<Button-1>',Menu_click_sound)
    btn_back.place(x=10,y=460)
   
    random.shuffle(matches)
    ppy.protocol('WM_DELETE_WINDOW',close)

def pagePlayYerBack():
    global ppy,score,winner
    score  = 0
    winner = 0
    ppy.withdraw()
    top.deiconify()

def pagePlayer():
    global top
    root.withdraw()
    top = Toplevel(root)
    top.geometry("960x540+400+200")
    top.iconbitmap(r'icon_gui.ico')
    top.resizable(False,False)
    
    background_label = Label(top, image = bg_play)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    btn_playPic = Button(top,image=bt_Ppic,borderwidth=0,cursor="hand2",command=page_player_pic)
    btn_playPic.bind('<Button-1>',Menu_click_sound)
    btn_playPic.place(x=290,y=280)
    
    btn_playNum = Button(top,image=bt_Pnum,borderwidth=0,cursor="hand2",command=page_player_number)
    btn_playNum.bind('<Button-1>',Menu_click_sound)
    btn_playNum.place(x=500,y=280)
    
    btn_back = Button(top,image=bt_back,borderwidth=0,cursor="hand2",command=pageHome)
    btn_back.bind('<Button-1>',Menu_click_sound)
    btn_back.place(x=10,y=460)
    
    top.protocol('WM_DELETE_WINDOW',close)

def pageHome(): 
    global top
    top.withdraw()
    root.deiconify()
     
def pageCredits():
    global top
    root.withdraw()
    
    top = Toplevel(root)
    top.geometry("960x540+400+200")
    top.iconbitmap(r'icon_gui.ico')
    top.resizable(False,False)
    
    background_label = Label(top, image = bg_credit)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    btn_back = Button(top,image=bt_back,borderwidth=0,cursor="hand2",command=pageHome)
    btn_back.bind('<Button-1>',Menu_click_sound)
    btn_back.place(x=10,y=460)
    
    top.protocol('WM_DELETE_WINDOW',close)
    
def pageSetting():
    
    global top
    root.withdraw()
    top = Toplevel(root)
    top.geometry("960x540+400+200")
    top.iconbitmap(r'icon_gui.ico')
    top.resizable(False,False)
    
    background_label = Label(top, image = bg_setting)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(top,text=" SONG NAME :  C148-SWEDEN-MINECRAFT ",bg='#ffffff',font=('Comic sans MS',15,'bold')).place(x=240,y=195)
    
    scale = Scale(top,label="Volume",font=('Comic sans MS',15,'bold'),from_=0,to=100,length=500,orient=HORIZONTAL,command=set_volume,bg='#fedc00',troughcolor='#ffffff',relief=FLAT,bd=2)
    scale.set(50)
    scale.place(x=240,y=240)
    
    btn_on = Button(top,image=bt_on,borderwidth=0,cursor="hand2",command=play_song)
    btn_on.bind('<Button-1>',Menu_click_sound)
    btn_on.place(x=290,y=350)
    
    btn_off = Button(top,image=bt_off,borderwidth=0,cursor="hand2",command=stop_song)
    btn_off.bind('<Button-1>',Menu_click_sound)
    btn_off.place(x=500,y=350)
    
    btn_back = Button(top,image=bt_back,borderwidth=0,cursor="hand2",command=pageHome)
    btn_back.bind('<Button-1>',Menu_click_sound)
    btn_back.place(x=10,y=460)

    top.protocol('WM_DELETE_WINDOW',close)
    
def choice(option):
    pop.destroy()
    if option == 'yes':
        pygame.mixer.music.stop()
        root.destroy()
    else:
        pass

def ExitButtom():
    global pop 
    pop = Toplevel(root)
    pop.title('EXIT')
    pop.geometry('250x150+420+220')
    pop.iconbitmap(r'icon_gui.ico')
    pop.resizable(False,False)
    pop.config(bg='#ffd09e')
    
    pop_label = Label(pop,text='Do you want exit?',bg='#ffd09e',fg='#000000',font=('Comic sans MS',20,'bold'))
    pop_label.pack(pady=10)

    myframe = Frame(pop,bg='#ffd09e')
    myframe.pack(pady=5)  
    
    yes = Button(myframe,image=bt_Yes,borderwidth=0,cursor="hand2",bg='#ffd09e',command=lambda:choice('yes'))
    yes.bind('<Button-1>',Menu_click_sound)
    yes.pack(side=LEFT,padx = 20)
  
    no = Button(myframe,image=bt_No,borderwidth=0,cursor="hand2",bg='#ffd09e',command=lambda:choice('no'))
    no.bind('<Button-1>',Menu_click_sound)
    no.pack(side=RIGHT,padx=20)

def close(): 
    pygame.mixer.music.stop()
    root.destroy()

def match_sound():
    math_sound = pygame.mixer.Sound("gruu.mp3")
    math_sound.set_volume(0.3)
    math_sound.play()

def incorrect_sound():
    incorrect_sound = pygame.mixer.Sound("bruh.mp3")
    incorrect_sound.set_volume(0.3)
    incorrect_sound.play() 
def play_song():
    pygame.mixer.music.load("C418_Sweden.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop_song():
    pygame.mixer.music.stop()
    
def set_volume(val): 
    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)
    
def Menu_click_sound(event):
    math_sound = pygame.mixer.Sound("couin.mp3")
    math_sound.set_volume(1)
    math_sound.play()
    
def Game_click_sound(event):
    math_sound = pygame.mixer.Sound("adriantnt_glass.mp3")
    math_sound.set_volume(1)
    math_sound.play()
    
root = Tk()

root.geometry('960x540+400+200')
root.title('MATCHING GAME')
root.iconbitmap(r'icon_gui.ico')
root.resizable(False,False)

bg_play = PhotoImage(file = "page_mode.png")
bg_setting = PhotoImage(file = "Setting_page.png")
bg_credit = PhotoImage(file = "Credits_page.png")
bg_no_font = PhotoImage(file = "background_noFont.png")


bt_Yes = PhotoImage(file = "bt_Yes2.png")
bt_No = PhotoImage(file = "bt_No2.png")
bt_back = PhotoImage(file = "bt_back.png")
bt_on = PhotoImage(file = "pic_turnOn.png")
bt_off = PhotoImage(file = "pic_turnOff.png")
bt_Ppic = PhotoImage(file = "bt_pics.png")
bt_Pnum = PhotoImage(file = "bt_nums.png")
pic_play = ImageTk.PhotoImage(Image.open("bt_play.png"))
pic_credit = ImageTk.PhotoImage(Image.open("bt_credits.png"))
pic_setting = ImageTk.PhotoImage(Image.open("bt_setting.png"))
pic_exit = ImageTk.PhotoImage(Image.open("bt_exit.png"))
whit_image = ImageTk.PhotoImage(Image.open ("bk_photo2.png").resize((90,110)))
bg = PhotoImage(file = "bg4.png")

background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

pic1 = ImageTk.PhotoImage(Image.open ("1.png").resize((90,110)))
pic2 = ImageTk.PhotoImage(Image.open ("2.png").resize((90,110)))
pic3 = ImageTk.PhotoImage(Image.open ("3.png").resize((90,110)))
pic4 = ImageTk.PhotoImage(Image.open ("4.png").resize((90,110)))
pic5 = ImageTk.PhotoImage(Image.open ("5.png").resize((90,110)))
pic6 = ImageTk.PhotoImage(Image.open ("6.png").resize((90,110)))
pic7 = ImageTk.PhotoImage(Image.open ("7.png").resize((90,110)))
pic8 = ImageTk.PhotoImage(Image.open ("8.png").resize((90,110)))
pic9 = ImageTk.PhotoImage(Image.open ("9.png").resize((90,110)))
pic10 = ImageTk.PhotoImage(Image.open ("10.png").resize((90,110)))
pic11 = ImageTk.PhotoImage(Image.open ("11.png").resize((90,110)))
pic12 = ImageTk.PhotoImage(Image.open ("12.png").resize((90,110)))

num1 = ImageTk.PhotoImage(Image.open ("1n.png").resize((90,110)))
num2 = ImageTk.PhotoImage(Image.open ("2n.png").resize((90,110)))
num3 = ImageTk.PhotoImage(Image.open ("3n.png").resize((90,110)))
num4 = ImageTk.PhotoImage(Image.open ("4n.png").resize((90,110)))
num5 = ImageTk.PhotoImage(Image.open ("5n.png").resize((90,110)))
num6 = ImageTk.PhotoImage(Image.open ("6n.png").resize((90,110)))
num7 = ImageTk.PhotoImage(Image.open ("7n.png").resize((90,110)))
num8 = ImageTk.PhotoImage(Image.open ("8n.png").resize((90,110)))
num9 = ImageTk.PhotoImage(Image.open ("9n.png").resize((90,110)))
num10 = ImageTk.PhotoImage(Image.open ("10n.png").resize((90,110)))
num11 = ImageTk.PhotoImage(Image.open ("11n.png").resize((90,110)))
num12 = ImageTk.PhotoImage(Image.open ("12n.png").resize((90,110)))

List_of_pic = [pic1,pic1,pic2,pic2,pic3,pic3,pic4,pic4,pic5,pic5,pic6,pic6,pic7,pic7,pic8,pic8,pic9,pic9,pic10,pic10,pic11,pic11,pic12,pic12]
random.shuffle(List_of_pic)

matches = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12]
random.shuffle(matches)

score = 0

winner = 0
count = 0
answer_list = []
answer_dict = {}

#play music
pygame.mixer.init()
#pygame.mixer.music.load("C418_Sweden.mp3")
#pygame.mixer.music.play(loops=-1)

btn1 = Button(root,image=pic_play,borderwidth=0,cursor="hand2",command=pagePlayer)
btn1.bind('<Button-1>',Menu_click_sound)
btn1.place(x=383,y=215)

btn2 = Button(root,image=pic_credit,borderwidth=0,cursor="hand2",command=pageCredits)
btn2.bind('<Button-1>',Menu_click_sound)
btn2.place(x=383,y=290)

btn3 = Button(root,image=pic_setting,borderwidth=0,cursor="hand2",command=pageSetting)
btn3.bind('<Button-1>',Menu_click_sound)
btn3.place(x=383,y=365)

btn4 = Button(root,image=pic_exit,borderwidth=0,cursor="hand2",command=ExitButtom)
btn4.bind('<Button-1>',Menu_click_sound)
btn4.place(x=383,y=440)

root.protocol('WM_DELETE_WINDOW',close)
root.mainloop()