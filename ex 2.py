''' saudade da minha professora maravilhosa'''
qnt = 1
time = 1
jovem = 0
pesados = 0
totalAltura = 0
totalIdade = 0

while time < 6:
    while qnt < 12:
        print("-=Time ", time, "=-", sep="")
        print("-=|Dados do ", qnt, "º Jogador|=-", sep="")
        idade = int(input("Insira a idade do jogador. "))
        while idade < 14 or idade > 35:
            print("Idade inválida.")
            idade = int(input("Insira a idade do jogador. "))
        if idade < 18:
            jovem += 1
        totalIdade += idade
        mediaIdade = totalIdade/11
        altura = float(input("Insira a altura do jogador. "))
        while altura < 1.6 or altura > 2.0:
            print("Altura inválida.")
            altura = float(input("Insira a altura do jogador. "))
        totalAltura += altura
        peso = float(input("Insira o peso do jogador. "))
        while peso < 60 or peso > 100:
            print("Insira um peso válido.")
            peso = float(input("Insira o peso do jogador. "))
        if peso > 80:
            pesados += 1
        print()
        qnt += 1
    print("A média da idade do ", time, "º time é ", mediaIdade, ".", sep="")
    print()
    time += 1
    totalIdade = 0
    qnt = 1

mediaAltura = totalAltura / 55
porcentPesados = (pesados / 55)*100
print("A quantidade de jogadores com idade inferior a 18 anos é ", jovem, ".", sep="")
print("A média de altura de todos os jogadores do campeonato é ", mediaAltura, ".", sep="")
print("A porcentagem de jogadores com peso acima dos 80kg é ", porcentPesados, ".", sep="")