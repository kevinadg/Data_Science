
import praw

# Définition de la connexion à Reddit
reddit = praw.Reddit(
    client_id="p7XFBCV2is0jEJKA1RV2Cw",         # Remplace avec ton client ID
    client_secret="pLu2i7_9SdozVxZ4abttiyvQ2YOpVw",  # Remplace avec ton client secret
    user_agent="mypython/2.0 (kevinadagbe@gmail.com)",  # Ton User-Agent
           
           
)


# Vérifier la connexion
print(f"Connecté en tant que : {reddit.user.me()}")

# Recherche dans un subreddit (ex : "python")
subreddit = reddit.subreddit("python")

# Afficher les 5 premiers posts populaires dans le subreddit "python"
for post in subreddit.hot(limit=5):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print(f"Author: {post.author}")
    print("-" * 40)
