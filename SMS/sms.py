from twitto.rest import Client

account_sid = 'esta key te la da la propia web'
auth_token = 'te da la web este token'
client = Client(account_sid, auth_token)


message = Client.messages.create(
    from_ = '+12266024690',
    body = 'I CANT BELIVE THIS WORKS',
    TO = 'QUIEN VA A RECIBIR EL SMS'
    )
print(message.sid)