import requests

def send_webhook(url, message):
    data = {"content": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    webhook_url = "YOUR WEBHOOK URL"
    message = "Hello world!"
    send_webhook(webhook_url, message)
