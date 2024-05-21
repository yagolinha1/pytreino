import metodo

a = int(input("digite a: "))
b = int(input("digite b: "))


op = int(input("1-soma\n2-subtração:\ndigite uma opção: "))
if op==1:
    print(metodo.somaValores(a, b))
elif op==2: 
    print(metodo.subtraiValores(a, b))
else:
    print("opção invalida")

metodo.fim()  
          