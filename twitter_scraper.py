from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020, 3, 10)
end_date = dt.date(2020, 3, 13)

limit = 1000
lang = 'en'

tweets_0 = query_tweets("❤️", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
tweets_1 = query_tweets("😄", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
tweets_2 = query_tweets("😔", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
tweets_3 = query_tweets("🥺", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)
tweets_4 = query_tweets("😤", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)

df_0 = pd.DataFrame(t.__dict__ for t in tweets_0)
df_1 = pd.DataFrame(t.__dict__ for t in tweets_1)
df_2 = pd.DataFrame(t.__dict__ for t in tweets_2)
df_3 = pd.DataFrame(t.__dict__ for t in tweets_3)
df_4 = pd.DataFrame(t.__dict__ for t in tweets_4)
df_0["label"] = 0
df_1["label"] = 1
df_2["label"] = 2
df_3["label"] = 3
df_4["label"] = 4

df_all = pd.concat([df_0, df_1, df_2, df_3, df_4])
df_train = df_all.sample(frac=1)
df_train.to_csv('train_data')