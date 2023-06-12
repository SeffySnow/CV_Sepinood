import requests

def send_sms(text):
    url = "https://api.kavenegar.com/v1/504E67495868675141633136564C4B5151745853626468394C6B34776D4C3979/sms/send.json?receptor=09102981178&message=You have a new message with the title :"+ text

    payload = {}
    headers = {
    'Cookie': 'cookiesession1=678A8C31234ABCEFGIJKLMNOPQRS6149'
    }

    requests.request("GET", url, headers=headers, data=payload)

