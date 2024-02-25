import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
current_date = datetime.now()

# Calculate yesterday's date
yesterday_time = current_date - timedelta(days=1)
yesterday = yesterday_time.strftime('%Y-%m-%d')

# Calculate the before yesterday's date
before_yesterday_time = current_date - timedelta(days=2)
before_yesterday = before_yesterday_time.strftime('%Y-%m-%d')


def stock_price():
    # getting stock data
    stock_parameters = {"function": "TIME_SERIES_DAILY",
                        "symbol": STOCK,
                        "apikey": "F6RDVKLYKPODRJFB",
                        }
    stock_api_url = f"https://www.alphavantage.co/query?"
    stock_response = requests.get(stock_api_url, params=stock_parameters)
    stock_data = stock_response.json()

    # getting stock price yesterday and before_yesterday
    yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
    before_yesterday_price = float(stock_data["Time Series (Daily)"][before_yesterday]["4. close"])
    print(yesterday_price)
    print(before_yesterday_price)
    # calculating percentage
    difference = yesterday_price - before_yesterday_price
    print(difference)
    percentage = round((difference / before_yesterday_price) * 100)
    print(percentage)
    return percentage


stock_difference = stock_price()


def formatted_percentage():
    p = str(stock_difference)
    if "-" in p:
        for_p = p.replace("-", "🔻")
        return for_p
    else:
        for_p = f"🔺{p}"
        return for_p


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then send message.
if stock_difference > 0 or stock_difference < -1:
    # get the first 3 news pieces
    news_apikey = "57b3d49680ef46149e2f418004313e95"
    parameters = {"from": yesterday,
                  "q": "tesla",
                  "sortBy": "relevancy",
                  "apiKey": news_apikey,
                  }

    news_api_url = f"https://newsapi.org/v2/top-headlines?"
    response = requests.get(news_api_url, params=parameters)
    print(response.url)
    news_data = response.json()

    news_title = news_data["articles"][1]["title"]
    news_description = news_data["articles"][1]["description"]

    stock_message = f"{STOCK}: {formatted_percentage()}\nHeadline: {news_title}\nBrief: {news_description}"
    print(stock_message)
    # Send a message with the percentage change and each article's title and description to your phone number.
    account_sid = "ACc16699c2e3ccdf2980f17498ecafa82d"
    auth_token = "5410e1c27a7942754c52bc8823ab2ef4"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"{stock_message}",
                         from_='+16592667763',
                         to='+918305230871'
                     )

    print(message.sid)
