import speech_recognition as sr
from text_to_num import text2num
import math
import winsound

OPERACAO_UNARIA = 1
OPERACAO_BINARIA = 2

def configura_microfone(microfone):

    microfone.pause_threshold = 1.2
    microfone.energy_threshold = 300
    microfone.dynamic_energy_threshold = True

    return

#Vai decidir os casos de divisão e exponenciação
def decisao_de_caso(numero1, numero2, operador):

    verifica_decisao = False

    microfone = sr.Recognizer()
    configura_microfone(microfone)

    #Só vai parar se realmente conseguirmos extrair a decisão
    while verifica_decisao == False:

        match operador:
            case "subtração":
                with sr.Microphone() as source:
                    microfone.adjust_for_ambient_noise(source)

                    print(f"Opção 1: Subtrair {numero1} por {numero2}")
                    print(f"Opção 2: Subtrair {numero2} por {numero1}")
                    print("Por favor diga Opção 1 ou Opção 2")

                    decisao_gravada = microfone.listen(source)

                    try:
                        #Passa a variável para o algoritmo reconhecer o padrão
                        decisao_final = microfone.recognize_google(decisao_gravada, language="pt-BR")
                        decisao_final = decisao_final.lower()

                        if decisao_final == "opção 1" or decisao_final == "opção um":
                            verifica_decisao = True
                            caso_final = 1
                        elif decisao_final == "opção 2" or decisao_final == "opção dois":
                            verifica_decisao = True
                            caso_final = 2
                        else:
                            print("Diga apenas uma das opções válida!")
                    except sr.UnknownValueError:
                        print("Decisão não reconhecida")
                        winsound.Beep(440, 1000)
            case "divisão":

                with sr.Microphone() as source:
                    microfone.adjust_for_ambient_noise(source)

                    print(f"Opção 1: Dividir {numero1} pelo {numero2}")
                    print(f"Opção 2: Dividir {numero2} pelo {numero1}")
                    print("Por favor diga Opção 1 ou Opção 2")

                    decisao_gravada = microfone.listen(source)

                    try:
                        #Passa a variável para o algoritmo reconhecer o padrão
                        decisao_final = microfone.recognize_google(decisao_gravada, language="pt-BR")
                        decisao_final = decisao_final.lower()

                        if decisao_final == "opção 1" or decisao_final == "opção um":
                            verifica_decisao = True
                            caso_final = 1
                        elif decisao_final == "opção 2" or decisao_final == "opção dois":
                            verifica_decisao = True
                            caso_final = 2
                        else:
                            print("Diga apenas uma das opções válida!")
                    except sr.UnknownValueError:
                        print("Decisão não reconhecida")
                        winsound.Beep(440, 1000)
            case "exponenciação":
                with sr.Microphone() as source:
                    microfone.adjust_for_ambient_noise(source)

                    print(f"Opção 1: {numero1} elevado à {numero2} ({numero1} - base, {numero2} - expoente)")
                    print(f"Opção 2: {numero2} elevado à {numero1} ({numero2} - base, {numero1} - expoente)")
                    print("Por favor diga Opção 1 ou Opção 2")

                    decisao_gravada = microfone.listen(source)

                    try:
                        #Passa a variável para o algoritmo reconhecer o padrão
                        decisao_final = microfone.recognize_google(decisao_gravada, language="pt-BR")
                        decisao_final = decisao_final.lower()

                        if decisao_final == "opção 1" or decisao_final == "opção um":
                            verifica_decisao = True
                            caso_final = 1
                        elif decisao_final == "opção 2" or decisao_final == "opção dois":
                            verifica_decisao = True
                            caso_final = 2
                        else:
                            print("Diga apenas uma das opções válida!")
                    except sr.UnknownValueError:
                        print("Decisão não reconhecida")
                        winsound.Beep(440, 1000)

        #Interrompe o laço a partir do momento que foi reconhecido uma das opções válidas
        if verifica_decisao == True:
            break

    #Caso 1: primeiro pelo segundo
    #Caso 2: segundo pelo primeiro
    #Ambos casos se encaixam nas 2 requisições, sendo tratado (num1 == num2) na função exterior
    return caso_final

#Para garantir que funções como sqrt vão receber um número positivo
def transforma_positivo(numero):

    numero = numero * (-1)
    return numero

