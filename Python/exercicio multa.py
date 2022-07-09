from __future__ import annotations

vel = float(input("Digite a velocidade: "))
dia = "data_de_nasc"
mes = "mes_de_nasc"
ano = "ano_de_nasc"

dia_multa = int(input("Digite a data da multa: "))
mes_multa = int(input("Digite o mes da multa: "))
ano_multa = int(input("Digite o ano da multa: "))

dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o numero do mes do nascimento: "))
ano = int(input("Digite o ano do nascimento: "))
print("Data da multa:",dia_multa,"/",mes_multa,"/",ano_multa)
print("Data de nascimento:",dia,"/",mes,"/",ano)
data = dia_multa/mes_multa/ano_multa
data_nasc = dia/mes/ano

if vel <= 60:
    print("Sem multa")
elif vel >= 61 and vel < 80:
    print("Multa pequena")
else:
    print("Multa grande")