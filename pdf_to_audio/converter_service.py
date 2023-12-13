import os
from PyPDF2 import PdfReader
from gtts import gTTS
from model import Document


class ConverterService:
    def __init__(self):
        self.language = 'en'

    def convert_pdf_to_audiobook(self, filepath: str):
        document = self.convert_pdf_to_text(filepath=filepath)
        print(document)
        self.convert_text_to_speech(document=document)

    def convert_text_to_speech(self, document: Document):
        speech_object = gTTS(text=document.text, lang=self.language, slow=False)
        speech_object.save(f'{document.filename}.mp3')

    def convert_pdf_to_text(self, filepath: str) -> Document:
        try:
            reader = PdfReader(filepath)
            filename = os.path.splitext(os.path.basename(filepath))[0]
            text = ''
            for page in reader.pages:
                text = text + ' ' + page.extract_text()
            return Document(filename=filename, text=text)
        except Exception as e:
            print(e)


