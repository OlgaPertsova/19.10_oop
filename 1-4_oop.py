"""
Задание 1
Реализуйте класс «Человек». Необходимо хранить
 в полях класса: ФИО, дату рождения, контактный телефон,
  город, страну, домашний адрес. Реализуйте методы класса
   для ввода данных, вывода данных, реализуйте доступ
    к отдельным полям через методы класса.
class Human:
    FIO = "П.О.В"
    year = 2023
    telefon = "8-909-420-99-45"
    city = "Псков"
    country = "РФ"
    address = "Рижский пр. 16"
    def setYear(self, year):
        if year > 2020:
            self.year = year

    def getYear(self):
        return self.year
    def Output(self):
        print(f"ФИО: {self.FIO}\n"
              f"Дата: {self.year}\n"
              f"Телефон: {self.telefon}\n"
              f"Город: {self.city}\n"
              f"Страна: {self.country}\n"
              f"Адрес: {self.address}\n"
              )
    def Input(self, FIO, year, telefon,city, country, address):
        self.FIO = FIO
        self.year = year
        self.telefon = telefon
        self.city = city
        self.country = country
        self.address = address

h1 = Human()
h1.Output()
h1.year = 2024
h1.setYear(2021)
h1.Input("П.Н.О.", 2072, "8-909-580-88-09", "Москва", "Россия", "Красная пл. 2")
h1.Output()

Задание 2
Создайте класс для подсчета максимума из четырех
 аргументов, минимума из четырех аргументов,
  средне-арифметического из четырех аргументов,
   факториала аргумента. Функциональность необходимо
    реализовать в виде статических методов.
import math
class Math:
    @staticmethod
    def Maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def Minimum(a, b,c, d):
        return min(a,b,c,d)
    @staticmethod
    def AVG(a,b,c,d):
        return (a + b+ c+d)/ 4
    @staticmethod
    def Fact(n):
        if (n==0 or n==1):
            return 1
        else:
            p =1
            for i in range(1, n+1):
                p *= i
            return p

print(Math.Maximum(1, 3, 10, -8))
print(Math.Fact(7))
print(Math.AVG(2,6,1,1))

Задание 3
Создать базовый класс Employer (служащий)
 с функцией Print(). Она должна выводить информацию
  о служащем. В случае базового класса это может быть
   строка Создайте от него три производных класса:
    President, Manager, Worker. Переопределите функцию Print() для
вывода информации, соответствующей каждому типу служащего.
Задание 4
Для классов из задания 3 реализуйте магический
 метод str, а также метод int (должен возвращать
  возраст служащего).

class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        pass

class Manager(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f"Менеджер {self.name}, возраст {self.age}")

class Worker(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f"Рабочий {self.name}, возраст {self.age}")

    def __str__(self):
        return f"Рабочий {self.name}, возраст {self.age}"

    def __int__(self):
        return self.age

m1 = Manager("Петров", 35)
m1.print()
w1 = Worker("Сидоров", 40)
w1.print()
print(w1)
print("Возраст", int(w1))


Задание 5
Создайте функцию для отображения текущего времени.
Произведите декорирование функции. Потенциальный вывод данных на экран:
***************************
23:00
***************************
В этом выводе на экран две линии из
 звездочек – результаты декорирования.
"""
import time

class CurrentTime:
    def curtime(func):
        def wrapper(self):
            print("********************")
            func(self)
            print("********************")

        return wrapper
    @curtime
    def mytime(self):
        dt = time.gmtime()
        print(dt.tm_hour +3,':',dt.tm_min)

dt = CurrentTime()
dt.mytime()


