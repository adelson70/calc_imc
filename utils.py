def calcularIMC(peso, altura):
    imc = (peso/(altura**2))*10**4 #COMO ESTA EM CM O VALOR PRECISA SER DIVIDO PARA O CALCULO
    print(imc, peso, altura)
    return f'{imc:.2f}'