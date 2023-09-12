import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

praise = ['Умничка!', 'Правильно!', 'Абсолютно верно!', 'Молодец!', 'Так держать!', 'Правильный ответ!']
reassure = ['Попробуй еще раз!', 'Пока не верно!', 'Нужно ещё постараться!', 'Не правильный ответ.']
levels = ['Easy', 'Middle', 'Hard']
actions = ['Сложение', 'Вычитание', 'Умножение', 'Деление']
scores_count = 0
ex = ''
right_answer = ''

def clear():
    answer.delete(0, tk.END)
    tk.Label(win, text=f'', font=('Arial', 13),
             relief=tk.RAISED, bd=5).grid(row=4, column=0, columnspan=2, padx=5, pady=5, stick='we')

def calc_scores():
    global scores_count
    scores_count += 5
    return scores_count

def create_math():
    global ex
    if combo1.get() == 'Easy':
        if combo2.get() == 'Сложение':
            ex = f"{random.randint(1,50)} + {random.randint(1,50)}"
        elif combo2.get() == 'Вычитание':
            ex = f"{random.randint(50, 100)} - {random.randint(1, 50)}"
        elif combo2.get() == 'Умножение':
            ex = f"{random.randint(1, 10)} * {random.randint(1, 11)}"
        elif combo2.get() == 'Деление':
            a = random.randint(1, 10)
            b = random.randint(1, 11)
            c = a * b
            ex = f"{c} / {a}"

    elif combo1.get() == 'Middle':
        if combo2.get() == 'Сложение':
            ex = f"{random.randint(30,400)} + {random.randint(30,400)}"
        elif combo2.get() == 'Вычитание':
            ex = f"{random.randint(100, 400)} - {random.randint(50, 100)}"
        elif combo2.get() == 'Умножение':
            ex = f"{random.randint(5, 11)} * {random.randint(5, 11)}"
        elif combo2.get() == 'Деление':
            a = random.randint(10, 50)
            b = random.randint(10, 50)
            c = a * b
            ex = f"{c} / {a}"

    elif combo1.get() == 'Hard':
        if combo2.get() == 'Сложение':
            ex = f"{random.randint(1, 100)} + {random.randint(1, 100)} + {random.randint(1, 100)}"
        elif combo2.get() == 'Вычитание':
            ex = f"{random.randint(50, 100)} - {random.randint(1, 50)} - {random.randint(1, 100)}"
        elif combo2.get() == 'Умножение':
            ex = f"{random.randint(1, 10)} * {random.randint(1, 11)} * {random.randint(1, 11)}"
        elif combo2.get() == 'Деление':
            a = random.randint(10, 31)
            b = random.randint(10, 31)
            c = a * b
            ex = f"{c} / {a}"

    tk.Label(win, text=f'{ex}', font=('Arial', 13),
             relief=tk.RAISED, bd=5).grid(row=4, column=0, columnspan=2, padx=5, pady=5, stick='we')


def show_answer():
    global right_answer
    right_answer = str(round(eval(ex)))
    if answer.get().isdigit():
        if answer.get() == right_answer:
            if show_answer_val.get() == 'Yes':
                tk.Label(win, text=f'{right_answer}', font=('Arial', 13),
                     relief=tk.RAISED, bd=5).grid(row=7, column=1, padx=5, pady=5, stick='we')
            else:
                tk.Label(win, text=f'{random.choice(praise)}', font=('Arial', 13),
                         relief=tk.RAISED, bd=5).grid(row=7, column=1, padx=5, pady=5, stick='we')
            if calc_scores_val.get() == 'Yes':
                calc_scores()
                tk.Label(win, text=f"{name.get()} у тебя {scores_count} баллов", font=('Arial', 13),
                         relief=tk.RAISED, bd=5).grid(row=8, column=1, padx=5, pady=5, stick='we')
            clear()
        else:
            tk.Label(win, text=f'{random.choice(reassure)}', font=('Arial', 13),
                     relief=tk.RAISED, bd=5).grid(row=7, column=1, padx=5, pady=5, stick='we')
    else:
        messagebox.showinfo('Нужно ввести цифры! Вы ввели другие символы.')


win = tk.Tk()
win.geometry(f"450x500+100+100")
win.title('Занимательная математика')
win.config(bg="#5FD2B5")

name = tk.Entry(win, font=('Arial', 13))
answer = tk.Entry(win, font=('Arial', 13))
calc_scores_val = tk.StringVar()
calc_scores_val.set(0)
show_answer_val = tk.StringVar()
show_answer_val.set(0)

tk.Checkbutton(win, text='Подсчитывать очки',
                         variable=calc_scores_val, offvalue='No', onvalue="Yes",
               font=('Arial', 13)).grid(row=2, column=0, padx=5, pady=5, stick='we')
tk.Checkbutton(win, text='Показать ответ',
                         variable=show_answer_val, offvalue='No', onvalue='Yes',
               font=('Arial', 13)).grid(row=2, column=1, padx=5, pady=5, stick='we')
tk.Label(win, text ='Напиши свое имя', font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=0, column=0, padx=5, pady=5, stick='we')
name.grid(row=0, column=1, columnspan=3, padx=5, pady=5, stick='wens')
answer.grid(row=5, column=1, padx=5, pady=5, stick='wens')


combo1 = ttk.Combobox(win, font=('Arial', 13), values=levels)
combo1.current(0)
combo1.grid(row=1, column=0, padx=5, pady=5, stick='we')

combo2 = ttk.Combobox(win, font=('Arial', 13), values=actions)
combo2.current(0)
combo2.grid(row=1, column=1, padx=5, pady=5, stick='we')



tk.Button(win,text='Начать',command=create_math, font=('Arial', 13),
          relief=tk.RAISED, bd=5).grid(row=3,column=0, columnspan=2,padx=5, pady=5, stick='we')

tk.Button(win,text='Подтвердить',command=show_answer, font=('Arial', 13),
          relief=tk.RAISED, bd=5).grid(row=6,column=0, columnspan=2,padx=5, pady=5, stick='we')

tk.Label(win, text ='', font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=4, column=0, columnspan=2, padx=5, pady=5, stick='we')

tk.Label(win, text ='Твой ответ', font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=5, column=0, padx=5, pady=5, stick='we')

tk.Label(win, text ='Правильный ответ', font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=7, column=0, padx=5, pady=5, stick='we')
tk.Label(win, text ='Начисленные баллы', font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=8, column=0, padx=5, pady=5, stick='we')
tk.Label(win, text= "", font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=7, column=1, padx=5, pady=5, stick='we')
tk.Label(win, text= f"{right_answer}", font=('Arial', 13),
         relief=tk.RAISED, bd=5).grid(row=7, column=1, padx=5, pady=5, stick='we')
tk.Label(win, text='', font=('Arial', 13),
                 relief=tk.RAISED, bd=5).grid(row=8, column=1, padx=5, pady=5, stick='we')
win.mainloop()