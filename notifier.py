#!/usr/bin/python3

import smtplib
import os

def send_email(email_subject):
	'''
	Send email notification to self

	@email_subject (string) Subject of the email to be sent
	'''

	gmail_sender = 'alexmmetcalfm2m@gmail.com'
	gmail_passwd = 'Machine123'
	email_address_to = 'alexmmetcalfm2m@gmail.com'
	
	script_name = os.path.basename(__file__)
	email_body_text = 'Script Name: %s' % script_name

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_sender, gmail_passwd)

	email_body = '\r\n'.join(['To: %s' % email_address_to,
	                    'From: %s' % gmail_sender,
	                    'Subject: %s' % email_subject,
	                    '', email_body_text])

	try:
	    server.sendmail(gmail_sender, [email_address_to], email_body)
	    print ('Email successfully sent.')
	except:
	    print ('Error sending mail.')

	server.quit()

if __name__ == "__main__":
    
    # For example
    run = 'success'

    if run == 'success':
    	send_email('Script success')
    if run == 'failure':
    	send_email('Script failure')

