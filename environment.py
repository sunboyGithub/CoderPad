'''

Python 3
Running CPython 3.10 - IntelliSense is enabled
Python 3 in CoderPad is generally identical to the Python 2.x environment.

One small difference is that mock is available in Python 3 in the stdlib, as unittest.mock.

Information about the Python 2.x environment is reproduced below:

The Python environment is augmented with a few REPL features as well as some helpful libraries.

The REPL uses IPython to provide a REPL with history, highlighting, and autocomplete. Additionally, whenever you run scripts in CoderPad’s editor, the REPL will deposit you at the exact line and state of any exceptions. If there were no errors, you will have a REPL with access to all of the variables and functions defined in your script.

The libraries included and ready for importing are:

- requests for simpler HTTP requests.
- beautifulsoup4 for HTML parsing.
-  numpy, scipy, pandas, scikit-learn, and statsmodels for advanced numerical analysis. Unfortunately, plotting does not work in CoderPad’s purely textual interface at this time.

Testing
We’ve got a few ways you can test your Python code in CoderPad:

1. The excellent unittest library that ships with Python by default. Here’s a quick example:

'''

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # s.split should throw when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

unittest.main(exit=False)
'''
2. The versatile pytest. The above snippet of code would look like the following when written for pytest:
'''
import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    # s.split should throw when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)

pytest.main()

'''
3. mock is also available if you need to stub out some behavior. Here’s a quick usage example:
'''

from mock import Mock

mock = Mock()
mock.method(1, 2, 3)
mock.method.assert_called_with('this should break')

'''
mock can of course be combined with unittest and pytest for even more fun.

4. hypothesis is available for property-based testing in Python. You can read more about it on their website, but here’s a stubbed example of how you might test that an encoding and decoding function both work:

'''

from hypothesis import given
from hypothesis.strategies import text

def encode(string):
    # return encoded string

def decode(string):
    # return decoded string

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

test_decode_inverts_encode()

'''
Calling test_decode_inverts_encode() fires up Hypothesis and tries to find an input that breaks your code.

Are there any libraries or settings we missed? Feel free to email us with suggestions!

'''