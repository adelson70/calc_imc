def calcularIMC(peso, altura):
    imc = (peso/(altura**2))
    return f'{imc:02d}'