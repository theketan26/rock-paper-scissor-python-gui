import tkinter
import customtkinter as ctk
from PIL import ImageTk, Image
import random
import time


root = ctk.CTk()


ctk.CTkLabel(root, text='Rock Paper Scissors', font=('Arial', 24)).grid(row=0, column=0, columnspan=100, pady=20)


options = ['rock', 'paper', 'scissor']

p_option = options[0]
p_img = ImageTk.PhotoImage((Image.open(f'./img/{p_option}.png')).resize((75, 75)))
p_option_var = tkinter.StringVar()
p_option_var.set(p_option.upper())
p_img_label = tkinter.Label(root, textvariable=p_option_var, width=10, font=('Arial', 18))
p_score = tkinter.StringVar()
p_score.set('0')
p_score_label = ctk.CTkLabel(root, textvariable=p_score, font=('Arial', 18))
p_img_label.grid(row=1, column=0, padx=10, pady=10)
p_score_label.grid(row=2, column=0)


count = tkinter.StringVar()
count.set('Start')
count_label = ctk.CTkLabel(root, textvariable=count, font=('Arial', 18), width=20)
count_label.grid(row=1, column=1, padx=10)


o_option = options[1]
o_img = ImageTk.PhotoImage((Image.open(f'./img/{o_option}.png')).resize((75, 75)))
o_option_var = tkinter.StringVar()
o_option_var.set(o_option.upper())
o_img_label = tkinter.Label(root, textvariable=o_option_var, width=10, font=('Arial', 18))
o_score = tkinter.StringVar()
o_score.set('0')
o_score_label = ctk.CTkLabel(root, textvariable=o_score, font=('Arial', 18))
o_img_label.grid(row=1, column=2, padx=10, pady=10)
o_score_label.grid(row=2, column=2)


def work(opt):
    global p_score, o_score, p_img, o_img

    for i in range(3):
        count.set('   ' + str(3 - i) + '   ')
        root.update()
        time.sleep(1)

    p_option_var.set(options[opt].upper())
    o_option_var.set(options[random.choice([0, 1, 2])].upper())

    if p_option_var.get() == 'ROCK':
        if o_option_var.get() == 'PAPER':
            count.set('Lost')
            o_score.set(str(int(o_score.get()) + 1))
        elif o_option_var.get() == 'ROCK':
            count.set('Draw')
        else:
            count.set('Win')
            p_score.set(str(int(p_score.get()) + 1))
    elif p_option_var.get() == 'PAPER':
        if o_option_var.get() == 'SCISSOR':
            count.set('Lost')
            o_score.set(str(int(o_score.get()) + 1))
        elif o_option_var.get() == 'PAPER':
            count.set('Draw')
        else:
            count.set('Win')
            p_score.set(str(int(p_score.get()) + 1))
    else:
        if o_option_var.get() == 'ROCK':
            count.set('Lost')
            o_score.set(str(int(o_score.get()) + 1))
        elif o_option_var.get() == 'SCISSOR':
            count.set('Draw')
        else:
            count.set('Win')
            p_score.set(str(int(p_score.get()) + 1))

    print(p_option_var.get(), o_option_var.get(), count.get())

    p_img = ImageTk.PhotoImage((Image.open(f'./img/{p_option}.png')).resize((75, 75)))
    o_img = ImageTk.PhotoImage((Image.open(f'./img/{o_option}.png')).resize((75, 75)))

    root.update()


rock_button = ctk.CTkButton(root, text='Rock', command=lambda: work(0), width=25)
paper_button = ctk.CTkButton(root, text='Paper', command=lambda: work(1), width=25)
scissor_button = ctk.CTkButton(root, text='Scissor', command=lambda: work(2), width=25)
rock_button.grid(row=3, column=0, pady=10)
paper_button.grid(row=3, column=1)
scissor_button.grid(row=3, column=2)


root.mainloop()
