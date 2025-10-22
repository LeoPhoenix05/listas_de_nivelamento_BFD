#1
# name="Léo"
# print(f"my name is {name}")

#2
# name=input("name: ")
# age=("age: ")
# print("hi {}, you are {} years old!".format(name, age))

#3
# cidade=input("cidade: ")
# estado=input("estado: ")
# print(f"Moro em {cidade}-{estado}")

#4
# curso=input("escolha um curso: ")
# print(f"você escolheu o curso de {curso}")

#5
# filme=input("digite o nome de um filme: ")
# ano=int(input("digite o ano de lançamento do filme: "))
# print("o filme{filme}, foi lançado no ano{ano}")

#6
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# print(f"{num1} + {num2} = {num1+num2}")

#7
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# print(f"{num1} - {num2} = {num1-num2}")

#8
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# print(f"{num1} X {num2} = {num1*num2}")

#9
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# print(f"{num1} / {num2} = {num1/num2}")

#10
# num1=int(input("digite um numero: "))
# print(f"o dobro de {num1} é igual a {num1*2}")

# 11
# abaixo de 5 = reprovado
# entre 5 e 6.9 = recuperação
# 7 ou superior = aprovado
# n1=float(input('nota 1: '))
# n2=float(input('nota 2: '))
# n3=float(input('nota 3: '))

# m=(n1+n2+n3)/3
# if m<5.0:
#   print(f"sua média foi {m:.2}")
#   print('você está reprovado!')
# if m>=5.0 and m<=6.9:
#   print(f"sua média foi {m:.2}")
#   print('você está em recuperação!')
# if m>=7.0:
#   print(f"sua média foi {m:.2}")
#   print('você está aprovado!')

#12
# ano_atual=int(input("digite o ano atual:  "))
# ano_nascimento=int(input("digite o ano de nascimento: "))
# print(f"nós estamos no ano {ano_atual} e você nasceu no ano de {ano_nascimento}, sendo assim, você tem {ano_atual-ano_nascimento} anos.")

#13
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# de 25 ate 30: sobrepeso
# de 30 ate 40: obeso
# acima de 40: obesidade morbida
# peso=float(input('digite seu peso: '))
# altura=float(input('digite sua altura: '))
# imc=peso/(altura**altura)

# if imc<18.5:
#     print(f"imc = {imc:.1f}")
#     print('você está abaixo do peso!')
# elif imc>=18.5 and imc<25:
#     print(f"imc = {imc:.1f}")
#     print('você está no peso ideal!')
# elif imc>=25 and imc<30:
#     print(f"imc = {imc:.1f}")
#     print('você está sobrepeso!')
# elif imc>=30 and imc<40:
#     print(f"imc = {imc:.1f}")
#     print('você está obeso!')
# else:
#     print(f"imc = {imc:.1f}")
#     print('você está com obesidade morbida!')
    # >>>>>OU<<<<<
    # ta dando erro com match case:
# match imc:
    # case '<18.5':
    #     print(f"imc = {imc:.1f}")
    #     print('abaixo do peso!')
    # case '>=18.5' | '<25':
    #     print(f"imc = {imc}")
    #     print('peso ideal!')
    # case '>=25' | 'imc<30':
    #     print(f"imc = {imc}")
    #     print('sobrepeso!')
    # case '>=30' | 'imc<40':
    #     print(f"imc = {imc}")
    #     print('obeso!')
    # case '>40':
    #     print(f"imc = {imc}")
    #     print('obesidade morbida!')

#14
# dias=int(input("digite uma quantidade de dias: "))
# horas=dias*24
# print(f"{dias} equivalem a {horas} horas de acordo com o calendario terrestre!")

#15
# produto=input("escolha um produto: ")
# preço=float(input("qual o preço do produto na prateleira? "))
# preçof=preço-(preço*10)/100
# print(f"{produto} está com 10% de desconto, seu valor atual é de {preçof:.2f}")
    
#16
# num1=int(input("esolha um numero: "))
# num2=int(input("escolha outro numero: "))
#print(f"o numero {num1} é maior que o numero {num2}")if num1>num2 else print(f"o numero {num1} é menor que o numero {num2}")
# if num1>num2:
#     print(f"o numero {num1} é maior que o numero {num2}")
# elif num2>num1:
#     print(f"o numero {num2} é maior que o numero {num1}")
# else:
#     print(f"o numero {num1} é igual ao numero {num2}")

#17
# num1=int(input("por favor,esolha um numero: "))
# num2=int(input("agora escolha outro numero: "))
# if num1<num2:
#     print(f"o numero {num1} é menor que o numero {num2}")
# elif num2<num1:
#     print(f"o numero {num2} é menor que o numero {num1}")
# else:
#     print(f"o numero 1: {num1} é igual ao numero 2: {num2}")

#18
# num1=int(input("esolha um numero: "))
# num2=int(input("escolha outro numero: "))
# num3=int(input("agora escolha um terceiro numero: "))
# print(f"{num1} + {num2} + {num3} é igual a {num1+num2+num3}")

