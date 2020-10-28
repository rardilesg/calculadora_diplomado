import unittest
import mods
from mods.calculadora import Calculadora10

class TestCalculadora(unittest.TestCase):

    def test_calculadora_correcta(self):
        cal = Calculadora10(100)
        self.assertEqual(cal.valor10, 10)
        
    def test_calculadora_incorrecta(self):
        cal = Calculadora10(100)
        self.assertNotEqual(cal.valor10, 20)
    
    def test_calculadora_no_enteros(self):
        self.assertRaises(TypeError, Calculadora10, '123')
        self.assertRaises(TypeError, Calculadora10, 'asdo1')

if __name__ == "__main__":
   unittest.main()