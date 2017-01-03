#!/usr/bin/python3
# -*- coding: utf-8 -*-

import clr
import sys
# мы не знаем какой каталог будет считаться рабочим при запуске, выполняем манипуляции по определению правильных путеей
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))#определяем путь к текущему файлу
sys.path.append(os.path.join(project_dir,"TestStack.White.0.13.3\\lib\\net40"))
sys.path.append(os.path.join(project_dir,"Castle.Core.3.3.0\\lib\\net40-client"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *
from TestStack.White.InputDevices import Keyboard # эмулятор клавиатуры
from TestStack.White.WindowsAPI import KeyboardInput # нужно знать коды клавиш


clr.AddReferenceByName('UIAutomationTypes, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import * # здесь находится класс ControlType

import time

def test_something():
    application = Application.Launch("C:\\Users\\chu\\Desktop\\Tools_for_testing\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")

    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter('test group') # получаем элемент у которого нет AutomationID, единственный вводимый элемент на странице
    KeyboardInput.Instance.PressSpecialKey(Keyboard.SpecialKeys.RETURN)

    time.sleep(10)

    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()



