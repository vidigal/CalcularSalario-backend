from vendedor import Vendedor

nome = 'Victor'
meses_contratrado = 8
valor_venda = 100.0

vendedor = Vendedor(nome, meses_contratrado, valor_venda)

perc_comissao = vendedor.calcular_comissao()
salario_base = vendedor.calcular_salario_base()
valor_receber = vendedor.calcular_valor_receber()

print("=================================================================")
print(f"Funcionário {nome}")
print(f"Tempo de contratação: {meses_contratrado} meses")
print(f"Valor vendido: R$ {valor_venda}")
print("------------------------------------------------------------------")
print(f"Percentual de comissão: {perc_comissao}%")
print(f"Salário base: R$ {salario_base}")
print(f"Valor a receber: R$ {valor_receber}")
print("=================================================================")


