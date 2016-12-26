#!/usr/bin/python3
# -*- coding: utf-8 -*-
# генератор групп

from model.group import Group
import random
import string                                                              # содержит константы хранящие списки символов
import os.path

import getopt # для чтения опций из командной строки
import sys # для того чтобы получить доступ к этим опциям
import clr # виртуальная машина .Net command language runtime
import time
#подключаем excel
clr. AddReferenceByName("Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c")
from Microsoft.Office.Interop import Excel



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) # n - количество генерируемых данных,
except getopt.GetoptError as err:                                                 # f- файл в который это все помещается
    # sys.argv это список параметров, которые переданы в программу из командной строки при запуске
    #1: это диапазон от второго элемента списка до последнего
    #почему от второго? потому что первый элемент в sys.argv это сам запускаемый сценарий, а дальше уже идут опции

    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.xlsx"

for o, a in opts:                   # o - название опции, a - ее значение
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_letters + string.digits #+ " "*10 + string.punctuation
    return prefix + "".join ([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную

testdata = [ Group(name="")] + [
            Group(name=random_string("name", 10))
             for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)  # получаем информацию о пути к текущему файлу

#with open(file, "w") as out:
 #   jsonpickle.set_encoder_options("json", indent = 2)
#    out.write(jsonpickle.encode(testdata)) # default=lambda x: x.__dict__, indent=2)) # __dict__хранит все свойства которые мы присваиваем в поля с self
                                                                            # функция dumps превращает некоторую структуру данных в строку в формате json
excel = Excel.ApplicationClass()
excel.Visible = True # чтобы информация выводилась на экран

time.sleep(10)