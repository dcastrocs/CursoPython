print('Calculadora IMC')
print('Por favor digite seus dados usando ponto')
print('Exemplo: peso 85.00')
print('exemplo: altura 1.85')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('imc {:.2f}'.format(imc))
if imc < 18.5:
    print('Seu IMC atual é {:.2f}'.format(imc))
    print('De acordo com a tabela adotada pela OMS para calcular o peso ideal de cada pessoa,você esta abaixo do peso.')
elif imc >= 18.5 and imc <= 25.00:
    print('Seu IMC atual é {:.2f}'.format(imc))
    print('De acordo com a tabela adotada pela OMS para calcular o peso ideal de cada pessoa,você esta no peso ideal')
elif imc >25 and imc <= 30:
    print('Seu IMC atual é {:.2f}'.format(imc))
    print('De acordo com a tabela adotada pela OMS para calcular o peso ideal de cada pessoa,você esta com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Seu IMC atual é {:.2f}'.format(imc))
    print('De acordo com a tabela adotada pela OMS para calcular o peso ideal de cada pessoa,você esta com obesidade')
else:
    print('Seu IMC atual é {:.2f}'.format(imc))
    print('De acordo com a tabela adotada pela OMS para calcular o peso ideal de cada pessoa,você esta com obesidade mórbida')
