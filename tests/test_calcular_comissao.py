import unittest

from vendedor import Vendedor


class TestCalcularComissao(unittest.TestCase):

    def setUp(self):
        print('Executou setUp')
        self.vendedor = Vendedor('Victor', 0, 0.0)

    def test_ct_01(self):
        self.vendedor.valor_venda = -0.01
        self.assertEqual(self.vendedor.calcular_comissao(), 0.0)

    def test_ct_02(self):
        self.vendedor.valor_venda = 0.00
        self.assertEqual(self.vendedor.calcular_comissao(), 0.0)

    def test_ct_03(self):
        self.vendedor.valor_venda = 0.01
        self.assertEqual(self.vendedor.calcular_comissao(), 0.03)

    def test_ct_04(self):
        self.vendedor.valor_venda = 9999.99
        self.assertEqual(self.vendedor.calcular_comissao(), 0.03)

    def test_ct_05(self):
        self.vendedor.valor_venda = 10000.00
        self.assertEqual(self.vendedor.calcular_comissao(), 0.03)

    def test_ct_06(self):
        self.vendedor.valor_venda = 10000.01
        self.assertEqual(self.vendedor.calcular_comissao(), 0.05)

    def test_ct_07(self):
        self.vendedor.valor_venda = 49999.99
        self.assertEqual(self.vendedor.calcular_comissao(), 0.05)

    def test_ct_08(self):
        self.vendedor.valor_venda = 50000.00
        self.assertEqual(self.vendedor.calcular_comissao(), 0.05)

    def test_ct_09(self):
        self.vendedor.valor_venda = 50000.01
        self.assertEqual(self.vendedor.calcular_comissao(), 0.1)