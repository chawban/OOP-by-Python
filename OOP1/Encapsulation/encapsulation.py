class Person:
    def __init__(self, name, age):
        self.name = name     # public
        self._age = age      # protected
        self.__password = "" # private

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
