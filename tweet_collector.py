# -*- coding: utf-8 -*-
"""Tweet collection based on GetOldTweets3.

The purpose of this script is to provide an easy work-around to
Twitter's request limits for multi-day searches and simplify
writing such data to a file. 

For in-depth instructions see the README found in the below
repository.

Explore this repository at:
    https://github.com/chalvarado96/tweet-collector

Author:
    Chance Alvarado
        LinkedIn: https://www.linkedin.com/in/chance-alvarado/
        Github: https://github.com/chalvarado96/
"""
import os
import time
import csv
import datetime
import GetOldTweets3 as got

while True:
    # Day to start search
    date_string = input('Date to start search (yyyy-mm-dd): ')
    try:
        start_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print('Please enter your date in (yyyy-mm-dd) form.')
        continue

    # Number of days to collect
    num_days = input('Number of days to collect for: ')
    try:
        num_days = int(num_days)
    except ValueError:
        print('Please enter your time frame as an integer.')
        continue

    # Location to search
    loc = input('Location to search (City, State, Country): ')

    # Time to wait
    waiting_period = input('Time in minutes to wait between search days: ')
    try:
        waiting_period = int(waiting_period)
        break
    except ValueError:
        print('Please enter your waiting period as an integer.')

# Collect all dates and store as a list of strings
date_list = [start_date.strftime("%Y-%m-%d")]
date = start_date
for i in range(num_days):
    date += datetime.timedelta(days=1)
    date_list.append(date.strftime("%Y-%m-%d"))

# If our data folder doesn't exist create one
if not os.path.isdir('data'):
    os.mkdir('data')

# Relative directory for data
tweet_dir = './data/tweet_data.csv'

# If our data file doesn't exist create a blank file
if not os.path.exists(tweet_dir):
    with open(tweet_dir, 'w', newline='') as file:

        # Print start message
        print('File created. Tweet collection has begun.')

        # Create custom writer
        writer = csv.writer(file,
                            quoting=csv.QUOTE_NONNUMERIC,
                            delimiter=','
                            )

        # Write headers to file
        writer.writerow(['date', 'username', 'text',
                         'favorites', 'retweets', 'hashtags'
                         ]
                        )

        # Iterate through all dates
        for i in range(num_days):

            # Specify dates to restrict search to
            to_date = date_list[i]
            til_date = date_list[i+1]

            # Create search criteria
            tweetCriteria = got.manager.TweetCriteria() \
                                       .setSince(to_date) \
                                       .setUntil(til_date) \
                                       .setNear(loc)

            # Searach for tweets
            tweets = got.manager.TweetManager.getTweets(tweetCriteria)

            # Add all tweets to list to write
            rows_to_write = []
            for tweet in tweets:
                rows_to_write.append(
                    [tweet.date, tweet.username, tweet.text,
                     tweet.favorites, tweet.retweets, tweet.hashtags
                     ]
                )

            # Write to file
            writer.writerows(rows_to_write)

            # Print success line and number of tweets
            print('Tweets written from %s: %s' % (to_date, len(tweets)))

            # Pause to ensure we don't overload requests
            if i != num_days - 1:
                print('Waiting...')
                time.sleep(60*waiting_period)
            else:
                print('Tweet collection completed.')
else:
    print('tweet_data.csv already exists.')
