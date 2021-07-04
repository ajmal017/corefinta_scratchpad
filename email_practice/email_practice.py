import smtplib, ssl

# https://stackoverflow.com/questions/10445528/python-mail-sent-by-script-is-marked-as-spam-by-gmail

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "jmzakatees@gmail.com"
receiver_email = 'crudedecay@gmail.com'
password = 'xxx'

message = f'''\
From: Javed Siddique {sender_email}
To: Javed Siddique {receiver_email}
Subject: When I put it in a function


Dear Javed, Then there is no subject\

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

