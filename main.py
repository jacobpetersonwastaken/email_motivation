import random
import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
QUOTES_DATA = 'quotes.json'
EMAIL_DATA = 'emails.json'
load_dotenv('.env')
my_email = os.getenv('my_email')
password = os.getenv('password')
quotes_df = pd.read_json('quotes.json', typ='series')
quote_list = quotes_df.tolist()
email_df = pd.read_json('emails.json', typ='series')
email_list = email_df.tolist()



def send_email(sending_from, to, msg, sub):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        """Sends email without attachment."""
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=sending_from, to_addrs=to, msg=f'Subject:{sub}\n\n{msg}')



rand_quote = quote_list[random.randint(0, len(quote_list) - 1)]
subject = 'Hopefully this quote motivates you.'
message = rand_quote
send_email(sending_from=my_email, to=email_list, msg=message, sub=subject)
