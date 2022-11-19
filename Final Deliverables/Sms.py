from twilio.rest import Client
import Keys

client = Client(Keys.account_sid, Keys.auth_token)

message = client.messages.create(
    body="The Water is UnSafe to drink, The Quality of water is Poor.",
    from_=Keys.twilio_number,
    to=Keys.my_phone_number
)
print(message.body)
