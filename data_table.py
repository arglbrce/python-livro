# coding: utf-8


class DataTable:
    # construtor
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []


class Column:
    # construtor
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description
