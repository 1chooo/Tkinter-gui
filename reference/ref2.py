import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class BaseDesk:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('回歸')
        self.root.geometry('800x600')

        InitialFrame(self.root)


class InitialFrame:
    def __init__(self, master):
        self.root = master
        self.root.config(bg="#98AFC7")  # Blue Gray

        # 基準界面 InitialFrame
        self.initial_frame = tk.Frame(self.root, bg="#BCC6CC")  # Metallic Silver
        self.initial_frame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.95)

        self.canvas = Canvas(self.initial_frame, width=350)
        self.canvas.pack(side=TOP, anchor=NW, padx=10, pady=10)

        self.img = Image.open('../assets/imgs/Login.jpg')
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(30, 30, anchor="center", image=self.tk_img)

        self.btn = tk.Button(self.initial_frame, text="開始", command=self.change)
        self.canvas.create_window(100, 100, anchor="center", window=self.btn)
        #self.btn.pack()

    def change(self):
        self.initial_frame.destroy()  # 刪除 InitialFrame
        FrameMenu(self.root)


class FrameMenu:
    def __init__(self, master):

        # saury, sardine, squid's frame initialize
        self.saury_menu = None
        self.sardine_menu = None
        self.squid_menu = None

        # saury, sardine, squid's frame 存在與否
        self.saury_frame_exit = False
        self.sardine_frame_exit = False
        self.squid_frame_exit = False

        # root 背景設定
        self.root = master
        self.root.config(bg="#98AFC7")  # Blue Gray
        # self.root.iconbitmap()

        # frame_menu 背景設定
        self.frame_menu = tk.Frame(self.root)  # 在 root 上建 FrameMenu
        self.frame_menu.config(bg="#737CA1")  # Slate Blue Grey
        self.frame_menu.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.25)

        # frame_menu 上的物件設定
        saury_btn = tk.Button(self.frame_menu, text='秋刀魚', command=self.saury_new_window,
                              font=('Arial', 18, 'bold'), bg="white", fg='black')  # Slate Blue Grey
        saury_btn.pack(side=TOP, expand=True, fill=BOTH)
        sardine_btn = tk.Button(self.frame_menu, text='沙丁魚', command=self.sardine_new_window,
                                font=('Arial', 18, 'bold'), bg="white", fg='black')  # Charcoal Blue
        sardine_btn.pack(side=TOP, expand=True, fill=BOTH)
        squid_btn = tk.Button(self.frame_menu, text='魷魚', command=self.squid_new_window,
                              font=('Arial', 18, 'bold'), bg="white", fg='black')  # Neon Blue
        squid_btn.pack(side=TOP, expand=True, fill=BOTH)
        btn_back = tk.Button(self.frame_menu, text='返回', command=self.back, font=('Arial', 18, 'bold'))
        btn_back.pack(side=TOP, expand=True, fill=BOTH)

    def saury_new_window(self):
        self.saury_menu = SauryMenu(self.root)
        self.saury_frame_exit = True

        if self.sardine_frame_exit:
            self.sardine_menu.frame_destroy()
            self.sardine_frame_exit = False

        if self.squid_frame_exit:
            self.squid_menu.frame_destroy()
            self.squid_frame_exit = False

    def sardine_new_window(self):
        self.sardine_menu = SardineMenu(self.root)
        self.sardine_frame_exit = True

        if self.saury_frame_exit:
            self.saury_menu.frame_destroy()
            self.saury_frame_exit = False

        if self.squid_frame_exit:
            self.squid_menu.frame_destroy()
            self.squid_frame_exit = False

    def squid_new_window(self):
        self.squid_menu = SquidMenu(self.root)
        self.squid_frame_exit = True

        if self.saury_frame_exit:
            self.saury_menu.frame_destroy()
            self.saury_frame_exit = False

        if self.sardine_frame_exit:
            self.sardine_menu.frame_destroy()
            self.sardine_frame_exit = False

    def back(self):
        self.frame_menu.destroy()
        InitialFrame(self.root)


