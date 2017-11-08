from ttools.utils import get_client


def main():
    client = get_client()
    client.SetCache(None)
    while True:
        tweets = client.GetFavorites(count=200)
        if not tweets:
            break

        for tweet in tweets:
            try:
                client.DestroyFavorite(status_id=tweet.id)
            except:
                pass
