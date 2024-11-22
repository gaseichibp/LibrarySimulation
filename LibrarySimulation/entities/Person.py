class Person:
    def __init__(self, name, cpf, phone):
        self._name = name
        self._cpf = cpf
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def phone(self):
        return self._phone

    @name.setter
    def name(self, name):
        self._name = name

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    def __str__(self):
        return f"Person{{name='{self._name}', cpf='{self._cpf}', phone='{self._phone}'}}"