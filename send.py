import json,os,shelve,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from pathlib import Path



def sendBook(fromAddr,toAddr,book):
    msg = MIMEMultipart()

    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['Subject'] = "New Book"

    body = "new book"
    text = MIMEText(body, 'plain','utf-8')
    msg.attach(text)
    
    attachment = open(Path.cwd() / 'books' / book, "rb")
    att = MIMEApplication(attachment.read())
    att.add_header('Content-Disposition','attachment',filename=book)
    msg.attach(att)
    attachment.close()
    return msg

# load information
with open('info.json','r',encoding='utf-8') as jfile:
    info = json.load(jfile)
gAddr = info['gmailAddress']
password = info['gmailPassword']
kAddr = info['kindleAddress']


#login to gmail server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo_or_helo_if_needed()
server.starttls()
try:
    server.login(gAddr, password)
except:
    print("Can't login! Perhaps wrong password?")
    input()
    sys.exit()

#open sent record 
record = shelve.open('books')

for book in os.listdir('./books'):
    bookName = book[:-4]
    try :
        if (record[bookName] == 'Sent'): continue  

    except KeyError : #book not sent, send book to kindle
        print("Finding new books... Don't close the program while running!")
        print(f"Found new book: {bookName}")
        print("Sending to Kindle...")
        msg = sendBook(gAddr, kAddr, book)
        
        text = msg.as_string()
        server.sendmail(gAddr, kAddr, text)
        print("Sent successfully!")
        record[bookName] = 'Sent'

print("All books sent!")

#save record, quit server
record.close()
server.quit()

print("Press Enter to close this window...")
input()



