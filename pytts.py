import pyttsx3 as tt
speaker = tt.init()
import PyPDF2

book = open("homeacrordrunified18_2018.pdf", 'rb')
reader = PyPDF2.PdfFileReader(book)
for i in range(reader.numPages):
    page = reader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()