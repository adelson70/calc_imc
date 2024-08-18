from flask import render_template, redirect, url_for, request, jsonify
from utils import *

def configure_routes(app):

    # ROTA INICIAL
    @app.route('/', methods=['POST','GET'])
    def main():
        return render_template('index.html')
    
    # ROTA PARA CALCULAR O IMC
    @app.route('/calcular_imc', methods=['POST'])
    def calcular_imc():
        # RECEBE VALORES
        data = request.get_json()

        # DESEMPACOTA OS VALORES
        peso = float(data.get('peso'))
        altura = float(data.get('altura'))

        # FAZ O CALCULO
        result = calcularIMC(peso, altura)

        # RETORNAR PRO FRONT O RESULTADO
        return jsonify(result)