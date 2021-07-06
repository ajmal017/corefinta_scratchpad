
import email, smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# https://djangocentral.com/sending-emails-with-csv-attachment-using-python/

fname = 'select_to_end.csv'
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jmzakatees@gmail.com"  # Enter your address
receiver_email = "crudedecay@gmail.com"
subj = "testing attachments"
body = "This is an email with attachment sent from Python"
password = 'xxx'

message = MIMEMultipart()
message["Subject"] = subj
message["From"] = sender_email
message["To"] = receiver_email


# Add attachment to message and convert message to string
with open(fname, 'rb') as file:
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name=fname))

# message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)