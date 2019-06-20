from tkinter import *
import sqlite3
import os


class Report(Frame):  # Создаем класс для отображения всех окон с информацией
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        scrollbar = Scrollbar(self)
        scrollbar.pack(side='right', fill='y')
        self._text = Text(self, state=DISABLED, wrap='word', *args, **kwargs)
        self._text.pack(side='left', fill='both', expand=1)
        scrollbar['command'] = self._text.yview
        self._text['yscrollcommand'] = scrollbar.set

    def write(self, text):
        self._text.configure(state=NORMAL)
        self._text.insert(END, text)
        self._text.configure(state=DISABLED)

    def clear(self):
        self._text.configure(state=NORMAL)
        self._text.delete(0.0, END)
        self._text.configure(state=DISABLED)

    def get(self):
        return self._text.get(0.0, END)

    def flush(selfself):
        pass


def select_item(event):  # извлечение названия выбранного сорта пва
    sort_beer = (lst_box.get(lst_box.curselection()))
    get_information(sort_beer)


def refresh_list():  # обновление списка сортов
    lst_box.delete(0, END)
    cur.execute("SELECT name FROM table1 WHERE level=%s" % var.get())
    for beer in cur.fetchall():
        lst_box.insert(END, beer[0])


def refresh_volume():  # Пересчет литража
    liter = ent_litr.get()
    try:
        liter = float(liter)
        sort = lbl_name['text']
        get_information(sort, liter)
    except ValueError:
        pass


def cleaning():  # Очистка всех окон
    txt_opisanie.clear()
    txt_recept.clear()
    txt_ruls.clear()
    txt_haract.clear()


def get_proportions(info, liters):  # Преобразование пропорций под нужный литраж
    info = info.split(',')
    standard_volume = float(info[0])
    for ingredient_volume in range(len(info)):
        info[ingredient_volume] = (float(info[ingredient_volume]) / standard_volume) * liters
        info[ingredient_volume] = round(info[ingredient_volume], 1)
    return tuple(info)


def get_information(sort_beer, liters=10):  # Добавление инфы во все окна
    cur.execute("SELECT * FROM table1 WHERE name=%s" % ("'" + sort_beer + "'"));
    all_information = cur.fetchall()[0]
    transformation = get_proportions(all_information[7], liters)
    cleaning()
    lbl_name['text'] = all_information[1]
    txt_opisanie.write(all_information[2])
    txt_recept.write(all_information[3] % transformation[:len(transformation) - 1])
    txt_ruls.write(all_information[5] % (transformation[len(transformation) - 1], transformation[0]))
    txt_haract.write(all_information[4])
    if all_information[8]:
        lbl_remarc['text'] = all_information[8]
    else:
        lbl_remarc['text'] = ''


def run_print():  # запуск печати рецепта
    with open('recept.txt', 'a') as print_file:  # Создаем временный файл для печати
        print_file.write('\n')
        print_file.write(lbl_name['text'])
        print_file.write('\n')
        print_file.write(txt_opisanie.get())
        print_file.write('\nХарактеристики\n')
        print_file.write(txt_haract.get())
        print_file.write('\nРецепт:\n')
        print_file.write(txt_recept.get())
        print_file.write('\nПравила варки:\n')
        print_file.write(txt_ruls.get())
        os.startfile('recept.txt', 'print')
        with open('recept.txt', 'w') as clean_file:  # очищаем временный файл для будущей печати
            clean_file.write('')


def close():  # Функция закрытия окна с удалением временного файла и запросом на подтверждение закрытия
    def destroy1():  # ф-я подтверждения выхода
        ext_root.destroy()
        try:
            os.remove('recept.txt')
        except OSError:
            pass
        root.destroy()


    def destroy2():  # ф-я отмены процедуры выхода
        ext_root.destroy()
        for i in widgets:
            i['state'] = NORMAL
        root.protocol("WM_DELETE_WINDOW", close)
    widgets = [btn_refresh, btn_litr, btn_print, btn_exit, lst_box, rbtn_level1, rbtn_level2, rbtn_level3]
    for i in widgets:
        i['state'] = DISABLED
    root.protocol("WM_DELETE_WINDOW", DISABLED)
    ext_root = Toplevel()
    ext_root.protocol("WM_DELETE_WINDOW", destroy2)
    ext_root.title('Выход')
    ext_root.geometry('200x60')
    ext_root.wm_attributes('-topmost', 1)
    exit_lbl = Label(ext_root, text='Вы уверены, что хотите выйти?')
    exit_lbl.place(x=0, y=0)
    y_btn = Button(ext_root, text='Да!', height=1, width=5, command=destroy1, bg='red')
    y_btn.place(x=30, y=30)
    n_btn = Button(ext_root, text='Нет!', height=1, width=5, command=destroy2, bg='green')
    n_btn.place(x=100, y=30)
    ext_root.resizable(width=False, height=False)


cur = sqlite3.connect('beer.db').cursor()  # цепляем базу данных
root = Tk()
root.title('Домашнее пивоварение')
root.geometry('700x550')
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", close)

lst_box = Listbox(width=40, height=10)  # Создание списка для сортов пива
lst_box.place(x=5, y=3)
lst_box.bind('<<ListboxSelect>>', select_item)
var = IntVar()  # Создаем список сортов
var.set(1)
rbtn_level1 = Radiobutton(text='Сложность 1', variable=var, value=1)
rbtn_level1.place(x=260, y=3)
rbtn_level2 = Radiobutton(text='Сложность 2', variable=var, value=2)
rbtn_level2.place(x=260, y=25)
rbtn_level3 = Radiobutton(text='Сложность 3', variable=var, value=3)
rbtn_level3.place(x=260, y=47)
btn_refresh = Button(text="Обновить", height=1, width=13, command=refresh_list)
btn_refresh.place(x=260, y=80)
refresh_list()  # запуск содержимого листа по умолчанию
btn_print = Button(text="Печать", height=1, width=13, command=run_print)
btn_print.place(x=580, y=10)
btn_exit = Button(text="Выход", height=1, width=13, command=close)
btn_exit.place(x=580, y=140)
lbl_litr = Label(text="Литры:")  # создаем кнопку расчета литража
lbl_litr.place(x=260, y=115)
ent_litr = Entry(width=10, textvariable=StringVar())
ent_litr.place(x=305, y=115)
btn_litr = Button(text="Пересчитать", height=1, width=13, command=refresh_volume)
btn_litr.place(x=260, y=140)
lbl_name = Label(root, text='Описание: ')  # Создаем поле для указания сорта
lbl_name.place(x=5, y=180)
txt_opisanie = Report(root, width=50, height=5)
txt_opisanie.place(x=5, y=200)  # создаем текстовое окно для описания
lbl_haract = Label(root, text='Характеристика пива:')  # Создаем поле для указания характеристик
lbl_haract.place(x=430, y=180)
txt_haract = Report(root, width=30, height=5)  # Создаем текстовое поле для характеристик
txt_haract.place(x=430, y=200)
lbl_rec = Label(root, text='Рецепт:')  # создаем лейбл "рецепт"
lbl_rec.place(x=5, y=288)
txt_recept = Report(root, width=40, height=14)  # текстовое поле для рецепта
txt_recept.place(x=5, y=310)
txt_ruls = Report(root, width=40, height=12)  # текстовое поле для правил варки
txt_ruls.place(x=340, y=310)
lbl_ruls = Label(root, text='Процесс варки: ')  # Лейбл для обозначения процесса варки
lbl_ruls.place(x=340, y=288)
lbl_remarc = Label(root, width=55, height=1)
lbl_remarc.place(x=330, y=520)
root.mainloop()
