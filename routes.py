from flask import render_template, redirect, url_for, request
from utils import *

def configure_routes(app):

    # ROTA INICIAL
    @app.route('/', methods=['POST','GET'])
    def main():
        return render_template('index.html')
    
    # ROTA PARA CALCULAR O IMC
    @app.route('/calcular_imc', methods=['POST'])
    def calcular_imc():
        data = request.get_json()
        peso = data.get('peso')
        altura = data.get('altura')

        result = calcularIMC(peso, altura)

        print(result)

        return data