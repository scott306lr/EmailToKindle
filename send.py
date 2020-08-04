import json,os,shelve,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from pathlib import Path

def sendmail(gAddr,kAddr,recording):
    #build email
    msg = MIMEMultipart()
    msg['From'] = gAddr
    msg['To'] = kAddr
    msg['Subject'] = "New Book"
    body = "new book"
    text = MIMEText(body, 'plain','utf-8')
    msg.attach(text)

    #attach books
    for book in recording :
        attachment = open(Path.cwd() / 'books' / book, "rb")
        att = MIMEApplication(attachment.read())
        att.add_header('Content-Disposition','attachment',filename=book)
        msg.attach(att)
        attachment.close()
        #print(f"{book} Attached to mail.")

    #send books to kindle
    text = msg.as_string()
    print("Sending mail to kindle...")
    #server.sendmail(gAddr, kAddr, text)
    print("All books sent!")

    for sentBook in recording :
        record[sentBook] = 'Sent'
    record.close()



# load information
with open('info.json','r',encoding='utf-8') as jfile:
    info = json.load(jfile)
gAddr = info['gmailAddress']
password = info['gmailPassword']
kAddr = info['kindleAddress']

#open sent record 
record = shelve.open('books')
print("Finding new books... Don't close while program is running!")

new = False
recording = []
for book in os.listdir('./books'): 
    try :
        if (record[book] == 'Sent'): continue  

    #book not sent. Attach book to mail
    except KeyError :  
        new = True
        print(f"Found new book: {book}")
        recording.append(book)
        

if new == True :
    #login to gmail server
    print('\nLogging in to gmail server......', end='')
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.login(gAddr, password)
        print('Logged in!')
    except:
        print("Can't login! Perhaps wrong password?")
        input()
        sys.exit()

    #generate email and send to kindle
    sendmail(gAddr,kAddr,recording)
    #exit gmail 
    server.quit()
    
else :
    print("All books sent already!")

print("\n\nPress Enter to close this window...")
input()



