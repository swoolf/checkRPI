#A Script to check if RPIw's are in stock at MicroCenter
#Sam Woolf, 2016

from bs4 import BeautifulSoup

import requests
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import smtplib
import time

######Add your info here####
MicroCenterUrl = "http://www.microcenter.com/product/475267/Zero_W" #currently for Cambridge

#from address (needs to be gmail, make a junk one)
#you'll likely need to give permission the first time
fromEmail = "junkexample@gmail.com"
fromPW = "password"

#to address (can be anything)
toEmail = "you@email.com"

############################


while(True):
    r  = requests.get(MicroCenterUrl)

    data = r.text
    soup = BeautifulSoup(data, "html.parser")


    myDivs = soup.find_all("span", {"class":"inventoryCnt"})
    Qty=myDivs[0].text

    if 'in stock' in Qty.lower():
        print 'yes!'
        fromaddr = "you@gmail.com"
        toaddr = toEmail
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "RPIw: A friendly note"

        body = Qty + ', Raspberry Pi Zero W, Woohoo!'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromEmail, fromPW)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    elif 'sold out' in Qty.lower():
#        print 'sold out'
        pass
    else:
#        print 'uhoh...'
        pass

    time.sleep(30)



