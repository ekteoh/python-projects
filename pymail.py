import smtplib

gmail_user='ekteoh618@gmail.com'
gmail_password='Tek_040728'

sent_from = 'ekteoh618@gmail.com'  
to = ['ekteoh618@gmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, whats up?\n\n- You'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


server=smtplib.SMTP('smtp.gmail.com',587)
#server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(gmail_user,gmail_password)
server.sendmail(sent_from,to,email_text)
server.close()
print('Email sent!')
