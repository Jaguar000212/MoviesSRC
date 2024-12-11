import customtkinter as ctk
from tkinter import messagebox
from imdb import Cinemagoer


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.results = None
        self.entry = None
        self.title("MoviesSRC")
        self.geometry("800x600")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")
        ctk.set_widget_scaling(1.5)
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Enter the name of the movie").pack(pady=20)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=20)

        ctk.CTkButton(self, text="Search", command=self.search_movie).pack(pady=20)

    def search_movie(self):
        cinemagoer = Cinemagoer()
        self.results = cinemagoer.search_movie(self.entry.get())
        optionmenu = ctk.CTkOptionMenu(self, values=[x.title for x in self.results], command=self.get_url)
        optionmenu.pack(pady=20)

    def get_url(self, value):
        id = value.getID()
        url = f"https://vidsrc.xyz/embed/tv/tt{id}"
        messagebox.showinfo("URL", url)
