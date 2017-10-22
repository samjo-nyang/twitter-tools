from ttools.utils import get_client


def main():
    client = get_client()
    client.SetCache(None)
    while True:
        tweets = client.GetUserTimeline(count=200)
        if not tweets:
            break

        for tweet in tweets:
            client.DestroyStatus(tweet.id)
