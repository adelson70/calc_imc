def calcularIMC(peso, altura):
    data = {}

    # CALCULO DO IMC
    imc = (peso/(altura**2))*10**4 #COMO ESTA EM CM O VALOR PRECISA SER DIVIDO PARA O CALCULO
    
    data['imc'] = f'{imc:.2f}'

    # GRAU DE ACORDO COM O IMC
    if imc <= 18.5:
        grau = 'abaixo do normal'

    elif 18.6 <= imc <= 24.9:
        grau = 'normal'

    elif 25 <= imc <= 29.9:
        grau = 'sobrepeso'

    elif 30 <= imc <= 34.9:
        grau = 'obesidade grau I'

    elif 35 <= imc <= 39.9:
        grau = 'obesidade grau II'

    elif imc >= 40:
        grau = 'obesidade grau III'

    data['grau'] = grau

    return data 