import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "jmzakatees@gmail.com"
receiver_email = 'crudedecay@gmail.com'
password = 'suite203!'

message = f'''\
From: Javed Siddique {sender_email}
To: Javed Siddique {receiver_email}
Subject: Your mom is sick


Dear Javed, She is at St. Peter's Hospital.  I will send the address when I get there.\

'''

# send email here

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message )
except Exception as e:
    print('It did not work!')
    print(e)
finally:
    server.quit()

