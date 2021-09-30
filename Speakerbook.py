import pyttsx3
import PyPDF2

sach=open("GT học phần Triết học MLN (K) Tr đầu -Tr59.pdf", "rb")
pdfReader = pyPDF2.PdfFileReader(sach)
pages=pdfReader.numpages
print(pages)
bot=pyttsx3.init() 
voice = bot.getProperty('voices')
bot.setPorperty('voice', voice[0].id)
for num in range(50,60,pages):
  page=pdfReader.getpage(num)
  text=page.extractText()
  bot.say(text) 
  bot.runAndWait()
