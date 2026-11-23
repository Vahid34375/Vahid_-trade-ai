
"""
Vahid Trade AI
Lightweight trading analysis engine
"""

from datetime import datetime

APP_NAME = "Vahid Trade AI"
ANALYSIS_INTERVAL = 3600  # One hour


def analyze_market(prices):
    """Basic market trend analysis."""

    if len(prices) < 20:
        return {
            "status": "waiting",
            "message": "Not enough market data"
        }

    short_average = sum(prices[-5:]) / 5
    long_average = sum(prices[-20:]) / 20

    if short_average > long_average:
        signal = "BULLISH"
    elif short_average < long_average:
        signal = "BEARISH"
    else:
        signal = "NEUTRAL"

    return {
        "status": "success",
        "signal": signal,
        "short_average": round(short_average, 4),
        "long_average": round(long_average, 4),
        "time": datetime.now().isoformat()
    }


if __name__ == "__main__":
    print(APP_NAME)
    print("Hourly market analysis engine is ready.")
    print("No automatic trades are executed.")
