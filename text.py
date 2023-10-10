# -*- coding: utf-8 -*-
import tkinter as tk
import pygame
from PIL import Image, ImageTk
from tkinter import Toplevel

i = 0
n = 30
select = None

class App(tk.Tk):
    # 呪文
    def __init__(self, *args, **kwargs):
        # 呪文
        tk.Tk.__init__(self, *args, **kwargs)
        
        pygame.mixer.init()
        
        # ウィンドウタイトルを決定
        self.title("Tkinter change page")

        # ウィンドウの大きさを決定
        self.geometry("800x600")
        
        # ウィンドウのグリッドを 1x1 にする
        # この処理をコメントアウトすると配置がズレる
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
#-----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        def changePage():
            self.changePage(self.frame1)
            pygame.mixer.music.load("GutenMorgen.mp3")
            pygame.mixer.music.play()
            
        def confirm():
            global select
            name = self.entryname.get()
            self.entryname.delete(0, 'end')
            print(select)
            self.titleLabel.config( text = "Willkommen " + name)
            with open("game.txt", "w") as file:
                file.write(name)
                
            self.titleLabel1.config(text= "Guten Morgen " + name)
            self.changePageButton.config(state='normal')              #ä
            #pygame.mixer.init()
            
        def language():
            select = self.radio.get()
            if select == 'j':
                self.changePageButton.config(text='  プレイ  ')
                self.confirm.config(text=' 名前を入力  ')
                self.titleLabel.config(text='究極のStevanQuiz!')
            
        
        # Datei "game.txt" im Lesemodus öffnen
        with open("game.txt", "r") as file:
            name = file.read()
            
            
        # タイトルラベル作成
        self.titleLabel = tk.Label(self.main_frame, text="Das ultimative StevanQuiz", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center')
        # フレーム1に移動するボタン
        self.changePageButton = tk.Button(self.main_frame, text="Play Game", command=changePage , font=('Helvetica',50))
        self.changePageButton.config(state='disabled')                       #ä
        self.changePageButton.place(x=200,y=200)
        self.entryname = tk.Entry(self.main_frame, text="Gib dein Namen ein", font=("Arial",32))
        self.entryname.place(x=150,y=380)
        self.confirm = tk.Button(self.main_frame, text="Name Bestätigen", command = confirm, font=('Helvetica',26))
        self.confirm.place(x=250,y=460)
        
        #language
        self.radio = tk.StringVar()
        
        self.c1 = tk.Radiobutton(self.main_frame, text='DE', variable=self.radio, value='d', command=language)
        self.c1.pack()
        self.c2 = tk.Radiobutton(self.main_frame, text='JP', variable=self.radio, value='j', command=language)
        self.c2.pack()
        
#--------------------------------------------------------------------------
#-----------------------------------frame1---------------------------------
        # 移動先フレーム作成
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        
        def machen():
            neutext()
            mp3()
        
        def neutext():
            global i
            if i < 10:
                w = ["Ich bin Stevan. Ich hoffe", "du hattest einen schönen Tag.", "übrigens,","hast du schon die Hausaufgaben","für Deutsch und PW gemacht?","...","Zeit für ein Quiz!","ich nenne es","StevanQuiz!", "Was bedeutet Wupsas?"]
                self.titleLabel1.config(text=w[i])
                i += 1
            else:
                self.quiz1.config(text="A) Rucksack       ", state = 'normal', width=15)
                self.quiz2.config(text="B) Wupsas       ", state = 'normal', width=15)
                self.quiz3.config(text="C) panapana     ", state = 'normal', width=15)
                
        def mp3():
            global i
            #pygame.mixer.init()
            
            if i == 1:
                pygame.mixer.music.load(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\Neue Aufnahme 12 (online-audio-converter.com).mp3")
                pygame.mixer.music.play()
            
            elif i == 9:
                pygame.mixer.music.load(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\StevanQuiz.mp3")
                pygame.mixer.music.play()
                
        
        def quiz1():
            self.titleLabel1.config(text="Richtig")
            self.changePageButton1.config(state = 'normal')
            self.quiz2.config(state='disabled')
            self.quiz3.config(state='disabled')
            self.button.config(state='disabled')
            pygame.mixer.music.load(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\Richtig.mp3")
            pygame.mixer.music.play()
            
        def quiz2():
            self.titleLabel1.config(text="Falsch")
            self.quiz1.config(state='disabled')
            self.button.config(state='disabled')
            pygame.mixer.music.load(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\Falsch.mp3")
            pygame.mixer.music.play()
            
        def quiz3():
            self.titleLabel1.config(text="Falsch")
            self.quiz1.config(state='disabled')
            self.button.config(state='disabled')
            pygame.mixer.music.load(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\Falsch.mp3")
            pygame.mixer.music.play()
            
        # タイトルラベル作成
        self.titleLabel1 = tk.Label(self.frame1, text="Guten Morgen " + name + ".", font=('Helvetica', '35'))
        self.titleLabel1.pack()
        
        self.image = tk.PhotoImage(file=r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\stevangame.png")
        self.label = tk.Label(self.frame1, image = self.image)
        self.label.place(x=100,y=80)
        
        # フレーム1から他のフレームに戻るボタン
        self.back_button = tk.Button(self.frame1, text="Home" , command=lambda : self.changePage(self.main_frame), font=('Helvetica',24))
        self.back_button.place(x=20,y=500)
        self.changePageButton1 = tk.Button(self.frame1, text="Weiter", command=lambda : self.changePage(self.frame2), font=('Helvetica',26))
        self.changePageButton1.config(state = 'disabled')                        #ä
        self.changePageButton1.place(x=600,y=500)
        self.button = tk.Button(self.frame1, text="Interaktion", command = machen, font=('Helvetica',26), width=10)
        self.button.place(x=300,y=350)
        
        self.quiz1 = tk.Button(self.frame1, text = "              ", command = quiz1, font=('Helvetica', 24), width=15)
        self.quiz1.config(state='disabled')
        self.quiz1.place(x=350,y=80)
        self.quiz2 = tk.Button(self.frame1, text = "              ", command = quiz2,  font=('Helvetica', 24), width=15)
        self.quiz2.config(state='disabled')
        self.quiz2.place(x=350,y=160)
        self.quiz3 = tk.Button(self.frame1, text = "              ", command = quiz3,  font=('Helvetica', 24), width=15)
        self.quiz3.config(state='disabled')
        self.quiz3.place(x=350,y=240)
#--------------------------------------------------------------------------
        self.frame2 = tk.Frame()
        self.frame2.grid(row=0, column=0, sticky="nsew")
        
        def move():
            # Aktualisiere die Position des Fensters
            x, y = self.frame2.winfo_x(), self.frame2.winfo_y()
            self.frame2.geometry(f"400x200+{x+5}+{y+5}")  # Ändere die Position um 5 Pixel nach rechts und unten
            new_window.after(10, move)  # Warte 100 Millisekunden und rufe die Funktion erneut auf
        
        def aufgeben():
             self.changePage(self.main_frame)
             self.frame2.destroy()
             self.frame1.destroy()
             #self.main_frame.destroy()
             
        def bild():        
            new_window = Toplevel()  # Neues Fenster erstellen
            new_window.title("Neues Fenster")  # Titel setzen
            
            
            # Setze die Position des neuen Fensters
            x_position = 500
            y_position = 500
            new_window.geometry(f"+{x_position}+{y_position}")
            
            pygame.mixer.music.load("rappa.mp3")
            pygame.mixer.music.play()

            self.image2 = tk.PhotoImage(file=r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\GameHaruki\_20230110_175739.png")
            self.label = tk.Label(new_window, image = self.image2)
            self.label.pack()
            
            
       
        def click():
            global n
            if n > -1:
                self.counterbutton.config(text = n)
                n -= 1
                print(n)
                
            elif n == -1:
                self.titleLabel2.config(text="Herzlichen Glückwunsch")
                self.back_button2.config(text="Home")
                self.counterbutton.config(text="> o <")
                bild()
                n -= 1
            
        
        self.titleLabel2 = tk.Label(self.frame2, text=" ", font=('Helvetica','23'))
        self.titleLabel2.pack(anchor='center')
        
        self.back_button2 = tk.Button(self.frame2, text="Aufgeben", command=aufgeben, font=('Helvetica', '35'), width = 9)
        self.back_button2.place(x=270,y=500)
        
        #無限ボタンクリック
        
        self.counterbutton = tk.Button(self.frame2, text="°0°", command = click, font=('Helvetica', '35'), width = 9)
        self.counterbutton.place(x=270,y=250)
    

        #main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, page):
        page.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()

