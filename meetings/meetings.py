import speech_recognition as sr
import openai

# Configuração da API do OpenAI
openai.api_key = "sk-svcacct-dUvl1tuvqTjqIL-bhY844NOGzlUbrXnQCbEjLyZYPf3-cE9T3BlbkFJ4MwuGrj1KK6YZYBHoflGmXX8eyfskVlg2jCQtk0XF7jgulQA"

def capturar_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando o microfone para reduzir ruídos...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Diga algo...")
        audio = recognizer.listen(source)

        try:
            print("Reconhecendo...")
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Google Speech Recognition não conseguiu entender o áudio")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
            return None

def enviar_para_gpt(pergunta):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pergunta,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    resposta = response.choices[0].text.strip()
    return resposta

def main():
    while True:
        texto = capturar_audio()
        if texto:
            resposta = enviar_para_gpt(texto)
            print(f"Resposta do GPT: {resposta}")
        
        # Se quiser parar o loop, pode incluir uma condição aqui, como uma palavra específica
        if texto and "parar" in texto.lower():
            print("Encerrando a aplicação.")
            break

if __name__ == "__main__":
    main()
