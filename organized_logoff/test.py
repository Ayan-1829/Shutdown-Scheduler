import os
import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import subprocess
import psutil

from ctypes import windll

from BlurWindow.blurWindow import blur


class topWindow():

    def __init__(self):
        self.pu = tkinter.Toplevel(st)
        self.pu.attributes('-transparentcolor', '#223333')
        self.pu.config(bg='#abefef')
        # self.pu.geometry('600x270')
        self.hour = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        self.min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                    '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                    '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

        label_fnt = ('Times', 14, 'bold')
        label_background = '#abefef'
        label_foreground = '#012323'

        row = 0
        col = 0

        self.x_coordinate = 20
        self.y_coordinate = 20
        self.width = 60
        self.height = 30

        button_font = ('Times', 14, 'bold')

        # ----------- time after -------------
        self.l1 = tkinter.Label(self.pu, font=label_fnt, bg=label_foreground, fg='white')
        # self.l1.grid(row=row, column=col, padx=10, pady=10)
        # col += 1
        self.l1.place(x=self.x_coordinate, y=self.y_coordinate)
        self.x_coordinate += 150

        self.cmb1 = ttk.Combobox(self.pu, value=self.hour, width=3)
        # self.cmb1.grid(row=row, column=col, padx=1, pady=10)
        # col += 1
        self.cmb1.place(x=self.x_coordinate, y=self.y_coordinate+3)
        self.x_coordinate += 48

        self.l2 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg=label_foreground)
        # self.l2.grid(row=row, column=col, padx=10, pady=10)
        # col += 1
        self.l2.place(x=self.x_coordinate, y=self.y_coordinate)
        self.x_coordinate += 60

        self.cmb2 = ttk.Combobox(self.pu, value=self.min, width=3)
        # self.cmb2.grid(row=row, column=col, padx=1, pady=10)
        # col += 1
        self.cmb2.place(x=self.x_coordinate, y=self.y_coordinate+3)
        self.x_coordinate += 45

        self.l3 = tkinter.Label(self.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
        # self.l3.grid(row=row, column=col, padx=10, pady=10)
        # col += 1
        self.l3.place(x=self.x_coordinate, y=self.y_coordinate)
        self.x_coordinate += 75

        self.button1 = tkinter.Button(master=self.pu, text='save', bg='#12ffdd', font=button_font,
                                      border=5, width=6)
        # self.button1.grid(row=row, column=col, padx=10, pady=10)
        # col += 1
        self.button1.place(x=self.x_coordinate, y=self.y_coordinate, width=self.width, height=self.height)
        self.x_coordinate += 20
        self.button1.bind("<Enter>", lambda x: self.button1.config(bg='#018888', fg='white'))
        self.button1.bind("<Leave>", lambda x: self.button1.config(bg='#12ffdd', fg='black'))

        # ----------- time at ---------------
        row = 1
        col = 0
        self.l4 = tkinter.Label(self.pu, font=label_fnt, bg=label_foreground, fg=label_background)
        # self.l4.grid(row=row, column=col, padx=10, pady=10)
        # col += 1

        self.cmb3 = ttk.Combobox(self.pu, value=self.hour, width=10)
        # self.cmb3.grid(row=row, column=col, padx=1, pady=10)
        # col += 1

        self.l5 = tkinter.Label(self.pu, text='Hours', font=label_fnt, bg=label_background, fg=label_foreground)
        # self.l5.grid(row=row, column=col, padx=10, pady=10)
        # col += 1

        self.cmb4 = ttk.Combobox(self.pu, value=self.min, width=10)
        # self.cmb4.grid(row=row, column=col, padx=1, pady=10)
        # col += 1

        self.l6 = tkinter.Label(self.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
        # self.l6.grid(row=row, column=col, padx=10, pady=10)
        # col += 1

        self.button2 = tkinter.Button(master=self.pu, text='save', bg='#12ffdd', font=button_font,
                                      border=5, width=6)
        # self.button2.grid(row=row, column=col, padx=10, pady=10)
        self.button2.bind("<Enter>", lambda x: self.button2.config(bg='#018888', fg='white'))
        self.button2.bind("<Leave>", lambda x: self.button2.config(bg='#12ffdd', fg='black'))

        # ---------- Close button ------------
        row = 4
        col = 1
        self.now_button = tkinter.Button(master=self.pu,
                                         text="Now",
                                         # text_color='White',
                                         # border_width=3,
                                         # border_color='white',
                                         # corner_radius=15,
                                         bg='#12ffdd',
                                         fg='black',
                                         font=button_font,
                                         border=5,
                                         width=6
                                         )
        # self.now_button.grid(row=row, column=col, pady=3)
        # col += 2
        self.now_button.bind("<Enter>", lambda x: self.now_button.config(bg='#018888', fg='white'))
        self.now_button.bind("<Leave>", lambda x: self.now_button.config(bg='#12ffdd', fg='black'))
        self.close_button = tkinter.Button(master=self.pu,
                                           text="Cancel",
                                           bg='red',
                                           fg='white',
                                           font=button_font,
                                           border=5,
                                           command=self.pu.destroy,
                                           width=6
                                           )
        # self.close_button.grid(row=row, column=col, pady=3)
        self.close_button.bind("<Enter>", lambda x: self.close_button.config(bg='#990000'))
        self.close_button.bind("<Leave>", lambda x: self.close_button.config(bg='red'))


def cal_after(a, b):
    return (a * 60 + b) * 60


def cal_at(a, b):
    ctime = time.localtime(time.time())
    hour = ctime.tm_hour
    minute = ctime.tm_min
    second = ctime.tm_sec

    if a < hour:
        a += 24
    a = a - hour

    if b < minute:
        a -= 1
        b += 60
    b = b - minute

    c = 0
    if c < second:
        b -= 1
        c += 60
    c = c - second

    return (a * 60 + b) * 60 + c


def shutdown():
    obj = topWindow()
    obj.pu.geometry('630x265')
    obj.pu.title("Shutdown menu")

    def f_now():
        os.system('shutdown -s -t 1')

    def f_after():
        a = int(v1.get())
        b = int(v2.get())
        work = cal_after(a, b)
        obj.pu.destroy()
        # print(work)
        os.system(f"shutdown -s -t {work}")

    def f_at():
        a = int(v3.get())
        b = int(v4.get())
        work = cal_at(a, b)
        obj.pu.destroy()
        os.system(f"shutdown -s -t {work}")

    def process_idle():
        obj.pu.destroy()
        st.destroy()
        p = psutil.Process(0)
        count = 0
        while True:
            cpu = p.cpu_percent(interval=1) / psutil.cpu_count()

            t = int(value.get()) * 60

            if cpu > 94:
                count += 1
            else:
                count = 0

            print("CPU percentage   : ", "{:.25f}".format(cpu))
            print(count)
            print()

            if count >= t:
                print("*****************************************************")
                print(f"Idle for {count} seconds")
                os.system("shutdown -s -t 1")

    # --------- Process idle -------------

    label_fnt = ('Times', 14, 'bold')
    label_background = '#abefef'
    label_foreground = '#012323'

    row = 2
    col = 0
    obj.time = ['1', '2', '3', '4', '5', '10', '11', '15', '20', '25', '30']
    obj.l7 = tkinter.Label(obj.pu, text='                  Process idle for                  ', font=label_fnt,
                           bg=label_foreground, fg=label_background)
    obj.l7.grid(row=row, column=col, columnspan=3, padx=10, pady=10)
    col += 3

    obj.cmb5 = ttk.Combobox(obj.pu, value=obj.time, width=10)
    obj.cmb5.grid(row=row, column=col, padx=1, pady=10)
    obj.cmb5.current(4)
    col += 1

    obj.l7 = tkinter.Label(obj.pu, text='Minutes', font=label_fnt, bg=label_background, fg=label_foreground)
    obj.l7.grid(row=row, column=col, padx=10, pady=10)
    col += 1

    obj.button3 = tkinter.Button(master=obj.pu, text='save', bg='#12ffdd', font=button_font, border=5, width=6)
    obj.button3.grid(row=row, column=col, padx=10, pady=10)
    obj.button3.bind("<Enter>", lambda x: obj.button3.config(bg='#018888', fg='white'))
    obj.button3.bind("<Leave>", lambda x: obj.button3.config(bg='#12ffdd', fg='black'))

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.button3.config(command=process_idle)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='  Shutdown after :  ')
    obj.l4.config(text='    Shutdown at :   ')

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    value = StringVar()
    obj.cmb1.config(textvariable=v1)
    obj.cmb2.config(textvariable=v2)
    obj.cmb3.config(textvariable=v3)
    obj.cmb4.config(textvariable=v4)
    obj.cmb5.config(textvariable=value)

    obj.cmb1.current(0)
    obj.cmb2.current(0)
    obj.cmb3.current(0)
    obj.cmb4.current(0)
    obj.cmb5.current(4)

    obj.pu.mainloop()


def restart():
    obj = topWindow()
    obj.pu.geometry('605x200')
    obj.pu.title("Restart menu")

    def f_now():
        os.system('shutdown -r -t 1')

    def f_after():
        a = int(v1.get())
        b = int(v2.get())
        work = cal_after(a, b)
        obj.pu.destroy()
        # print(work)
        os.system(f"shutdown -r -t {work}")

    def f_at():
        a = int(v3.get())
        b = int(v4.get())
        work = cal_at(a, b)
        obj.pu.destroy()
        os.system(f"shutdown -r -t {work}")

    obj.button1.config(command=f_after)
    obj.button2.config(command=f_at)
    obj.now_button.config(command=f_now)

    obj.l1.config(text='  Restart after :  ')
    obj.l4.config(text='   Restart at :    ')

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    obj.cmb1.config(textvariable=v1)
    obj.cmb2.config(textvariable=v2)
    obj.cmb3.config(textvariable=v3)
    obj.cmb4.config(textvariable=v4)

    obj.cmb1.current(0)
    obj.cmb2.current(0)
    obj.cmb3.current(0)
    obj.cmb4.current(0)

    obj.pu.mainloop()


def screen_off():
    subprocess.call([r'monitor_off.bat'])


def logoff():
    os.system('shutdown -l')


def hibernate():
    os.system('shutdown -h')


def abort():
    os.system("shutdown -a")


def on_enter(b):
    b.config(bg="#018888", fg="#ffffff", border=5)


def on_leave(b):
    b.config(bg="#12ffdd", fg="#000000", border=5)


st = tkinter.Tk()
# st.attributes('-transparentcolor', '#012345')
st.title("Task Scheduler")
st.geometry("320x400")
st.config(bg='#abefef')
st.iconbitmap(r'shutdown.ico')
st.resizable(False, False)
# st.overrideredirect(True)
# hWnd = windll.user32.GetForegroundWindow()
# blur(hWnd)

x_coordinate = 80
y_coordinate = 40

button_font = ('Times', 15, 'bold')
button_width = 160
button_hight = 40
button_distance = 45

restart_button = tkinter.Button(master=st,
                                text="Restart",
                                border=5,
                                bg='#12ffdd',
                                font=button_font,
                                command=lambda: restart()
                                )
restart_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
restart_button.bind("<Enter>", lambda x: on_enter(restart_button))
restart_button.bind("<Leave>", lambda x: on_leave(restart_button))
y_coordinate += button_distance

shutdown_button = tkinter.Button(master=st,
                                 text="Shutdown",
                                 border=5,
                                 bg='#12ffdd',
                                 font=button_font,
                                 command=shutdown
                                 )
shutdown_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
shutdown_button.bind("<Enter>", lambda x: on_enter(shutdown_button))
shutdown_button.bind("<Leave>", lambda x: on_leave(shutdown_button))
y_coordinate += button_distance

logoff_button = tkinter.Button(master=st,
                               text="Sign out",  # logoff
                               border=5,
                               bg='#12ffdd',
                               font=button_font,
                               command=logoff
                               )
logoff_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
logoff_button.bind("<Enter>", lambda x: on_enter(logoff_button))
logoff_button.bind("<Leave>", lambda x: on_leave(logoff_button))
y_coordinate += button_distance

hibernate_button = tkinter.Button(master=st,
                                  text="Hibernate",
                                  border=5,
                                  bg='#12ffdd',
                                  font=button_font,
                                  command=hibernate
                                  )
hibernate_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
hibernate_button.bind("<Enter>", lambda x: on_enter(hibernate_button))
hibernate_button.bind("<Leave>", lambda x: on_leave(hibernate_button))
y_coordinate += button_distance

scroff_button = tkinter.Button(master=st,
                               text="Screen off",
                               border=5,
                               bg='#12ffdd',
                               font=button_font,
                               command=screen_off
                               )
scroff_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
scroff_button.bind("<Enter>", lambda x: on_enter(scroff_button))
scroff_button.bind("<Leave>", lambda x: on_leave(scroff_button))
y_coordinate += button_distance

abort_button = tkinter.Button(master=st,
                              text="Abort",
                              border=5,
                              bg='#12ffdd',
                              font=button_font,
                              command=abort
                              )
abort_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
abort_button.bind("<Enter>", lambda x: on_enter(abort_button))
abort_button.bind("<Leave>", lambda x: on_leave(abort_button))
y_coordinate += button_distance

close_button = tkinter.Button(master=st,
                              text="Close",
                              border=5,
                              bg='red',
                              fg='white',
                              font=button_font,
                              command=st.destroy
                              )
close_button.place(x=x_coordinate, y=y_coordinate, width=button_width, height=button_hight)
close_button.bind("<Enter>", lambda x: close_button.config(bg="#bb0000"))
close_button.bind("<Leave>", lambda x: close_button.config(bg='red'))
y_coordinate += button_distance

# os.startfile("C:\Others\Studies\Mid_Night_Thoughts\mynotepad\mynotepad.exe")

st.mainloop()

