# from email.message import Message
# from email.quoprimime import quote
# from http import client
# from lib2to3.pgen2 import token
# import random, schedule, time

# from twilio.rest import Client 
# from creds import cellphone,twilio_account,twilio_number,twilio_token

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
#     account = twilio_account
#     token = twilio_token
#     client = Client(account, token)
#     quote = quotes_list[random.randint(0, len(quotes_list)-1)]


#     client.messages.create(
#         to=cellphone,
#         from_=twilio_token,
#         body=quote
#     )

#     # Morning Text
#     schedule.every().day.at("07:00").do(send_messages, GOOD_MORNING_QUOTES)

#     # Evening Text
#     schedule.every().day.at("19:00").do(send_messages,GOOD_MORNING_QUOTES)

#     # Test Message
#     schedule.every().day.at("17:00").do(send_messages,GOOD_MORNING_QUOTES)

#     while True:
#         # checks whether a scheduled task is pending to run or not
#         schedule.run_pending()
#         time.sleep(2)