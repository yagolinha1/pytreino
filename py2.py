def imc(peso, est):
    res = peso / altura**2
    return(res)

def despedida():
    print("obrigado por usar este programa!")
    print("ATE LOGOOOO!")


peso = float(input("digite o peso da pessoa, em kg: "))
altura = float(input("digite a estrutura da pessoa, em m: "))
print("o imc é", imc(peso, altura), "kg/m²")
despedida()