def calcula_conta(operador, qtd_numeros, lista_numeros):

    #Caso 1: Normal num1 op num2
    houve_troca = False

    #Utilizando variáveis para o caso de um dia precisar mudar
    primeiro_numero = lista_numeros[0]
    segundo_numero = lista_numeros[1]

    #Estou utilizando a string operador aqui só para poder fazer um match case p/ calcular as contas
    #garantindo que o operador esteja no padrão
    operador = operador.lower()

    #Aqui que eu pergunto os casos de divisão e exponenciação
    if qtd_numeros == 1:
        match operador:
            case "seno":
                resultado = math.sin(primeiro_numero)
            case "cosseno":
                resultado = math.cos(primeiro_numero)
            case "raiz quadrada":

                if primeiro_numero < 0:
                    primeiro_numero = transforma_positivo(primeiro_numero)
                resultado = math.sqrt(primeiro_numero)

            case "raiz cúbica":
                resultado = math.cbrt(primeiro_numero)
            case "tangente":
                resultado = math.tan(primeiro_numero)
    else:
        match operador:
            case "soma":
                resultado = primeiro_numero + segundo_numero
            case "subtração":

                if primeiro_numero == segundo_numero:
                    resultado = 0

                opcao_subtracao = decisao_de_caso(primeiro_numero, segundo_numero, operador)

                if opcao_subtracao == 1:
                    resultado = primeiro_numero - segundo_numero
                elif opcao_subtracao == 2:
                    houve_troca = True
                    resultado = segundo_numero - primeiro_numero
            case "divisão":

                if primeiro_numero == segundo_numero:
                    resultado = 1

                opcao_divisao = decisao_de_caso(primeiro_numero, segundo_numero, operador)

                if opcao_divisao == 1: 
                    resultado = primeiro_numero / segundo_numero
                elif opcao_divisao ==2:
                    houve_troca = True
                    resultado = segundo_numero / primeiro_numero
            case "multiplicação":
                resultado = primeiro_numero * segundo_numero
            case "exponenciação":
                
                if primeiro_numero == segundo_numero:
                    resultado = math.pow(primeiro_numero, primeiro_numero)

                opcao_exponenciacao = decisao_de_caso(primeiro_numero, segundo_numero, operador)

                if opcao_exponenciacao == 1:
                    resultado = math.pow(primeiro_numero, segundo_numero)
                elif opcao_exponenciacao == 2:
                    houve_troca = True
                    resultado = math.pow(segundo_numero, primeiro_numero)

            case _:
                print("Falha na execução da conta!")
                exit(1)

    #Caso houver troca entre num1 e num2, passa pra main p/ exibir corretamente
    return [resultado, houve_troca]


def ouvir_numeros(qtd_numero): 

    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    configura_microfone(microfone)

    lista_numeros = []

    with sr.Microphone() as source:

        for i in range(qtd_numero):
            microfone.adjust_for_ambient_noise(source)

            print(f"Diga o {(i + 1)} número:")
            audio = microfone.listen(source)

            try:
                resultado = microfone.recognize_google(audio, language="pt-BR", show_all=True)
                texto = resultado['alternative'][0]['transcript'].lower()

                #Converte a vírgula para um ponto, pra ficar mais fácil converter para float
                try:
                    numero = float(texto.replace(",", "."))
                    lista_numeros.append(numero)
                    continue
                except ValueError:
                    pass

                #Caso o usuário fale virgula ou ponto ele faz a separação do numero inteiro e depois o decimal e junta num float as duas partes 
                if "vírgula" in texto or "ponto" in texto:
                    separador = "vírgula" if "vírgula" in texto else "ponto"
                    partes = texto.split(separador)

                    parte_inteira = text2num(partes[0].strip(), "pt")
                    parte_decimal = text2num(partes[1].strip(), "pt")

                    numero = float(f"{parte_inteira}.{parte_decimal}")
                    lista_numeros.append(numero)
                    continue
                    

                #Caso mais fácil, o número formatadinho do jeito que eu preciso
                numero = text2num(texto, "pt")
                lista_numeros.append(numero)
                continue
            except Exception as x:
                print("Erro:", x)
                return [False, []]
                
    return [True, lista_numeros]    