class SauryMenu:
    def __init__(self, master):

        # root 背景設定
        self.root = master
        self.root.config(bg="#98AFC7")  # Blue Gray

        # frame_menu 背景設定
        self.saury_menu = tk.Frame(self.root)  # 在 root 上建 FrameMenu
        self.saury_menu.config(bg="#737CA1")  # Slate Blue Grey
        self.saury_menu.place(relx=0.275, rely=0.025, relheight=0.95, relwidth=0.7)

        # saury_menu 上的物件設定
        self.frame_label1 = tk.Label(self.saury_menu, text='海溫(°C): ')
        self.frame_label1.place(relx=0.07, rely=0.75)

        self.frame_entry = tk.Entry(self.saury_menu)
        self.frame_entry.place(relx=0.07, rely=0.8, relheight=0.04, relwidth=0.16)

        self.frame_btn = tk.Button(self.saury_menu, text='確認', command=self.button_event)
        self.frame_btn.place(relx=0.25, rely=0.8, relheight=0.04, relwidth=0.06)

        self.frame_label2 = tk.Label(self.saury_menu, text='捕獲量(ton): ')
        self.frame_label2.place(relx=0.39, rely=0.75)

        self.frame_ans = tk.Text(self.saury_menu, height=1.5, width=20)
        self.frame_ans.place(relx=0.39, rely=0.8, relheight=0.04, relwidth=0.16)

        self.img = Image.open('Saury_range.jpg')
        self.img = self.img.resize((375, 250))
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.label_pic = tk.Label(self.saury_menu, image=self.tk_img)
        self.label_pic.place(relx=0.2, rely=0.05, relheight=0.4, relwidth=0.6)

    def button_event(self):
        x = float(self.frame_entry.get())
        y = -1135741.9808 * x**2 + 129342 * x - 2866.1217
        self.frame_ans.insert('insert', str(round(y, 3)))

    def frame_destroy(self):
        self.saury_menu.destroy()


class SardineMenu:
    def __init__(self, master):
        # root 背景設定
        self.root = master
        self.root.config(bg="#98AFC7")

        # sardine_menu 背景設定
        self.sardine_menu = tk.Frame(self.root)  # 在 root 上建 FrameMenu
        self.sardine_menu.config(bg="#36454F")  # Charcoal Blue
        self.sardine_menu.place(relx=0.275, rely=0.025, relheight=0.95, relwidth=0.7)

        # sardine_menu 上的物件設定
        self.frame_label1 = tk.Label(self.sardine_menu, text='海溫(°C): ')
        self.frame_label1.place(relx=0.07, rely=0.75)
        self.frame_entry = tk.Entry(self.sardine_menu)
        self.frame_entry.place(relx=0.07, rely=0.8, relheight=0.04, relwidth=0.16)
        self.frame_btn = tk.Button(self.sardine_menu, text='確認', command=self.button_event)
        self.frame_btn.place(relx=0.25, rely=0.8, relheight=0.04, relwidth=0.06)
        self.frame_label2 = tk.Label(self.sardine_menu, text='捕獲量(ton): ')
        self.frame_label2.place(relx=0.39, rely=0.75)
        self.frame_ans = tk.Text(self.sardine_menu, height=1.5, width=20)
        self.frame_ans.place(relx=0.39, rely=0.8, relheight=0.04, relwidth=0.16)

    def button_event(self):
        x = float(self.frame_entry.get())
        y = 77568397.53 - 10373035.10*x + 347362.90*x**2
        self.frame_ans.insert('insert', str(round(y, 3)))

    def frame_destroy(self):
        self.sardine_menu.destroy()


class SquidMenu:
    def __init__(self, master):
        # root 背景設定
        self.root = master
        self.root.config(bg="#98AFC7")

        # squid_menu 背景設定
        self.squid_menu = tk.Frame(self.root)  # 在 root 上建 FrameMenu
        self.squid_menu.config(bg="#1589FF")  # Neon Blue
        self.squid_menu.place(relx=0.275, rely=0.025, relheight=0.95, relwidth=0.7)

        # squid_menu 上的物件設定
        self.frame_label1 = tk.Label(self.squid_menu, text='海溫(°C): ')
        self.frame_label1.place(relx=0.07, rely=0.75)
        self.frame_entry = tk.Entry(self.squid_menu)
        self.frame_entry.place(relx=0.07, rely=0.8, relheight=0.04, relwidth=0.16)
        self.frame_btn = tk.Button(self.squid_menu, text='確認', command=self.button_event)
        self.frame_btn.place(relx=0.25, rely=0.8, relheight=0.04, relwidth=0.06)
        self.frame_label2 = tk.Label(self.squid_menu, text='捕獲量(ton): ')
        self.frame_label2.place(relx=0.39, rely=0.75)
        self.frame_ans = tk.Text(self.squid_menu, height=1.5, width=20)
        self.frame_ans.place(relx=0.39, rely=0.8, relheight=0.04, relwidth=0.16)

    def button_event(self):
        x = float(self.frame_entry.get())
        y = 1076487.66 - 88084.91 * x
        self.frame_ans.insert('insert', str(round(y, 3)))

    def frame_destroy(self):
        self.squid_menu.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    BaseDesk(root)
    root.mainloop()
