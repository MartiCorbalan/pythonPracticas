import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Marti'
email['to'] = 'Corba@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email.gmail.com', 'password')
    smtp.send_message(email)
    print('all good boos! ')

