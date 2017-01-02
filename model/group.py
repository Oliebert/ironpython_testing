#!/usr/bin/python3
# -*- coding: utf-8 -*-


from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name


    def __repr__(self):

        return  self.name

    def __eq__(self, other):                                                                            # gruppen sind gleich wenn Namen oder ids sind gleich
                                                                                                        # oder einer der ids ist None
        return self.name == other.name

    def key(self):  # функция вычисляет по группе ключ для сравнения

        return self.name  # ели нет идентификатора, то присваевается максимально возможное число