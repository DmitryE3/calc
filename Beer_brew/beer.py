from tkinter import *
import sqlite3


class Report(Frame): # Создаем класс для отображения всех окон с информацией
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent)

        scrollbar = Scrollbar(self)
        scrollbar.pack(side='right',fill='y')
        self._text = Text(self,state=DISABLED, wrap='word',*args,**kwargs)
        self._text.pack(side='left',fill='both',expand=1)
        scrollbar['command']=self._text.yview
        self._text['yscrollcommand']=scrollbar.set

    def write(self,text):
        self._text.configure(state=NORMAL)
        self._text.insert(END,text)
        self._text.configure(state=DISABLED)

    def clear(self):
        self._text.configure(state=NORMAL)
        self._text.delete(0.0,END)
        self._text.configure(state=DISABLED)

    def flush(selfself):
        pass

def select_item(event): #извлечение названия выбранного сорта пва
    sort_beer = (lst_box.get(lst_box.curselection()))
    run_beer(sort_beer)

def refresh_list():  #обновление списка сортов
    lst_box.delete(0,END)
    cur.execute("SELECT name FROM table1 WHERE level=%s"%var.get())
    for beer in cur.fetchall():
        lst_box.insert(END, beer[0])

def refresh_litr():
    litr=ent_litr.get()
    try:
        litr=float(litr)
        sort=lbl_name['text']
        run_beer(sort,litr)
    except ValueError:
        pass


def cleaning(): #Очистка всех окон
    txt_opisanie.clear()
    txt_recept.clear()
    txt_ruls.clear()
    txt_haract.clear()

def proporcii(info,litr): # Преобразование пропорций под нужный литраж
    info=info.split(',')
    x=float(info[0])
    for i in range(len(info)):
        info[i]=(float(info[i])/x)*litr
    return tuple(info)

def run_beer(sort_beer,x=23.5): # Добавление инфы во все окна
    cur.execute("SELECT * FROM table1 WHERE name=%s"%("'"+sort_beer+"'"));
    q = cur.fetchall()[0]
    cleaning()
    lbl_name['text']=q[1]
    txt_opisanie.write(q[2])
    txt_recept.write(q[3]%proporcii(q[7],x))
    txt_ruls.write(q[5])
    txt_haract.write(q[4])

beer_db=sqlite3.connect('beer.db')
cur=beer_db.cursor()

root = Tk()
root.title('Домашнее пивоварение')
root.geometry('700x550')
root.resizable(width=False,height=False)

lst_box = Listbox(root,width=40,height=10) #Создание списка для сортов пива, потом к нему прикрутим сложность
lst_box.place(x=5,y=3)
scrl_box = Scrollbar() #создаем полосу прокрутки для списка пив
scrl_box.pack(side='right',fill='y')
scrl_box['command']=lst_box.yview
lst_box['yscrollcommand']=scrl_box.set
lst_box.bind('<<ListboxSelect>>', select_item)

var=IntVar() #Создаем список сортов
var.set(1)
rbtn_level1=Radiobutton(root,text='Сложность 1',variable=var, value=1)
rbtn_level1.place(x=260,y=3)
rbtn_level2=Radiobutton(root,text='Сложность 2',variable=var, value=2)
rbtn_level2.place(x=260,y=25)
rbtn_level3=Radiobutton(root,text='Сложность 3',variable=var, value=3)
rbtn_level3.place(x=260,y=47)
btn_refresh=Button(root,text="Обновить", height=1,width=13,command=refresh_list)
btn_refresh.place(x=260,y=80)
refresh_list() #запуск содержимого листа по умолчанию

lbl_litr=Label(root,text="Литры:") #создаем кнопку расчета литража
lbl_litr.place(x=260,y=115)
ent_litr = Entry(root,width=10)
ent_litr.place(x=305,y=115)
btn_litr=Button(root,text="Пересчитать",height=1,width=13,command=refresh_litr)
btn_litr.place(x=260,y=140)


lbl_name = Label(root,text='Описание: ')  # Создаем поле для указания сорта
lbl_name.place(x=5,y=180)

txt_opisanie = Report(root,width=50, height=8)
txt_opisanie.place(x=5,y=200) #создаем текстовое окно для описания

lbl_haract = Label(root, text='Характеристика пива:') #Создаем поле для указания характеристик
lbl_haract.place(x=430,y=180)

txt_haract = Report(root, width=30, height=8) #Создаем текстовое поле для характеристик
txt_haract.place(x=430,y=200)

lbl_rec = Label(root,text='Рецепт:') # создаем лейбл "рецепт"
lbl_rec.place(x=5,y=339)

txt_recept = Report(root, width=30, height=11) # текстовое поле для рецепта
txt_recept.place(x=5,y=360)

txt_ruls = Report(root, width=50, height=8) # текстовое поле для правил варки
txt_ruls.place(x=270 ,y=360)

lbl_ruls = Label(root, text='Процесс варки: ') # Лейбл для обозначения процесса варки
lbl_ruls.place(x=270,y=339)

root.mainloop()
