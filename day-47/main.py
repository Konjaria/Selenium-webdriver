from bs4 import BeautifulSoup
import requests
import lxml
from smtplib import SMTP

URL = "YOUR_DESIRED_PRODUCT"
headers = {
    "User-Agent": "YOUR_BROWSERS'S_USER-AGENT",
    "Accept-Language": "YOUR-BROWSER'S ACCEPT LANGUAGE"

}
response = requests.get(url=URL, headers=headers)
raw_html = response.text

soup = BeautifulSoup(raw_html, "lxml")
price = float(soup.find(name="span", id="price").string.split("$")[1])

if price <= 25:
    # constants
    my_email = "YOUR_EMAIL"
    password = "YOUR_PASSWORD"
    text = f'BUY NOW!! Your Favourite product\'s price decreased.'.encode("utf-8")
    with SMTP("YOUR_EMAIL'S_SMTP", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ADDRESSEE'S EMAIL",
            msg=text
        )
    print("sent successfully ✅")
