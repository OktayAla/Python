from translate import Translator

translator = Translator(from_lang='Turkish',
                        to_lang='English')
sonuc = translator.translate((input()))
print(sonuc)