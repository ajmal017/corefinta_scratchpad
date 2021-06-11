import smtplib, ssl

class EmailYahoo:

    def email_func(self):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "jmzakatees@gmail.com"
        receiver_email = 'crudedecay@gmail.com'
        password = 'suite203!'

        message = '''\
        \
        Subject: Buy this stock\
        
        TSLA\
        
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

    def trigger(self):
        x = 7
        y = x + 1
        if y > 5:
            self.email_func()
        else:
            print('nothing to email yet!')

def main():
    app = EmailYahoo()
    app.trigger()

if __name__ == "__main__":
    main()