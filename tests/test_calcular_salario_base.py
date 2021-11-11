import unittest

from vendedor import Vendedor


class TestCalcularSalarioBase(unittest.TestCase):

    def setUp(self):
        print('Executou setUp')
        self.vendedor = Vendedor('Victor', 0, 0.0)

    # Entrada 0
    # Saída esperada: 0.0
    def test_ct_01(self):
        self.vendedor.meses_contratado = 0
        self.assertEqual(self.vendedor.calcular_salario_base(), 0.0)

    # Entrada 1
    # Saída esperada: 1500.0
    def test_ct_02(self):
        self.vendedor.meses_contratado = 1
        self.assertEqual(self.vendedor.calcular_salario_base(), 1500.0)

    # Entrada 2
    # Saída esperada: 1500.0
    def test_ct_03(self):
        self.vendedor.meses_contratado = 2
        self.assertEqual(self.vendedor.calcular_salario_base(), 1500.0)

    # Entrada 11
    # Saída esperada: 1500.0
    def test_ct_04(self):
        self.vendedor.meses_contratado = 11
        self.assertEqual(self.vendedor.calcular_salario_base(), 1500.0)

    # Entrada 12
    # Saída esperada: 1500.0
    def test_ct_05(self):
        self.vendedor.meses_contratado = 12
        self.assertEqual(self.vendedor.calcular_salario_base(), 1500.0)

    # Entrada 13
    # Saída esperada: 2000.0
    def test_ct_06(self):
        self.vendedor.meses_contratado = 13
        self.assertEqual(self.vendedor.calcular_salario_base(), 2000.0)

    # Entrada 23
    # Saída esperada: 2000.0
    def test_ct_07(self):
        self.vendedor.meses_contratado = 23
        self.assertEqual(self.vendedor.calcular_salario_base(), 2000.0)

    # Entrada 24
    # Saída esperada: 2000.0
    def test_ct_08(self):
        self.vendedor.meses_contratado = 24
        self.assertEqual(self.vendedor.calcular_salario_base(), 2000.0)

    # Entrada 25
    # Saída esperada: 2500.0
    def test_ct_09(self):
        self.vendedor.meses_contratado = 25
        self.assertEqual(self.vendedor.calcular_salario_base(), 2500.0)

    # Entrada 35
    # Saída esperada: 2500.0
    def test_ct_10(self):
        self.vendedor.meses_contratado = 35
        self.assertEqual(self.vendedor.calcular_salario_base(), 2500.0)

    # Entrada 36
    # Saída esperada: 2500.0
    def test_ct_11(self):
        self.vendedor.meses_contratado = 36
        self.assertEqual(self.vendedor.calcular_salario_base(), 2500.0)

    # Entrada 37
    # Saída esperada: 3000.0
    def test_ct_12(self):
        self.vendedor.meses_contratado = 37
        self.assertEqual(self.vendedor.calcular_salario_base(), 3000.0)