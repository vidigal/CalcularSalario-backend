class Vendedor:

    def __init__(self, nome, meses_contratado, valor_venda):
        self.name = nome
        self.meses_contratado = meses_contratado
        self.valor_venda = valor_venda

    def calcular_salario_base(self):
        if self.meses_contratado < 12:
            return 1500.0
        elif self.meses_contratado > 12 and self.meses_contratado < 24:
            return 2000.0
        elif self.meses_contratado > 24 and self.meses_contratado < 36:
            return 2500.0
        elif self.meses_contratado > 36:
            return 3000.0

    def calcular_comissao(self):
        if self.valor_venda < 10000.0:
            return 0.03
        elif self.valor_venda > 1000.0 and self.valor_venda < 50000.0:
            return 0.05
        elif self.valor_venda > 500000:
            return 0.1

    def calcular_valor_receber(self):
        comissao = self.valor_venda * self.calcular_comissao()
        salario_base = self.calcular_salario_base()
        return salario_base + comissao

