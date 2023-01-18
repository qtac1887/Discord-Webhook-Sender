# Discord Webhook Sender

The Discord Webhook Sender is a Python function that uses the requests library to send a webhook message to a Discord server. This allows users to easily and quickly send webhook messages to their Discord server, providing an easy way to communicate important information.

## Getting Started
To use the Discord Webhook Sender, you will need to first install the requests library.

Install [python](https://www.python.org/downloads/) to use the script.

```bash
pip install requests
```
Once the requests library is installed, you can use the following code snippet to send a webhook message to a Discord server:
```bash
import requests

def send_webhook(url, message):
    data = {"content": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    webhook_url = "YOUR WEBHOOK URL"
    message = "Hello world!"
    send_webhook(webhook_url, message)
```
The code can be run in a Python script, allowing users to easily and quickly send webhook messages to their Discord server. After providing the webhook URL and message, all that is left is to run the script and the message will be sent to the Discord server.

To customize a message to send to a Discord server, you will need to edit the code snippet used in the previous example. In this example, the message that is sent can be set as the "content" key in the data dictionary. For example, if you wanted to send a message that said "Hello World!", you would change the code to look like this:
```bash
import requests

def send_webhook(url, message):
    data = {"content": "Hello World!"}
    requests.post(url, data=data)

if __name__ == "__main__":
    webhook_url = "YOUR WEBHOOK URL"
    message = "Hello world!"
    send_webhook(webhook_url, message)
```
In this code snippet, the "Hello World!" string has been set as the content of the message, and this will be the message that is sent to the Discord server. You can change this string to any message you want, allowing you to customize the message that is sent.
