from tkinter import *
from tkinter import ttk
from ctypes import windll
import pyperclip


class DisappearingTextWriting:
    def __init__(self, root):
        self.TIME = 300
        self.TIME_WRITING = 6
        self.timer = NONE
        self.time_writing = self.TIME_WRITING
        self.time = self.TIME
        self.FAMILY = 'Microsoft YaHei UI'


        root.title("Diesappearing Text Writing")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky="nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.geometry('1843x1036+250+120')

        self.inputted_words = StringVar()
        self.words_entry = ttk.Entry(mainframe, width=25, textvariable=self.inputted_words, justify="center")
        self.words_entry.grid(column=2, row=3)
        self.words_entry.configure(font=(self.FAMILY, 24, "normal"))


        self.time_display = StringVar()
        self.time_display.set(self.time_calculation())
        timer_label = ttk.Label(mainframe, textvariable=self.time_display, font=(self.FAMILY, 60, "normal"))
        timer_label.grid(column=1, row=1)

        words_label = ttk.Label(mainframe, textvariable=self.inputted_words,
                                wraplength=900, borderwidth=5, background="grey", anchor="center", width=50)
        words_label.grid(column=2, row=1, rowspan=2, sticky="ew")
        words_label.configure(font=(self.FAMILY, 24, "normal"))

        copy_button = ttk.Button(mainframe, text="Copy", command=self.copy_word)
        copy_button.grid(column=3, row=2, sticky=W)

        start_button = ttk.Button(mainframe, text="Start", command=lambda: [self.count_down(),
                                                                            self.count_down_writing(),
                                                                            self.reset_parameter()])
        start_button.grid(column=3, row=3, sticky=W)



        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Key>", self.reset_writing_time)

        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=1)
        mainframe.columnconfigure(3, weight=1)
        mainframe.rowconfigure(1, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.rowconfigure(3, weight=1)

        s = ttk.Style()
        s.configure('.', font=('Helvetica', 20))




    def count_down(self):
        if self.time > -1:
            self.time_display.set(self.time_calculation())
            self.time -= 1
            self.timer = root.after(1000, self.count_down)
        else: #count_down finish
            self.words_entry.config(state="disabled")
            self.time = self.TIME
            root.after_cancel(self.timer)
            root.after_cancel(self.writing_timer)
            self.time_display.set(self.time_calculation())



    def count_down_writing(self):
        if self.time_writing > 1:
            self.time_writing -= 1
            self.writing_timer = root.after(1000, self.count_down_writing)
            print(self.time_writing)
        else:
            self.inputted_words.set("")
            self.time_display.set(self.time_calculation())
            root.after_cancel(self.timer)

    def reset_writing_time(self, *args):
        self.time_writing = 5

    def copy_word(self):
        pyperclip.copy(self.inputted_words.get())
        self.inputted_words.set("")


    def reset_parameter(self):
        self.words_entry.config(state="normal")
        self.inputted_words.set("")
        self.timer = NONE
        self.writing_timer = NONE
        self.time_writing = self.TIME_WRITING
        self.time = self.TIME

    def time_calculation(self):
        minute, second = (self.time//60, self.time % 60)
        if minute < 10:
            minute_display = f"0{minute}"
        else:
            minute_display = minute
        if second < 10:
            second_display = f"0{second}"
        else:
            second_display = second
        display = f"{minute_display}:{second_display}"
        return display











root = Tk()
windll.shcore.SetProcessDpiAwareness(1)
DisappearingTextWriting(root)
root.mainloop()
