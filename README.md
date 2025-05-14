
# MEXC TradingView Webhook Bot

This bot receives webhook alerts from TradingView and places market orders on MEXC using the REST API.

## Setup

1. Create an account on [Render](https://render.com).
2. Create a new Web Service and connect to this project from GitHub or upload the files.
3. Set the following environment variables:
   - `API_KEY`: Your MEXC API Key
   - `SECRET_KEY`: Your MEXC Secret Key
4. Set the build and start command:
   - **Start Command:** `python3 mexc_webhook_bot.py`
   - **Port:** `5000`

## TradingView Alert Format

Webhook URL example:

```
https://your-service-name.onrender.com/webhook
```

Message body example:

```
{
  "message": "buy,BTCUSDT"
}
```
