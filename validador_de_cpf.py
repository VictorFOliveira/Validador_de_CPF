def validador(str):
# Para validar o CPF, vamos precisar dos primeiros 9 números para realização do calculo.
# Foi realizado o tratamento da string, removendo pontos, e traços.
    cpf_usuario = input('Digite seu CPF: ').replace('.','').replace('-', '')
    cpf_nove_digitos = cpf_usuario[:9]

    contagem_regressiva_1 = 10
    resultado_digito_1 = 0 

# Para o calculo, multiplicamos os 9 digitos do CPF
# Por uma contagem regressiva de 10 a 2, isso o primeiro digito

    for digito_1 in cpf_nove_digitos:
        resultado_digito_1 += int(digito_1) * contagem_regressiva_1
        contagem_regressiva_1 -= 1

# Agora devemos multiplicar o resultado por 10, e depois o resto da divisão por 11.
    primeiro_digito =  (resultado_digito_1 * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <=9 else 0

# Se o primeiro digito for menor ou igual a nove, ele recebe o proprio digito.
# Se o primeiro digito for maior do que 9, ele recebe 0.

# ------------------- Digito 2 --------------------------

# Nesse passo, o cpf_nove_digitos recebe o primeiro digito.
# E a contagem regressiva começa de 11 até 2.
    contagem_regressiva_2 = 11
    resultado_digito_2 = 0
    cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)

    for digito_2 in cpf_dez_digitos:
        resultado_digito_2 += int(digito_2) * contagem_regressiva_2
        contagem_regressiva_2 -= 1

# Os próximos passos são iguais ao primeiro digito

    segundo_digito = (resultado_digito_2 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0


    cpf_validado = f'{cpf_nove_digitos}{primeiro_digito}{segundo_digito}'

    if cpf_validado == cpf_usuario:
       return print('CPF VALIDADO')
    else:
       return print('CPF INVÁLIDO')


validador(str)