#19
# num1=int(input("digite um numero: "))
# num2=int(input("digite outro numero: "))
# num3=int(input("e agora mais um numero: "))
# print(f"a media dos 3 numeros é igual a {(num1+num2+num3)/3:.2f}")

#20
# num=int(input("digite um numero: "))
# if num%2==0:
#     print(f"{num} é um numero par!")
# else:
#     print(f"{num} é um numero impar")

#21
# jogador1=input("jogador 1: ")
# jogador2=input("jogador 2: ")
# jogador3=input("jogador 3: ")
# jogador4=input("jogador 4: ")
# time1=input("time 1: ")
# time2=input("time 2: ")
# time3=input("time 3: ")
# time4=input("time 4: ")
# print(f"""
#       o jogo será amanhã e os jogadores são: 
#       o jogador {jogador1} irá jogar no time {time1}
#       o jogador {jogador2} irá jogar no time {time2}
#       o jogador {jogador3} irá jogar no time {time3}
#       o jogador {jogador4} irá jogar no time {time4}
      
#       """)

#22
# livro=input("me fala um livro pra ver se ja li: ")
# print(f"estou lendo {livro} essa semana!")

#23
# nome1=input("qual a profissão?: ")
# profissão1=input("qual a profissão?: ")
# empresa1=input("qual a empresa?:")
# nome2=input("qual a empresa?:")
# profissão2=input("qual a profissão?: ")
# empresa2=input("qual a empresa?:")
# nome3=input("qual a profissão?: ")
# profissão3=input("qual a profissão?: ")
# empresa3=input("qual a empresa?:")
# nome4=input("qual a empresa?:")
# profissão4=input("qual a profissão?: ")
# empresa4=input("qual a empresa?:")
# print("""
# meu nome é {nome1} e trabalho como {profissão1} na empresa {empresa1}
# meu nome é {nome2} e eu trabalho como {profissão1} na empresa {empresa2}
# meu nome é {nome3} e trabalho como {profissão1} na empresa {empresa3}
# meu nome é {nome4} e trabalho como {profissão1} na empresa {empresa4}
# """)

#24
# cor=input("Qual a sua cor favorita? ")
# print(f"Minha cor favorita é {cor}")

#25
# animal1=input("qual o seu animal?: ")
# nome1=input("qual o nome do seu animal?: ")
# animal2=input("qual o seu animal?: ")
# nome2=input("qual o nome do seu animal?: ")
# animal3=input("qual o seu animal?: ")
# nome3=input("qual o nome do seu animal?: ")
# animal4=input("qual o seu animal?: ")
# nome4=input("qual o nome do seu animal?: ")
# print(f"meu animal de estimação é um(a) {animal1} e seu nome é {nome1}")
# print(f"meu animal de estimação é um(a) {animal2} e seu nome é {nome2}")
# print(f"meu animal de estimação é um(a) {animal3} e seu nome é {nome3}")
# print(f"meu animal de estimação é um(a) {animal4} e seu nome é {nome4}")

#26
# nome1=input("Qual o seu nome? ")
# comida1=("Qual a sua comida favorita? ")
# nome2=input("Qual o seu nome? ")
# comida2=("Qual a sua comida favorita? ")
# nome3=input("Qual o seu nome? ")
# comida3=("Qual a sua comida favorita? ")
# nome4=input("Qual o seu nome? ")
# comida4=("Qual a sua comida favorita? ")
# print(f"Seu nome é {nome1} e você gosta de comer {comida1}")
# print(f"Seu nome é {nome2} e você gosta de comer {comida2}")
# print(f"Seu nome é {nome3} e você gosta de comer {comida3}")
# print(f"Seu nome é {nome4} e você gosta de comer {comida4}")

#27
# cantor1=input("Diga o nome de um cantor? ")
# musica1=("Qual nome de uma musica? ")
# cantor2=input("Diga o nome de um cantor? ")
# musica2=("Qual nome de uma musica? ")
# cantor3=input("Diga o nome de um cantor? ")
# musica3=("Qual nome de uma musica? ")
# cantor4=input("Diga o nome de um cantor?  ")
# musica4=("Qual nome de uma musica? ")
# print(f"O(a) cantor(a) {cantor1} canta a musica {musica1}")
# print(f"O(a) cantor(a) {cantor2} canta a musica {musica2}")
# print(f"O(a) cantor(a) {cantor3} canta a musica {musica3}")
# print(f"O(a) cantor(a) {cantor4} canta a musica {musica4}")

#28
# cidade=input("Diz o nome de uma cidade: ")
# ano=input("Escolhe um ano: ")
# print(f"E num é que eu visitei {cidade} em {ano} msm")

#29
# escola=input("Escreva o nome da escola: ")
# curso=input("Agora escreva o nome de um curso: ")
# print(f"Eu estudo {curso} na escola {escola}")

#30
# nome=input("me diz o nome de um amigo: ")
# apelido=input("me fala um apelido: ")
# print(f"Meu amigo {nome} também é con hecido como {apelido}")