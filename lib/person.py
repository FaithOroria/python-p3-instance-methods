#!/usr/bin/env python3
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name}, and I am {self.age} years old."

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
