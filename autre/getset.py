#!/usr/bin/env python3

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
    
    @property
    def password(self):
        return f"aaaa{self._password}"
    
    @password.setter
    def password(self, value):
        if len(value) > 4:
            self._password = value
        else:
            print("Mdp trop court")
paul = User("Paul", "azerty")
print(paul.password)
paul.password = "toto"
print(paul.password)