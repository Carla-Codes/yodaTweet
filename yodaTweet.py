import tweepy # EASIEST Twitter API
import requests
import ast
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, YODA_KEY


# Tweepy authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# mentions_timeline will return all the tweets you are mentioned in
# count = 1 will only grab the most recent one
mentions = api.mentions_timeline(count=1)

# Let's get rid of the tag so we only have the sentence we want to translate
mention = str(mentions[0].text).replace("@CodesCarla ", "")

#Everything we need for the Yoda Translator API
#https://rapidapi.com/orthosie/api/yoda-translator
url = "https://yodish.p.rapidapi.com/yoda.json"

querystring = {"text":mention}

payload = ""
headers = {
    'x-rapidapi-host': "yodish.p.rapidapi.com",
    'x-rapidapi-key': YODA_KEY ,
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

#Parsing the response
strResp=response.text.encode('ascii', 'ignore')
dictResp = ast.literal_eval(strResp)
print(dictResp["contents"]["translated"])

#Posting the translated tweet
api.update_status(dictResp["contents"]["translated"])