from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "test"
# Your Auth Token from twilio.com/console
auth_token  = "test"
client = Client(account_sid, auth_token)
def send_msg(content):
    try:
        message = client.messages.create(
        # 这里中国的号码前面需要加86
        to="+8615821221621",
        from_="+13343262263",
        body = content )
    except:
        return "短信服务被暂停，请联系twillo恢复"
    else:
        return "短信发送成功,管理员正在赶来的路上。。"
if __name__ == '__main__':
    send_msg(content="test")

