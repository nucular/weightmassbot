import asyncio, os, sys
from peony import PeonyClient

SEARCH_QUERY = "weight kg"
RETWEET_COMMENT = "You may have implied weight was measured in grams instead of Newtons. Did you mean MASS? If not, have a nice day :)"
ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]

lastId = 0

async def track(client):
  async with client.stream.statuses.filter.post(track=SEARCH_QUERY) as stream:
    async for tweet in stream:
      if (not "text" in tweet)
        or tweet["id"] <= lastId
        or not all(i in tweet["text"] for i in SEARCH_QUERY.split(" ")):
        continue
      lastId = tweet["id"]

      tweet_url = "https://twitter.com/{}/status/{}".format(
        tweet["user"]["screen_name"], tweet["id"]
      )
      status = RETWEET_COMMENT + " " + tweet_url
      print("Retweeting", tweet_url)
      await client.api.statuses.update.post(status=status)

if __name__ == "__main__":
  client = PeonyClient(
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET
  )
  print("Starting")
  asyncio.get_event_loop().run_until_complete(track(client))
