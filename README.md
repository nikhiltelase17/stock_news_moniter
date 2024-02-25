# Stock Price Notifier

## Overview

The Stock Price Notifier is a Python script designed to monitor the daily stock prices of a specified company, in this case, Tesla Inc (TSLA). It provides notifications when the stock price experiences significant changes, accompanied by relevant news headlines.

## How it Works

1. **Stock Data Retrieval:**
   - The script fetches daily stock data from the Alpha Vantage API using the provided API key.

2. **Percentage Change Calculation:**
   - It calculates the percentage change in stock prices between yesterday and the day before yesterday.      

3. **News Headline Retrieval:**
   - Utilizing the News API, the script gathers top headlines related to the specified company.

4. **Notification Sending:**
   - If the stock percentage change is deemed significant, the script sends an SMS notification using the Twilio API.
   - The notification includes the percentage change and a relevant news headline.

## Key Components

- **Alpha Vantage API:**
  - Provides daily stock data for the specified company.

- **News API:**
  - Fetches top headlines related to the specified company for additional context.

- **Twilio API:**
  - Sends SMS notifications to the user when significant stock changes occur.

## Requirements

- Python 3.x
- Twilio Account and API credentials
- Alpha Vantage API Key

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nikhiltelase17/stock_news_moniter.git
   cd stock-price-notifier
   ```

2. **Install Required Dependencies:**
   ```bash
   pip install requests twilio
   ```

3. **API Key Configuration:**
   - Replace the placeholder API keys and Twilio credentials in the script (`stock_notifier.py`).

4. **Run the Script:**
   ```bash
   python stock_notifier.py
   ```

5. **Receive Notifications:**
   - Get SMS notifications with the percentage change and relevant news when significant stock changes occur.

## Customize and Contribute

- Feel free to customize the script or add new features based on your preferences.
- Contributions are welcome! If you have improvements, submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
