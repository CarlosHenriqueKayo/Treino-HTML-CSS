def obterDominio(email):
    saida = email.split("@")[-1]
    return saida
    
a = input("Digite seu email: ")

print(obterDominio(a))