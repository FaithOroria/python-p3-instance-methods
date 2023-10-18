#!/usr/bin/env python3
from person import Person
import io
import sys
import types

class TestPerson:
    '''Person in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person(first_name="Guido", last_name="van Rossum", age=65)
        assert isinstance(guido.walk, types.MethodType)

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person(first_name="Guido", last_name="van Rossum", age=65)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.walk()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "The person is walking.\n"

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person(first_name="Guido", last_name="van Rossum", age=65)  # Provide first_name, last_name, and age arguments
        assert isinstance(guido.talk, types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person(first_name="Guido", last_name="van Rossum", age=65)  # Provide first_name, last_name, and age arguments
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World!\n"

