# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/27/2018 3:21 PM'
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import pandas as pd

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

df = pd.read_csv('fff.csv')


def generator(first_name, last_name, email, phone, id, row, pdf, VIP):
    # test if first_name is NaN
    if first_name != row['first_name']:
        full_name = last_name
    else:
        full_name = first_name + " " + last_name

    c = canvas.Canvas(pdf, pagesize=landscape(letter))

    # header
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 500, "ticket ID: " + id)
    c.drawCentredString(415, 450, "Name: " + full_name)
    c.drawCentredString(415, 400, "Phone No: " + phone)
    if VIP:
        img = 'ticket_r.jpg'
    else:
        img = 'ticket1.jpg'
    c.drawImage(img, 7, 50, width=None, height=None)
    c.showPage()
    c.save()




def send_email(email, pdf):
    email_user = 'greatleonsariel@gmail.com'
    email_password = 'l116066116066'
    email_send = email

    subject = 'E-ticket'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = u'Thanks for using our ticket register system. \nPlease download and print out the movie ticket in the attachment.\n' \
           u'Our Movie time is Feb 8th, 2018 6:30 - 8:30 PM.\n The location is 7128 Ada Blvd, AI & Trish Huehn Theatre, Concordia University.\n Thanks a lot and see you around!\n\n\n'\
        u'感谢您使用埃德蒙顿同促会系统，请下载并打印附件中的电影票。\n电影公映时间为2018年2月8日 6:30-8:30 PM。\n地址为:' \
           u' 7128 Ada Blvd, AI & Trish Huehn Theatre, Concordia University\n' \
           u'谢谢！'

    msg.attach(MIMEText(body, 'plain'))
    filename = pdf
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()


send_list = []
for index, row in df.iterrows():
    if index >= 28 and index<=53:
        VIP = row['VIP']
        first_name = str(row['first_name'])
        last_name = str(row['last_name'])
        email = str(row['email'])
        phone = str(row['phone'])
        id = str(row['Serial No'])
        if email[-1] == "?":
            email = email[:-1]
        if row['first_name'] == "Munoz":
            email = email[:-1]


        if first_name[-1] == "?":
            first_name = first_name[:-1]
        if last_name[-1] == "?":
            last_name = last_name[:-1]
        if phone[-1] == "?":
            phone = phone[:-1]
        pdf_name = "e-ticket " + str(id) + ' ' + str(last_name) + '.pdf'
        generator(str(first_name), str(last_name), str(email), str(phone), str(id), row, pdf_name, VIP)

        send_email(email, pdf_name)
        print(index)
    if index <28:
        continue