def ouvir_operador():

    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    configura_microfone(microfone)

    with sr.Microphone() as source:

        #Chama um algoritmo para reduzir os ruídos de som
        microfone.adjust_for_ambient_noise(source)

        #Alterar para um menu de exibição
        print("Operadores disponíveis:")
        print("| Soma | Subtração | Divisão  | Multiplicação | Exponenciação |")
        print("| Seno |  Cosseno  | Tangente | Raiz Quadrada |  Raiz Cúbica  |")
        print("Escolha um Operador:")

        operador_falado = microfone.listen(source)
        try:
            #Passa a variável para o algoritmo reconhecer o padrão
            palavra_operador = microfone.recognize_google(operador_falado, language="pt-BR")
            palavra_operador = palavra_operador.lower()

            verificador = True
            #Tem que retornar (operador, verificador, binario/unario)
            match palavra_operador:
                case "soma":
                    tipo_operacao = OPERACAO_BINARIA
                case "subtração":
                    tipo_operacao = OPERACAO_BINARIA
                case "divisão":
                    tipo_operacao = OPERACAO_BINARIA
                case "multiplicação":
                    tipo_operacao = OPERACAO_BINARIA
                case "exponenciação":
                    tipo_operacao = OPERACAO_BINARIA
                case "seno":
                    tipo_operacao = OPERACAO_UNARIA
                case "cosseno":
                    tipo_operacao = OPERACAO_UNARIA
                case "tangente":
                    tipo_operacao = OPERACAO_UNARIA
                case "raiz quadrada":
                    tipo_operacao = OPERACAO_UNARIA
                case "raiz cúbica":
                    tipo_operacao = OPERACAO_UNARIA
                case _:
                    print("Operador não reconhecido")
                    winsound.Beep(440, 1000)
                    palavra_operador = None
                    verificador = False
                    tipo_operacao = -1
        except sr.UnknownValueError:
            print("Saída em formato não esperado!")
            winsound.Beep(440, 1000)
            palavra_operador = None
            verificador = False
            tipo_operacao = -1
        
    return [palavra_operador, verificador, tipo_operacao]
            
#a partir do operador ele retorna seu respectivo símbolo
def get_symbol(operador):

    match operador:
        case "soma":
            op_symbol = "+"
        case "subtração":
            op_symbol = "-"
        case "divisão":
            op_symbol = "/"
        case "multiplicação":
            op_symbol = "*"
        case "exponenciação":
            op_symbol = "**"
        case "seno":
            op_symbol = "sen"
        case "cosseno":
            op_symbol = "cos"
        case "tangente":
           op_symbol = "tan"
        case "raiz quadrada":
            op_symbol = "√"
        case "raiz cúbica":
            op_symbol = "∛"
        case _:
            print("Símbolo não encontrado!")
            exit(1)


    return op_symbol

if __name__ == "__main__":

    verifica_operador = False
    verifica_numeros = False

    while verifica_operador == False:
        parcial = ouvir_operador()
        operador_conta = parcial[0]
        verifica_operador = parcial[1]
        qtd_numeros = parcial[2]

        if verifica_operador == True and verifica_operador != False:
            break
    
    while verifica_numeros == False:

        parcial_numerico = ouvir_numeros(qtd_numeros)
        verifica_numero_valido = parcial_numerico[0]
        lista_numeros = parcial_numerico[1]

        if verifica_numero_valido == True:
            verifica_numeros = True

        if verifica_numeros == True and verifica_numero_valido != False:
            break

    parcial_resultado = calcula_conta(operador_conta, qtd_numeros, lista_numeros)

    resultado_conta = parcial_resultado[0]
    troca_posicao = parcial_resultado[1]
    symbol = get_symbol(operador_conta)

    if qtd_numeros == 1:
        print(f"O resultado da conta {symbol}({lista_numeros[0]})  = {resultado_conta:.2f}")
    else:

        if troca_posicao == True:
            #Se trocou de posição: o primeiro_numero é lista_numeros[1], o segundo_numero é lista_numeros[0]
            auxiliar = lista_numeros[0]
            lista_numeros[0] = lista_numeros[1]
            lista_numeros[1] = auxiliar

        print(f"O resultado da conta {lista_numeros[0]} {symbol} {lista_numeros[1]} = {resultado_conta:.2f}")
