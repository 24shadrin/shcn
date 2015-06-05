#!/usr/bin/python
#file mail.py

import smtplib
import sys

txtparam=sys.argv[1]

fromaddr = '24shadrin@gmail.com'

toaddr = 'n.v.shadrin@gmail.com'

subj = 'shms'

msg_txt = txtparam + '\n\nHave a good day!' #

msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( fromaddr, toaddr, subj, msg_txt)

username = '24shadrin@gmail.com'

password = 'scooterman3128'

server = smtplib.SMTP('smtp.gmail.com:587')

#server = smtplib.SMTP('smtp.gmail.com:465')

server.set_debuglevel(5);

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, msg)

server.quit()
