
import email, smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# https://djangocentral.com/sending-emails-with-csv-attachment-using-python/

fname = 'select_to_end.csv'
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jmzakatees@gmail.com"  # Enter your address
#receiver_email = input("What is the recipient email address?: ")  # Enter receiver address
receiver_email = "crudedecay@gmail.com"
#subj = input("What is the subject of the email?: ")
subj = "testing attachments"
#txtwords = input('what do you want to say?: ')
body = "This is an email with attachment sent from Python"
password = 'suite203!'

message = MIMEMultipart()
message["Subject"] = subj
message["From"] = sender_email
message["To"] = receiver_email

# filename = fname  # In same directory as script

# Add attachment to message and convert message to string
with open(fname, 'rb') as file:
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name=fname))

# message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)