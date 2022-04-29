import tweepy, csv, key, re

# OAuth認証
auth = tweepy.OAuthHandler(key.Consumer_key, key.Consumer_secret)
auth.set_access_token(key.Access_token, key.Access_secret)
api = tweepy.API(auth)

#ツイート取得
rowdata = []

#最大2200件のツイートを取得するためのページ
pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

for page in pages:
  results = api.user_timeline(q="-filter:retweets" , screen_name="okaka10180", count = 100, page = page)
  for r in results:
	#r.textで、投稿の本文のみ取得する
    rowdata.append(r.text.replace(",",""))

data = []

for s in rowdata:
  c = re.search('[ｦ-ﾟ]+', s)
  if(s[0] == '@'):
    continue
  if(c):
    data.append(s)

f = open('output.csv', 'w',encoding='UTF_8_sig')
writer = csv.writer(f, lineterminator='\n')

writer.writerow(data)


# ファイルクローズ
f.close()

#with open('tweet_test.csv', 'w',newline='',encoding='utf-8') as f:
#    writer = csv.writer(f, lineterminator='\n')
#    writer.writerow(["id","user","created_at","text","fav","RT","follower","follows"])
#    writer.writerows(tweet_data)
#pass
