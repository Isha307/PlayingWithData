mport pyttsx3
import PyPDF2

book = open('oops_python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
speaker.setProperty('volume', 0.7)

for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
