
from google_trans_new import google_translator
translator = google_translator()


def gtranslate(query, dest='en'):
    value = translator.translate(query, lang_tgt=dest)

    return value


# print(gtranslate('hola'))
