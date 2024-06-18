from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

    translated_text = translate_text(text, target_language)
    print(f"Translated text: {translated_text}")