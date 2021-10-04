#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200 Mk
# e R$0.45 para viagens mais longas.

km = float(input('Qual a distância da viagem em Km: '))
if km <= 200:
    print('Viagem de até 200 KM. O valor da passagem é R$ {:.2f}'.format(km * 0.5))
else:
    print('Sua viagem é de mais de 200 km. O valor da passagem é R${:.2f}'.format(km * 0.45))


