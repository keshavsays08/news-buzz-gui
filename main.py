import io
import webbrowser

import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

# # Main Bg Color
color1 = "#FB7318"
# # Main Container Color
# color2 = "#F2F2F2"
# # Button Bg on hover
# color3 = "#cc6e30"


color2 = "#F2F2F2"
color3 = "#cc6e30"
color4 = "BLACK"
color5 = "WHITE"

def open_link(url):
    webbrowser.open(url)


class NewsApp:
    def __init__(self):
        # fetch json data
        self.data = requests.get(
            "https://newsapi.org/v2/top-headlines?country=in&apiKey=885848d8bdce410b848dad31e437699a").json()
        # print(self.data)

        # initialize GUI load
        self.load_gui()

        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(False, False)
        self.root.title("NewsBuzz")


    # this function clears up the news so far for the new news container to load
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index, next_btn=None):
        # clear the screen for the new news item
        self.clear()

        # Logo
        bg_img = PhotoImage(file="bg.png")
        logo_img = PhotoImage(file="logo.png")

        logo_label = Label(self.root, image=logo_img)
        logo_label.pack(anchor="n")

        bg_label = Label(self.root, image=bg_img)
        bg_label.place(x=0,y=150,relwidth=1, relheight=1)

        # Image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_img_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_img_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = "https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg"
            raw_img_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_img_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root, image=photo)
        label.pack()


        # title
        heading = Label(self.root,
                        text=self.data["articles"][index]["title"],
                        bg=color2,
                        fg="black",
                        wraplength=350,
                        justify="center")

        heading.pack(pady=(10, 5))
        heading.config(font=("arial", 15, "bold"))

        # description
        details = Label(self.root,
                        text=self.data["articles"][index]["description"],
                        bg=color2,
                        fg="black",
                        wraplength=350,
                        justify="center")

        details.pack(pady=(5, 5))
        details.config(font=("arial", 12))

        # buttons frame
        main_frame = Frame(self.root, bg="#F2BF88" ,pady=1)
        main_frame.pack(expand=False,fill=X, anchor="s")

        if index > 0:
            prev_btn = Button(
                main_frame,
                text="Prev",
                background=color1,
                foreground=color4,
                activebackground=color3,
                activeforeground=color5,
                highlightthickness=2,
                highlightbackground=color2,
                highlightcolor=color5,
                width=10,
                height=2,
                border=1,
                cursor="hand2",
                font=("Arial", 14, "bold"),
                command=lambda: self.load_news_item(index - 1)
            )
            prev_btn.pack(side=LEFT)
        if index != len(self.data["articles"])-1:
            read_more_btn = Button(
                main_frame,
                text="Read More",
                background=color1,
                foreground=color4,
                activebackground=color3,
                activeforeground=color5,
                highlightthickness=2,
                highlightbackground=color2,
                highlightcolor=color5,
                width=10,
                height=2,
                border=1,
                cursor="hand2",
                font=("Arial", 14, "bold"),
                command=lambda: open_link(self.data["articles"][index]["url"])
            )
            read_more_btn.pack(side=LEFT)
        else:
            read_more_btn = Button(
                main_frame,
                text="Read More",
                background=color1,
                foreground=color4,
                activebackground=color3,
                activeforeground=color5,
                highlightthickness=2,
                highlightbackground=color2,
                highlightcolor=color5,
                width=10,
                height=2,
                border=1,
                cursor="hand2",
                font=("Arial", 14, "bold"),
                command=lambda: open_link(self.data["articles"][index]["url"])
            )
            read_more_btn.pack(side=RIGHT)


        if index != len(self.data["articles"]) - 1:
            next_btn = Button(
                main_frame,
                text="Next",
                background=color1,
                foreground=color4,
                activebackground=color3,
                activeforeground=color5,
                highlightthickness=2,
                highlightbackground=color2,
                highlightcolor=color5,
                width=10,
                height=2,
                border=1,
                cursor="hand2",
                font=("Arial", 14, "bold"),
                command=lambda: self.load_news_item(index + 1)
            )
            next_btn.pack(side=RIGHT)



        # load the gui
        self.root.mainloop()


obj = NewsApp()
