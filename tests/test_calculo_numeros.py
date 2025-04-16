import unittest
#from src.exceptions import (
#    ingrese_numero,
#   NumeroDebeSerPositivo,
#)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    @patch(
        'builtins.input',
        return_value='55'
    )
    def test_ingreso_bien(self, patch_input):
        numero=ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(
        'builtins.input',
        return_value='-100'
        )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    @patch(
        'builtins.input',
        return_value='-2'
        )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 