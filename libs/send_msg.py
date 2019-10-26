from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC54a086023a43ebd4da03f27e62d956e9"
# Your Auth Token from twilio.com/console
auth_token  = "8e9add01afa3906ad085aee5054fcd11"
client = Client(account_sid, auth_token)
def send_msg():
    message = client.messages.create(
    # 这里中国的号码前面需要加86
    to="+8615821221621",
    from_="+13343262263",
    body="204.53重启遇到问题，请协助")
    print(message.sid)
if __name__ == '__main__':
    send_msg()

