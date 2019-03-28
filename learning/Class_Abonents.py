"""Класс Абонент: Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Дебет, Кредит,
Время междугородных и городских переговоров; Конструктор; Методы: установка значений атрибутов, получение значений
атрибутов, вывод информации. Создать массив объектов данного класса. Вывести сведения относительно абонентов,
у которых время городских переговоров превышает заданное.  Сведения относительно абонентов, которые пользовались
междугородной связью. Список абонентов в алфавитном порядке."""

class Abonents():
    class_mass=[]
    def __init__(self,id,familia,name,otchestvo,adress,nomer_credit_card,debet,kredit,time_intercity,time_city):
        self.id=id
        self.familia=familia
        self.name=name
        self.otchestvo=otchestvo
        self.adress=adress
        self.nomer_credit_card=nomer_credit_card
        self.debet=debet
        self.kredit=kredit
        self.time_intercity=time_intercity
        self.time_city=time_city
        self.class_mass.append(self)

    def change_name(self,new_name):
        self.name=new_name

    def change_familia(self,new_familia):
        self.familia=new_familia

    def change_otchestvo(self,new_otchestvo):
        self.otchestvo=new_otchestvo

    def change_adress(self,new_adress):
        self.adresss=new_adress

    def change_nomer_credit_card(self,new_nomer):
        self.nomer_credit_card=new_nomer

    def change_debet(self,new_debet):
        self.debet=new_debet

    def change_kredit(self,new_kredit):
        self.kredit=new_kredit

    def change_time_intercity(self,new_time):
        self.time_intercity=new_time

    def change_time_city(self,new_time):
        self.time_city=new_time

    @classmethod
    def print_out(cls):
        for obj in cls.class_mass:
            print(obj)

    @classmethod
    def time_city(cls,time):
        for obj in cls.class_mass:
            if obj.time_city>time:
                print(obj.familia,obj.name,obj.otchestvo, 'Время городских разговоров: ',obj.time_city)

    @classmethod
    def intercity(cls):
        for obj in cls.class_mass:
            if obj.time_intercity > 0:
                print(obj.familia, obj.name, obj.otchestvo, 'Звонил межгород')

    @classmethod
    def all_user(cls):
        def bySort(users):
            return users.familia
        mass=sorted(cls.class_mass,key=bySort)
        for obj in mass:
            print(obj.familia,obj.name, obj.otchestvo,'Адрес: ',obj.adress)

X=Abonents(1,'Petrov','Ivan','Borisovich','Moscow,Red Square,1',1234432112344321,100,999,150,300)
Y=Abonents(2,'Avanov','Diman','Petrovich','Schelkovo,Shirokaya,106',123123123123,120,299,550,100)
Z=Abonents(3,'Sidorov','Gavrila','Anatolievich','Noginsk,Kominterna,111',12312314234313,10,11,0,0)
#Abonents.time_city(100)
#Abonents.intercity()
Abonents.all_user()