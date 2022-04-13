import os
# import twilio
from twilio.rest import Client
# import random

account_sid =os.environ[AC8168860f96cb101ed5554d164bbd8803]
auth_token = os.environ [e448911608d42a798cab48fb5851f5a3]
client = Client(account_sid, auth_token)



# GOOD_MORNING_QUOTES =[
#     "Good Morning Love! Hope You Have An Amazing Day <3",
#     "Good Morning Beautiful! Hope you slept well <3",
#     "Hope you have a great day today, my lover!",
#     "Love you so much, I know you will have an amazing day"
# ]

# GOOD_EVENING_QUOTES = [
#     "Good Evening Love",
#     "Sleep Tight My Love!",
#     "Goodnight sweetie, I hope the love bugs bite!",
#     "Love you! I hope you dream about me tonight <3"
# ]

# def send_messages(quotes_list=GOOD_MORNING_QUOTES):
#     account_sid =os.environ[AC8168860f96cb101ed5554d164bbd8803]
#     auth_token = os.environ [e448911608d42a798cab48fb5851f5a3]
#     client = Client(account_sid, auth_token)
#     quote = quotes_list[random.randint(0, len(quotes_list)-1)]

message = client.messages \
    .create(
        body='Hello Malibu',
        from_='+18305810766',
        to='+15615370225'
    )
print(message.sid)