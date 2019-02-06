from tkinter import *
import recepts

class Report(Frame):
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


root = Tk()
root.title('Домашнее пивоварение')
root.geometry('700x370')

lbl_name = Label(root,text='Описание: ')  # Создаем поле для указания сорта
lbl_name.place(x=0,y=0)

txt_opisanie = Report(root,width=50, height=8)
txt_opisanie.place(x=0,y=20) #создаем текстовое окно для описания

lbl_haract = Label(root, text='Характеристика пива:') #Создаем поле для указания характеристик
lbl_haract.place(x=430,y=0)

txt_haract = Report(root, width=30, height=8) #Создаем текстовое поле для характеристик
txt_haract.place(x=430,y=20)

lbl_rec = Label(root,text='Рецепт:') # создаем лейбл "рецепт"
lbl_rec.place(x=0,y=159)

txt_recept = Report(root, width=30, height=11) # текстовое поле для рецепта
txt_recept.place(x=0,y=180)

txt_ruls = Report(root, width=50, height=8) # текстовое поле для правил варки
txt_ruls.place(x=270 ,y=180)

lbl_ruls = Label(root, text='Процесс варки: ') # Лейбл для обозначения процесса варки
lbl_ruls.place(x=270,y=159)

mainmenu = Menu(root)  # создаем меню выбора сортов
root.config(menu=mainmenu)

hard = Menu(mainmenu, tearoff=0)  # Создаем меню разного
#hard.add_command(label='Борщ', command=recepts.borsh)

stout_command=[['Золотистый эль в английском стиле',recepts.easy1],['стаут 2',recepts.easy2],['стаут 3',recepts.easy3]]
easy = Menu(mainmenu, tearoff=0)  # Создаем меню для стаутов
for i in stout_command:
    easy.add_command(label=i[0],command=i[1])

apa = ['апа 1', 'апа 2']
medium = Menu(mainmenu, tearoff=0)  # Создаем меню для АПА
medium.add_command(label='АПА1',command=recepts.apa1)

mainmenu.add_cascade(label='Сложность 1', menu=easy)
mainmenu.add_cascade(label='Сложность 2', menu=medium)
mainmenu.add_cascade(label='Сложность 3', menu=hard)

root.mainloop()
