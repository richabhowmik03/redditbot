import praw

reddit = praw.Reddit(
    client_id="DkeAyTvyf1PVK_MqwXXBGw",
    client_secret="SV9mOMSiLYNNWBz581zdNmCy6qsh2g",
    user_agent="trybot1.o",
    username="AttitudeIndependent2",
    password="trybotapp",
)
count = 0

subreddit = reddit.subreddit("science")
for post in subreddit.new(limit=15):
#    print("****************")
#    print(post.title)
    if "research" in post.title:
        count +=1
print(count)
