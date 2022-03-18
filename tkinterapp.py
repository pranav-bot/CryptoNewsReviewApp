from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import *
from turtle import position
from main1 import *
from GraphPred import *
def New_Window():
    News_Window_Screen = Tk()
    News_Window_Screen.title("News")
    Screen_Title=Label(News_Window_Screen,text='News Tab', font=("Times","30", "bold"))
    Screen_Title.pack()
    coin_input_title=Label(News_Window_Screen, text='Enter Coin Name', font=("Times","15"))
    coin_input_title.pack()
    coin_input_frame = Frame(News_Window_Screen)
    coin_input_frame.pack_propagate(False)
    coin_input_frame.pack(expand=True)
    coin_input = Entry(News_Window_Screen, width=30)
    coin_input.place(x=220, y=100)
    coin_input.pack()
    ans=str(coin_input)

    canvas = tk.Canvas(News_Window_Screen, height=HEIGHT, width=WIDTH)
    canvas.pack()
    enter_button = tk.Button(News_Window_Screen, text='Enter', bg='White', fg='Black',
                             command=lambda: AnotherWindow())
    enter_button.pack
    enter_button.place(x=100, y=100)
    ArticleReview(ans)
    def AnotherWindow():
        content = ans
        text_box = Text(
            News_Window_Screen,
            height=12,
            width=40
        )
        text_box.pack(expand=True)
        text_box.insert('end', content)
        text_box.config(state='disabled')
        text_box.place(x=180, y=180)
        canvas = tk.Canvas(News_Window_Screen, height=HEIGHT, width=WIDTH)
        canvas.pack()


def Graph_Window():
    Graph_Window_Screen = Tk()
    Graph_Window_Screen.title("Graph")
    Screen_Title = Label(Graph_Window_Screen, text='Graph Tab', font=("Times", "30", "bold"))
    Screen_Title.pack()
    coin_input_title = Label(Graph_Window_Screen, text="Enter the coin u wish to see(format ETC-USD)", font=("Times", "15"))
    coin_input_title.pack()
    coin_input_frame = Frame(Graph_Window_Screen)
    coin_input_frame.pack_propagate(False)
    coin_input_frame.pack(expand=True)
    coin_input = Entry(Graph_Window_Screen, width=30)
    trash=str(coin_input)
    coin_input.place(x=220, y=100)
    coin_input.pack()
    canvas = tk.Canvas(Graph_Window_Screen, height=HEIGHT, width=WIDTH)
    canvas.pack()
    enter_button = tk.Button(Graph_Window_Screen, text='Enter', bg='White', fg='Black', command=lambda: graph(trash))
    enter_button.pack
    enter_button.place(x=100, y=100)

HEIGHT = 640
WIDTH = 360

ws = tk.Tk()
ws.title("Cryptop")
lbl =Label(ws,text='ok',font=("Times","100","bold")).place(x=100, y=100)
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()

news_button = tk.Button(ws, text="News",padx=10,pady=10, bg='White', fg='Black',
                              command=lambda: New_Window())
graph_button=tk.Button(ws, text="Prediction", bg='White', fg='Black', command=lambda:Graph_Window())
news_button.place(x=180, y=180)
graph_button.place(x=100, y=100)
ws.mainloop()