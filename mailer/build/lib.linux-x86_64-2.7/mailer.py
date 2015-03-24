#!/usr/bin/python

import smtplib

def mailer (sender, password, receivers, message):

	try:
   		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   		smtpObj.starttls()
   		smtpObj.login(sender, password)
   		smtpObj.sendmail(sender, receivers, message)         
   		smtpObj.quit()
   		print "Successfully sent email"
	
	except smtplib.SMTPException:
   		print "Error: unable to send email"
