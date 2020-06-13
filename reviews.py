from google_play_scraper import Sort, reviews
result, continuation_token = reviews(
    'com.fantome.penguinisle',
    lang='en', # defaults to 'en'
    country='in', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=100, # defaults to 100
    filter_score_with=1 # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.zhiliaoapp.musically',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)

for x in result:
	content1 = x["content"]
	print(content1)
	print()