import requests

TOKEN = "7122908765:AAFQCJwn-_0Rtn6GBp5hbOxi8SoYiLauTZg"
ROOT_ADMIN = 6432444926  # it's me
#ROOT_ADMIN = 1355559290


def send_load(load_price, load_id):
    load_link = f"https://www.haully.com/search/load/{load_id}"
    text = f"New load with price: {load_price}$ \nLoad link: {load_link}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": ROOT_ADMIN, "text": text}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        # send_load_me(load_price, load_id)
        print("Error: ", response.status_code)


def send_load_me(load_price, load_id):
    load_link = f"https://www.haully.com/search/load/{load_id}"
    text = f"New load with price: {load_price}$ \nLoad link: {load_link}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": IM, "text": text}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Error: ", response.status_code)
