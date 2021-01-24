import praw

reddit = praw.Reddit(client_id="id", client_secret="secret",
                     user_agent="agent")

# Posts can be obtained by choosing a subreddit and filtering by top/new/hot/etc. or by entering a url

posts = reddit.subreddit("News").top(limit=5)

topNews = reddit.submission(
    url="https://www.reddit.com/r/news/comments/jptqj9/joe_biden_elected_president_of_the_united_states/")

# Comments can then be extracted from a given post. Things to keep in mind are the number of queries/required depth

topNews.comments.replace_more()
comments = []

for item in topNews.comments.list():
    comments.append(item.body)

# Getting the number of times a particular symbol appears in the comments. Regular expressions can be used for versatility

symbols = {"Fox": 0}

def symFreq(sym):

    for symbol in sym:
        numSym = 0
        for item in comments:
            numSym += item.count(symbol)
        sym[symbol] = numSym

symFreq(symbols)

print(symbols)