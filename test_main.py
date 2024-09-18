# test_main.py
import unittest
from main import hello_world
from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from Ryan Pham!")
class TestGreetPerson(unittest.TestCase):
    def greet_person(name):
        name.assertEqual(greet_person(), "Hello, %s!" % (name))

if __name__ == '__main__':
    unittest.main()