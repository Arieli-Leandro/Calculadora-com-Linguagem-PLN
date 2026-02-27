import speech_recognition as sr
import webbrowser
from text_to_num import text2num
import re
import winsound
import os

# -> Código real

"""
-> Detalhes
operador tem que ser uma string, numero1 tem que ser float e o numero2 tbm

"""


def calcula_conta(operador, numero1, numero2):

    #garantindo que o operador esteja no padrão
    operador = operador.lower()

    resultado_final = 0

    match operador:

        case "soma":
            resultado_final = numero1 + numero2
        case "subtração":
            resultado_final = numero1 - numero2
        case "divisão":
            resultado_final = numero1 / numero2
        case "multiplicação":
            resultado_final = numero1 * numero2
        case _:
            print("Não foi possível realizar a conta")
            exit(1)

    return resultado_final

def ouvir_numeros(): #preciso retornar true ou false, os Números, e preciso colocar eles numa lista com while
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga o primeiro número:")
        audio = microfone.listen(source)

        try:
            resultado = microfone.recognize_google(audio, language="pt-BR", show_all=True)
            texto = resultado['alternative'][0]['transcript'].lower()

            #Converte a vírgula para um ponto, pra ficar mais fácil converter para float
            try:
                numero = float(texto.replace(",", "."))
                print("Número:", numero)
                return numero
            except ValueError:
                pass

            #Caso o usuário fale virgula ou ponto ele faz a separação do numero inteiro e depois o decimal e junta num float as duas partes 
            if "vírgula" in texto or "ponto" in texto:
                separador = "vírgula" if "vírgula" in texto else "ponto"
                partes = texto.split(separador)

                parte_inteira = text2num(partes[0].strip(), "pt")
                parte_decimal = text2num(partes[1].strip(), "pt")

                numero = float(f"{parte_inteira}.{parte_decimal}")
                print("Número:", numero)
                return numero

            #Caso mais fácil, o número formatadinho do jeito que eu preciso
            numero = text2num(texto, "pt")
            print("Número:", numero)
            return numero
        except Exception as e:
            print("Erro:", e)
            return None
    

def ouvir_operador(): #preciso retornar true ou false E TAMBÉM O OPERADOR!!!!!!!!!!!

    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        #Chama um algoritmo para reduzir os ruídos de som
        microfone.adjust_for_ambient_noise(source)

        print("Diga algum operador matemático: (soma/subtração/divisão/multiplicação)")

        operador_falado = microfone.listen(source)
        try:
            #Passa a variável para o algoritmo reconhecer o padrão
            palavra_operador = microfone.recognize_google(operador_falado, language="pt-BR")
            palavra_operador = palavra_operador.lower()

            if "soma" in palavra_operador:
                return [palavra_operador, True]
            elif "subtração" in palavra_operador:
                return [palavra_operador, True]
            elif "divisão" in palavra_operador:
                return [palavra_operador, True]
            elif "multiplicação" in palavra_operador:
                return [palavra_operador, True]
            else:
                print("Operador não reconhecido")
                winsound.Beep(440, 1000)
                palavra_operador = "Invalido"
                return [palavra_operador, False]
        except sr.UnknownValueError:
            print("Saída em formato não esperado!")
            exit(1)
            
    

if __name__ == "__main__":

    verifica_operador = False
    verifica_numeros = False

    #O Operador já está funcionando
    """while verifica_operador == False:
        parcial = ouvir_operador()
        operador = parcial[0]
        verifica_operador = parcial[1]

        if verifica_operador == True and operador != "Invalido":
            break
    """

    while verifica_numeros == False:
        ouvir_numeros()
    