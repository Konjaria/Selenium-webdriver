from twilio.rest import Client
from flight_search import FlightSearch
import smtplib
import os


class NotificationManager(FlightSearch):
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, from_code='TBS', to_code='PAR'):
        super().__init__(from_code=from_code, to_code=to_code)
        self.client = None
        self.auth_token = None
        self.account_sid = None
        self.search_flights()

    def send_message(self):
        pseudo_account_sid = os.environ.get("TWILIO_ACC_SID")
        pseudo_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.account_sid = pseudo_account_sid
        self.auth_token = pseudo_auth_token
        self.client = Client(self.account_sid, self.auth_token)
        self.client.messages.create(body=f'Low price alert! Only ₾{self.price} to fly'
                                         f'from {self.cityFrom}-{self.flyFrom} to'
                                         f' {self.cityTo}-{self.flyTo}, from'
                                         f' {self.tomorrow.replace("/", "-")} to '
                                         f' {self.six_month_later.replace("/", "-")}.',
                                    from_='YOUR_PHONE_NUMBER',
                                    to='YOUR_TWILIO_VERIFIED_PHONE_NUMBER')

    def send_email(self, to):
        my_email = "YOUR_EMAIL"
        password = "YOUR_PASSWORD"
        text = f'Subject:Hey from Python\n\nLow price alert! Only ₾{self.price} to fly'\
               f'from {self.cityFrom}-{self.flyFrom} to'\
               f' {self.cityTo}-{self.flyTo}, from'\
               f' {self.tomorrow.replace("/", "-")} to '\
               f' {self.six_month_later.replace("/", "-")}.'.encode("utf-8")
        with smtplib.SMTP("YOUR SMTP SERVER ADDRESS", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to,
                msg=text
            )
