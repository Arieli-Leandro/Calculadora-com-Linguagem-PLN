🎙️ Calculadora por Voz (Python)

Calculadora em Python que realiza operações matemáticas básicas a partir de comandos de voz em português (pt-BR).
O usuário fala o operador e os números, e o sistema reconhece, converte e calcula automaticamente.

---

🧠 Processamento de Linguagem Natural (PLN)

Este projeto foi desenvolvido como parte de estudos sobre Processamento de Linguagem Natural (PLN).

A aplicação utiliza técnicas básicas de PLN para:

- Converter fala em texto (Speech-to-Text)
- Interpretar comandos em linguagem natural
- Identificar operadores matemáticos a partir de palavras faladas
- Converter números escritos por extenso em valores numéricos

O reconhecimento de padrões linguísticos, a normalização do texto (lowercase, tratamento de vírgula/ponto) e a conversão semântica de números demonstram a aplicação prática de conceitos fundamentais de PLN.
O projeto serviu como exercício prático para compreender como sistemas interpretam linguagem humana e a transformam em instruções computacionais.

---
🚀 Funcionalidades

- Reconhecimento de voz com SpeechRecognition
- Conversão de números falados por extenso (text2num)

---

📦 Instalação
git clone "https://github.com/Arieli-Leandro/calcula_por_voz.git"
cd calcula_por_voz
pip install SpeechRecognition text2num pyaudio
▶️ Execução
python calcula_por_voz.py

O programa irá:
- Solicitar o operador matemático.
- Solicitar os números.
- Exibir o resultado da operação.

---

⚠️ Observações

- Requer conexão com internet (Google Speech Recognition).
- Atualmente compatível com Windows.
- Operações trigonométricas ainda não implementadas.
