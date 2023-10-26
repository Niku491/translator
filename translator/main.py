from googletrans import Translator

# create a Translator object
translator = Translator()

#text to be translated
text = "Hello, how are you?"

#translate the text into another language
translated_text = translator.translate(text,dest="hindi")

#print the translated text
print(f"original text: {text}")
print(f"Translated text: {translated_text.text}")