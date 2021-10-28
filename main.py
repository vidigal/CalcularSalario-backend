from flask import Flask, request, jsonify
from flask_cors import CORS


from vendedor import Vendedor

api = Flask(__name__)
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})


if __name__ == "__main__":
    api.run(debug=True)

@api.route('/api')
def ola_mundo():
    return 'Olá mundo!'

@api.route('/api/calcular_valor_receber/<nome>/<meses_contratado>/<valor_venda>', methods=['GET'])
def calcular_valor_receber(nome, meses_contratado, valor_venda):
    vendedor = Vendedor(nome, int(meses_contratado), float(valor_venda))
    perc_comissao = vendedor.calcular_comissao()
    salario_base = vendedor.calcular_salario_base()
    valor_receber = vendedor.calcular_valor_receber()

    return jsonify({'perc_comissao': perc_comissao, 'salario_base': salario_base, 'valor_receber': valor_receber})
