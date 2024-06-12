import PyPDF2
import pyttsx3

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

def text_to_audio(text, audio_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

def pdf_to_audio(pdf_path, audio_path):
    text = pdf_to_text(pdf_path)
    text_to_audio(text, audio_path)

pdf_path = ""
audio_path = ""

pdf_to_audio(pdf_path, audio_path)