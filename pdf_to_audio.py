from PyPDF2 import PdfReader
from gtts import gTTS

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""

        for page_number in range(len(reader.pages)): 
            page = reader.pages[page_number]
            text += page.extract_text()
    return text

def text_to_audio(text, audio_path):
   tts = gTTS(text)
   tts.save(audio_path)

def pdf_to_audio(pdf_path, audio_path):
    text = pdf_to_text(pdf_path)
    text_to_audio(text, audio_path)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    audio_path = input("Enter the path to save the audio file: ")

pdf_to_audio(pdf_path, audio_path)