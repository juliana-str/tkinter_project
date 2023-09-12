import tkinter as tk
import random
from decimal import *

praise = ['Умничка!', 'Правильно!', 'Абсолютно верно!', 'Молодец!', 'Так держать!', 'Правильный ответ!']
reassure = ['Попробуй еще раз!', 'Пока не верно!', 'Нужно ещё постараться!', 'Не правильный ответ.']
answer = 0



def valid():
    if not (first_value.get().isdigit() and second_value.get().isdigit()):
        tk.Label(win, text='Нужно ввести числа', bg='red', font=('Arial', 12, 'bold')).grid(row=5, column=1,
                                                                                        columnspan=2, stick='we')
    else:
        return True

def mult():
    global answer
    if valid():
        answer = Decimal(first_value.get()) * Decimal(second_value.get())
        return answer


def division():
    global answer
    if valid():
        try:
            answer = Decimal(first_value.get()) / Decimal(second_value.get())
        except ZeroDivisionError:
            tk.Label(win, text='На 0 делить нельзя', bg='red', font=('Arial', 12, 'bold')).grid(row=5, column=1,
                                                                                        columnspan=2,stick='we')
        return answer

def subtraction():
    global answer
    if valid():
        answer = Decimal(first_value.get()) - Decimal(second_value.get())
        return answer

def addition():
    global answer
    if valid():
        answer = Decimal(first_value.get()) + Decimal(second_value.get())
        return answer

def get_answer():
    global answer
    if ent_answer.get():
        value = Decimal(ent_answer.get())
        if answer == value:
            tk.Label(win, text=f'{random.choice(praise)}', bg='green', font=('Arial', 12, 'bold')).grid(row=5, column=1,
                                                                                        columnspan=2,stick='we')
        else:
            tk.Label(win, text=f'{random.choice(reassure)}', bg='red', font=('Arial', 12, 'bold')).grid(row=5, column=1,
                                                                                                columnspan=2,stick='we')
    else:
        tk.Label(win, text='Нужно ввести ответ', bg='yellow', font=('Arial', 12, 'bold'),).grid(row=5, column=1,
                                                                                                columnspan=2,stick='we')
def delete_entry():
    first_value.delete(0, tk.END)
    second_value.delete(0, tk.END)
    ent_answer.delete(0, tk.END)
    tk.Label(win, text='',bg='white', font=('Arial', 12, 'bold'),).grid(row=5, column=1, columnspan=2,stick='we')

win = tk.Tk()
win.title('Проверь себя')
win.geometry(f"500x600+100+200")

tk.Label(win, text='Первое число',font=('Arial', 12, 'bold')).grid(row=0, column=0, stick='we')
tk.Label(win, text='Второе число',font=('Arial', 12, 'bold')).grid(row=1, column=0, stick='we')
tk.Label(win, text='Действие',font=('Arial', 12, 'bold')).grid(row=2, column=0, stick='we')
tk.Label(win, text='Твой ответ',font=('Arial', 12, 'bold')).grid(row=4, column=0, stick='we')
tk.Label(win, text='Результат',font=('Arial', 12, 'bold')).grid(row=5, column=0, stick='we')



first_value = tk.Entry(win)
second_value = tk.Entry(win)
ent_answer = tk.Entry(win)


first_value.grid(row=0, column=1)
second_value.grid(row=1,column=1)
ent_answer.grid(row=4, column=1)


tk.Button(win,text='*',command=mult,font=('Arial', 14, 'bold')).grid(row=2,column=1,stick='we', padx=5, pady=5)
tk.Button(win,text='/',command=division,font=('Arial', 14, 'bold')).grid(row=2,column=2,stick='we', padx=5, pady=5)
tk.Button(win,text='-',command=subtraction,font=('Arial', 14, 'bold')).grid(row=3,column=1,stick='we', padx=5, pady=5)
tk.Button(win,text='+',command=addition,font=('Arial', 14, 'bold')).grid(row=3,column=2,stick='we', padx=5, pady=5)
tk.Button(win,text='Подтвердить',command=get_answer,font=('Arial', 12, 'bold')).grid(row=4,column=2, padx=5, pady=5)
tk.Button(win, text='Удалить',command=delete_entry,font=('Arial', 12, 'bold')).grid(row=6,column=3, padx=5, pady=5)

win.mainloop()
