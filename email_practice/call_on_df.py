import smtplib, ssl
import time
import yfinance as yf

# use outlook app and put it in favorites by selecting the sender email address and clicking star in upper-right
# then set notifications for favorites

class EmailYahoo:

    def __init__(self):
        self.counter = 0
        self.buy_msg = "Buy today"
        self.data = None

    def email_func(self):

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "jmzakatees@gmail.com"
        receiver_email = 'crudedecay@gmail.com'
        password = 'suite203!'

        message = f'''\
        From: Javed Siddique {sender_email}
        To: Javed Siddique {receiver_email}
        Subject: {self.buy_msg}


        Dear Javed, This is the future:\
        {self.data}

        '''

        # send email here

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            print('It did not work!')
            print(e)
        finally:
            server.quit()

    def trigger(self):
        x = 0
        while self.counter < 10:
            x = x + 1
            print(x)
            if x == 4:
                # self.buy_msg = f"Short that {x} mutha!"
                self.df_table()
                time.sleep(1)
                self.email_func()
                break
            else:
                time.sleep(2)
                self.counter += 1

    def df_table(self):
        # data = yf.download(tickers = ticker, start='2019-01-04', end='2021-06-09')
        ticker = 'NQ=F'
        self.data = yf.download(tickers=ticker, period="3mo", interval='1wk')
        print(self.data)
        # data = yf.download(tickers = ticker, start='2000-01-04', end='2005-12-31', interval = '1d')

        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo



def main():
    app = EmailYahoo()
    app.trigger()

if __name__ == "__main__":
    main()