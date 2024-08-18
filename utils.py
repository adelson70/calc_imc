def calcularIMC(peso, altura):
    data = {}

    # CALCULO DO IMC
    imc = (peso/(altura**2))*10**4 #COMO ESTA EM CM O VALOR PRECISA SER DIVIDO PARA O CALCULO
    
    data['imc'] = f'{imc:.2f}'

    # GRAU DE ACORDO COM O IMC
    data['grau'] = None
    
    print(data)

    return data 