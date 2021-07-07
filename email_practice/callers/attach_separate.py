import smtplib, ssl
import time

import df_class_attach

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# use outlook app and put it in favorites by selecting the sender email address and clicking star in upper-right
# then set notifications for favorites

class EmailYahoo:

    def __init__(self):
        self.counter = 0
        self.buy_msg = "Buy today"
        self.df_short_table = df_class_attach.Sample_DF_Call()

    def email_func(self):
        fname = 'selected.csv'
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "jmzakatees@gmail.com"  # Enter your address
        with open(r"/Users/jsidd/Documents/Quant Library/receiver_email.txt",
                  "r") as file2:
            receive_email = file2.read()
        receiver_email = receive_email
        subj = "Forecasted values for TQQQ based Gauss and ATR bands"
        body = "This is an email with attachment sent from Python"

        with open(r"/Users/jsidd/Documents/Quant Library/test.txt",
                  "r") as file1:
            passwd = file1.read()
        password = passwd

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

    def trigger(self):
        x = 0
        while self.counter < 10:
            x = x + 1
            print(x)
            if x == 4:
                # self.buy_msg = f"Short that {x} mutha!"
                self.df_short_table.yahoo_sample()
                self.email_func()
                time.sleep(1)
                break
            else:
                time.sleep(2)
                self.counter += 1


def main():
    app = EmailYahoo()
    app.trigger()

if __name__ == "__main__":
    main()