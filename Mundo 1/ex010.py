#Converta reais para dolar usando a contação de US$1,00 para R$ 3,27
c = float (input('Digite quantos reais você deseja converter, utilize ponto para centavos, por exemplo R$ 5.55 ou R$ 10.00 \nValor R$  '))
dolar = (3.27)
conversao = (c / dolar)
print ('Com o valor R${} apos a conversão você tem US${:.2f}' .format (c, conversao) )
