# coding: utf-8


class DataTable:
    # construtor
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []

    def getData(self):
        return self._data

    @property
    def name(self):
        return self._name


class Column:
    # construtor
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description
