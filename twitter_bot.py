# Filename: twitter_bot.py
# File Path: /home/carbaja1/Python/TwitterBot/twitter_bot.py
# Run Command: sudo python3 /home/carbaja1/Python/TwitterBot/twitter_bot.py

from twython import Twython 

# Fill in your keys and token infollowing variables 
C_key = "Z8WmPjrVTPmhWptbIdy1BmCzr" 
C_secret = "Qt62127YChSXmM3qgmLggzfCdtcUXuRvJBZ41S2Y8t2WL0HB6S" 
A_token = "1191747179066449920-5nKy7fluHwa6zyxWeKJmYiFTMp1bRP" 
A_secret = "rbRdWVQd5m40sV1bKRqwKmxVGZEXNOVJfFe7tPrGblDQT" 

# Authenticate to your app.
myTweet = Twython(C_key,C_secret,A_token,A_secret) 

# Tweet text by editing the text in the quotes. 
myTweet.update_status(status= "This is my second Twitter Bot Tweet")

#Tweet Photos 
# photo = open('/path/to/file/image.jpg', 'rb') 
# response = twitter.upload_media(media=photo)
# twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])
