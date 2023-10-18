#!/usr/bin/env python3
#!/usr/bin/env python3
from dog import Dog
import io
import sys
import types

class TestBark:
    '''Dog.bark() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog(name="Fido", breed="Golden Retriever")
        assert isinstance(fido.bark, types.MethodType)

    def test_prints_barking_message(self):
        '''prints "Fido is barking."'''  # Update the description
        fido = Dog(name="Fido", breed="Golden Retriever")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Fido is barking.\n"  # Update the expected value


