#Programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 
dias = int (input('Quantos dias ficou com o veiculo? '))
km = int (input('Qual o km rodado? '))
sd = dias * 60.00
kmr = km * 0.15
soma = sd + kmr

print ('O total de dias é: {} \n Total de KM {}\n Valor total da locação: {:.2f}'.format (dias, km, soma))
