
import pyttsx3
shu = input('语音读：')
with open(shu, 'r', encoding='utf-8') as file:   #只读的方式打开文件
    text =file.read()
    print(text)

book = pyttsx3.init()
book.say(text)
book.runAndWait()     #这句必有，不然没有声音