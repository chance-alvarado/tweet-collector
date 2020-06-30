# tweet-collector
Script to collect tweets from a specified location during a set time period.

The purpose of this script is to provide an easy work-around to Twitter's request limits for multi-day searches and simplify writing such data to a file. **This script acts an extension of [Dmitry Mottl](https://pypi.org/user/Mottl/)'s library [GetOldTweets3](https://pypi.org/project/GetOldTweets3/). Please see this library's documentation for more general Twitter scraping scenarios.** 

---

### Prerequisites

This script has been written and tested using [Python](https://www.python.org/) v3.7.4.

The following default modules are required for proper function.

Requirement | Version
------------|--------
os | -
time | -
csv | -
datetime | -

The following package is required for proper function. 

Requirement | Version
------------|--------
[GetOldTweets3](https://pypi.org/project/GetOldTweets3/) | 0.0.11

This can be installed through the terminal as follows:

```
pip install GetOldTweets3
```

---

### Usage

Based on the user's specified **start date, duration, location,** and **waiting period**, `tweet_collector` creates a local *csv* file containing the following:
 
 date | text | favorites | retweets | hashtags | 
------|------|-----------|----------|----------|
Date and time of the tweet | Body of the tweet | Number of favorites | Number of retweets | All hashtags for the tweet |  

When run, `tweet_collector.py` will prompt the user for relevant information.

##### The first date to retrieve from:
```
Date to start search (yyyy-mm-dd): 
```

##### The number of days (including the start date) to collect for:
```
Number of days to collect for:
```

##### Location to search:
```
Location to search (City, State, Country): 
```

##### Time to wait to begin next search
```
Time in minutes to wait between search days:
```

It is important to specify an adequate waiting period as to not overload Twitter's allowable number of requests. **15 minutes should work well for most scenarios.**

---

### Example

For this example we will collect all tweets from Rochester, New York on August 3rd and 4th, 2018. We will run a terminal in the `resources` folder. In this case `tweet_collector.py` is in the same directory though it can be referenced from any other directory. A `data` folder can already exist, too.

##### Our project currently has the following form:
```

example_project
├─ my_example_project.py
└─ resources
   └─ tweet_collector.py
   
```

##### We run `tweet_collector.py` as follows:
```

$pwd
../example_project/resources

$python tweet_collector.py
Date to start search (yyyy-mm-dd): 2019-08-03
Number of days to collect for: 2
Location to search (City, State, Country): Rochester, New York, USA
Time in minutes to wait between search days: 15
File created. Tweet collection has begun.
Tweets written from 2019-08-03: 962
Waiting...
Tweets written from 2019-08-04: 880
Tweet collection completed.

```

##### Our project now appears as below:

```

example_project
├─ my_example_project.py
└─ resources
   ├─ tweet_collector.py
   └─ data
      └─ tweet_data.csv
      
```

##### We now have a *csv* file, `tweet_data.csv`, with all the tweets and information we need!

---

## Limitations

- For large amounts of tweets our one day request may still overload Twitter's request limits. 
- Special characters may not be properly transcribed in our file.

---

## Cloning

Clone this repository to your computer [here](https://github.com/chance-alvarado/tweet-collector/).

---

## Author

- **Chance Alvarado** 
    - [LinkedIn](https://www.linkedin.com/in/chance-alvarado/)
    - [GitHub](https://github.com/chance-alvarado/)

---

## License / Legal

- **The user of this script is solely responsible for adhering to [Twitter's rules and policies](https://help.twitter.com/en/rules-and-policies). This may include but is not limited to acquiring appropriate permissions and limiting the redistribution of certain Twitter data.**

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
