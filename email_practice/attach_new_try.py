from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib

EMAIL_SUBJECT = 'test for attachments'
EMAIL_FROM = 'jmzakatees@gmail.com'
EMAIL_TO = 'crudedecay@gmail.com'
PATH_TO_CSV_FILE = 'select_to_end.csv'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USERNAME = 'jmzakatees@gmail.com'
SMTP_PASSWORD = 'xxx'

def send_mail():
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(PATH_TO_CSV_FILE,'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=PATH_TO_CSV_FILE))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_obj.quit()