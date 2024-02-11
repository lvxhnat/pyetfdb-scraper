# pyetfdb_scraper: Free ETF data at your fingertips
```pyetfdb_scraper``` is a Python library for extracting ETF data directly from [ETFDB](https://etfdb.com/), a website providing one of the largest ETF Databases containing ETFs from a vast range of asset classes, industries, issuers, and investment styles.

## Quick Start 
Install with ```pip``` as a package pip. See the pip package here https://pypi.org/project/pyetfdb-scraper/.

```
pip install pyetfdb-scraper
```

```python
from pyetfdb_scraper import etf
```

## Example Usage

```python
from pyetfdb_scraper.etf import ETF,load_etfs 
# returns list of available ETFs.
etfs = load_etfs()
# load etf
ivv = ETF('IVV')
# Get basic ETF information
print(ivv.info)

>>> {
    "vitals": {
        "etf_name": "iShares Core S&P 500 ETF",
        "issuer": "BlackRock, Inc.",
        "issuer_link": "/issuer/blackrock-inc/",
        "brand": "iShares",
        "brand_link": "/issuer/ishares/",
        "structure": "ETF",
        "structure_link": "",
        "expense_ratio": "0.03%",
        "hompage_link": "http://us.ishares.com/product_info/fund/overview/IVV.htm?qt=IVV",
        "inception": "May 15, 2000",
        "index_tracked": "S&P 500 Index",
        "index_tracked_link": "/index/sp-500-index/",
    },
    "dbtheme": {
        "category": "Large Cap Growth Equities",
        "category_link": "",
        "asset_class": "Equity",
        "asset_class_link": "/etfs/asset-class/equity/",
        "asset_class_size": "Large-Cap",
        "asset_class_size_link": "/etfs/size/large-cap/",
        "asset_class_style": "Blend",
        "asset_class_style_link": "/etfs/style/blend/",
        "general_region": "North America",
        "general_region_link": "/etfs/region/north-america/",
        "specific_region": "U.S.",
        "specific_region_link": "/etfs/country/us/",
    },
    "fact_set": {
        "segment": ["Equity: U.S.  -  Large Cap"],
        "category": ["Size and Style"],
        "focus": ["Large Cap"],
        "niche": ["Broad-based"],
        "strategy": ["Vanilla"],
        "weighting_scheme": ["Market Cap"],
    },
    "analyst_report": "Another alternative is VOO, which is slightly cheaper and is eligible for commission free trading within Vanguard accounts. Beyond the S&P 500, RSP may be another alternative worth a closer look; that ETF, which is a bit more expensive, holds all stocks in the S&P 500 but gives an equivalent weighting to each. As such, it might be attractive to investors looking to steer clear of the potential inefficiencies in market cap weighting methodologies.",
    "trade_data": {
        "open": "",
        "volume": "",
        "day_low": "",
        "day_high": "",
        "52_week_low": "$376.34",
        "52_week_high": "$491.10",
        "aum": "$416,620.0 M",
        "shares": "854.5 M",
    },
    "historical_trade_data": {
        "1_month_avg_volume": "5,672,082",
        "3_month_avg_volume": "5,182,910",
    },
    "alternative_etfs": [
        {
            "type": "Cheapest",
            "ticker": "SFY",
            "expense_ratio": "0.00%",
            "assets": "$622.0 M",
            "avg_daily_volume": "175,030",
            "ytd_return": "1.89%",
        },
        {
            "type": "Largest (AUM)",
            "ticker": "SPY",
            "expense_ratio": "0.09%",
            "assets": "$485.9 B",
            "avg_daily_volume": "79 M",
            "ytd_return": "2.68%",
        },
        {
            "type": "Most Liquid (Volume)",
            "ticker": "SPY",
            "expense_ratio": "0.09%",
            "assets": "$485.9 B",
            "avg_daily_volume": "79 M",
            "ytd_return": "2.68%",
        },
        {
            "type": "Top YTD Performer",
            "ticker": "WUGI",
            "expense_ratio": "0.75%",
            "assets": "$25.1 M",
            "avg_daily_volume": "2,590",
            "ytd_return": "8.00%",
        },
    ],
    "other_alternative_etfs": [
        {
            "type": "Cheapest",
            "ticker": "BKLC",
            "expense_ratio": "0.00%",
            "assets": "$2.1 B",
            "avg_daily_volume": "78,895",
            "ytd_return": "2.60%",
        },
        {
            "type": "Largest (AUM)",
            "ticker": "SPY",
            "expense_ratio": "0.09%",
            "assets": "$485.9 B",
            "avg_daily_volume": "79 M",
            "ytd_return": "2.68%",
        },
        {
            "type": "Most Liquid (Volume)",
            "ticker": "SPY",
            "expense_ratio": "0.09%",
            "assets": "$485.9 B",
            "avg_daily_volume": "79 M",
            "ytd_return": "2.68%",
        },
        {
            "type": "Top YTD Performer",
            "ticker": "AMOM",
            "expense_ratio": "0.75%",
            "assets": "$16.0 M",
            "avg_daily_volume": "4,800",
            "ytd_return": "7.15%",
        },
    ],
}

print(ivv.to_dict())

>>> {
    "info": {
        "vitals": {
            "issuer": "BlackRock, Inc.",
            "issuer_link": "/issuer/blackrock-inc/",
            "brand": "iShares",
            "brand_link": "/issuer/ishares/",
            "structure": "ETF",
            "structure_link": "",
            "expense_ratio": "0.03%",
            "hompage_link": "http://us.ishares.com/product_info/fund/overview/IVV.htm?qt=IVV",
            "inception": "May 15, 2000",
            "index_tracked": "S&P 500 Index",
            "index_tracked_link": "/index/sp-500-index/",
            "etf_name": "iShares Core S&P 500 ETF",
        },
        "dbtheme": {
            "category": "Large Cap Growth Equities",
            "category_link": "",
            "asset_class": "Equity",
            "asset_class_link": "/etfs/asset-class/equity/",
            "asset_class_size": "Large-Cap",
            "asset_class_size_link": "/etfs/size/large-cap/",
            "asset_class_style": "Blend",
            "asset_class_style_link": "/etfs/style/blend/",
            "general_region": "North America",
            "general_region_link": "/etfs/region/north-america/",
            "specific_region": "U.S.",
            "specific_region_link": "/etfs/country/us/",
        },
        "fact_set": {
            "segment": ["Equity: U.S.  -  Large Cap"],
            "category": ["Size and Style"],
            "focus": ["Large Cap"],
            "niche": ["Broad-based"],
            "strategy": ["Vanilla"],
            "weighting_scheme": ["Market Cap"],
        },
        "analyst_report": "Another alternative is VOO, which is slightly cheaper and is eligible for commission free trading within Vanguard accounts. Beyond the S&P 500, RSP may be another alternative worth a closer look; that ETF, which is a bit more expensive, holds all stocks in the S&P 500 but gives an equivalent weighting to each. As such, it might be attractive to investors looking to steer clear of the potential inefficiencies in market cap weighting methodologies.",
        "trade_data": {
            "open": "",
            "volume": "",
            "day_low": "",
            "day_high": "",
            "52_week_low": "$376.34",
            "52_week_high": "$491.10",
            "aum": "$416,620.0 M",
            "shares": "854.5 M",
        },
        "historical_trade_data": {
            "1_month_avg_volume": "5,672,082",
            "3_month_avg_volume": "5,182,910",
        },
        "alternative_etfs": [
            {
                "type": "Cheapest",
                "ticker": "SFY",
                "expense_ratio": "0.00%",
                "assets": "$622.0 M",
                "avg_daily_volume": "175,030",
                "ytd_return": "1.89%",
            },
            {
                "type": "Largest (AUM)",
                "ticker": "SPY",
                "expense_ratio": "0.09%",
                "assets": "$485.9 B",
                "avg_daily_volume": "79 M",
                "ytd_return": "2.68%",
            },
            {
                "type": "Most Liquid (Volume)",
                "ticker": "SPY",
                "expense_ratio": "0.09%",
                "assets": "$485.9 B",
                "avg_daily_volume": "79 M",
                "ytd_return": "2.68%",
            },
            {
                "type": "Top YTD Performer",
                "ticker": "WUGI",
                "expense_ratio": "0.75%",
                "assets": "$25.1 M",
                "avg_daily_volume": "2,590",
                "ytd_return": "8.00%",
            },
        ],
        "other_alternative_etfs": [
            {
                "type": "Cheapest",
                "ticker": "BKLC",
                "expense_ratio": "0.00%",
                "assets": "$2.1 B",
                "avg_daily_volume": "78,895",
                "ytd_return": "2.60%",
            },
            {
                "type": "Largest (AUM)",
                "ticker": "SPY",
                "expense_ratio": "0.09%",
                "assets": "$485.9 B",
                "avg_daily_volume": "79 M",
                "ytd_return": "2.68%",
            },
            {
                "type": "Most Liquid (Volume)",
                "ticker": "SPY",
                "expense_ratio": "0.09%",
                "assets": "$485.9 B",
                "avg_daily_volume": "79 M",
                "ytd_return": "2.68%",
            },
            {
                "type": "Top YTD Performer",
                "ticker": "AMOM",
                "expense_ratio": "0.75%",
                "assets": "$16.0 M",
                "avg_daily_volume": "4,800",
                "ytd_return": "7.15%",
            },
        ],
    },
    "expense": {
        "tax_analysis": {
            "max_short_term_capital_gains_rate": ["39.60%"],
            "max_long_term_capital_gains_rate": ["20.00%"],
            "tax_on_distributions": ["Qualified dividends"],
            "distributes_k1": ["No"],
        },
        "expense_ratio_analysis": [
            {"ivv": "0.03%"},
            {"etf_database_category_average": "0.37%"},
            {"factset_segment_average": "0.59%"},
        ],
    },
    "holdings": {
        "top_holdings": [
            {
                "symbol": "AAPL",
                "holding": "Apple Inc.",
                "share": "7.18%",
                "url": "https://etfdb.com/stock/AAPL/",
            },
            {
                "symbol": "MSFT",
                "holding": "Microsoft Corporation",
                "share": "6.50%",
                "url": "https://etfdb.com/stock/MSFT/",
            },
            {
                "symbol": "AMZN",
                "holding": "Amazon.com, Inc.",
                "share": "3.32%",
                "url": "https://etfdb.com/stock/AMZN/",
            },
            {
                "symbol": "NVDA",
                "holding": "NVIDIA Corporation",
                "share": "2.95%",
                "url": "https://etfdb.com/stock/NVDA/",
            },
            {
                "symbol": "GOOGL",
                "holding": "Alphabet Inc. Class A",
                "share": "2.03%",
                "url": "https://etfdb.com/stock/GOOGL/",
            },
            {
                "symbol": "META",
                "holding": "Meta Platforms Inc. Class A",
                "share": "1.83%",
                "url": "https://etfdb.com/stock/META/",
            },
            {
                "symbol": "TSLA",
                "holding": "Tesla, Inc.",
                "share": "1.82%",
                "url": "https://etfdb.com/stock/TSLA/",
            },
            {
                "symbol": "GOOG",
                "holding": "Alphabet Inc. Class C",
                "share": "1.75%",
                "url": "https://etfdb.com/stock/GOOG/",
            },
            {
                "symbol": "BRK.B",
                "holding": "Berkshire Hathaway Inc. Class B",
                "share": "1.66%",
                "url": "https://etfdb.com/stock/BRK.B/",
            },
            {
                "symbol": "UNH",
                "holding": "UnitedHealth Group Incorporated",
                "share": "1.25%",
                "url": "https://etfdb.com/stock/UNH/",
            },
            {
                "symbol": "JPM",
                "holding": "JPMorgan Chase & Co.",
                "share": "1.22%",
                "url": "https://etfdb.com/stock/JPM/",
            },
            {
                "symbol": "JNJ",
                "holding": "Johnson & Johnson",
                "share": "1.17%",
                "url": "https://etfdb.com/stock/JNJ/",
            },
            {
                "symbol": "XOM",
                "holding": "Exxon Mobil Corporation",
                "share": "1.16%",
                "url": "https://etfdb.com/stock/XOM/",
            },
            {
                "symbol": "V",
                "holding": "Visa Inc. Class A",
                "share": "1.03%",
                "url": "https://etfdb.com/stock/V/",
            },
            {
                "symbol": "AVGO",
                "holding": "Broadcom Inc.",
                "share": "0.98%",
                "url": "https://etfdb.com/stock/AVGO/",
            },
        ],
        "holding_comparison": [
            {
                "number_of_holdings": "1000",
                "etf_database_category_average": "418",
                "factset_segment_average": "173",
            },
            {
                "pct_of_assets_in_top_10": "41.95%",
                "etf_database_category_average": "43.40%",
                "factset_segment_average": "60.51%",
            },
            {
                "pct_of_assets_in_top_15": "51.15%",
                "etf_database_category_average": "52.16%",
                "factset_segment_average": "65.06%",
            },
            {
                "pct_of_assets_in_top_50": "83.62%",
                "etf_database_category_average": "81.26%",
                "factset_segment_average": "81.64%",
            },
        ],
        "size_comparison": [
            {
                "large_(>12.9b)": "98.31%",
                "etf_database_category_average": "86.63%",
                "factset_segment_average": "46.30%",
            },
            {
                "mid_(>2.7b)": "1.49%",
                "etf_database_category_average": "5.88%",
                "factset_segment_average": "3.26%",
            },
            {
                "small_(>600m)": "0.00%",
                "etf_database_category_average": "0.58%",
                "factset_segment_average": "0.09%",
            },
            {
                "micro_(<600m)": "0.00%",
                "etf_database_category_average": "0.12%",
                "factset_segment_average": "0.01%",
            },
        ],
    },
    "holdings_analysis": [
        {"North, Central and South America": 99.87, "Other": 0.2},
        {
            "United States": 96.79,
            "Ireland": 1.61,
            "United Kingdom": 0.66,
            "Switzerland": 0.43,
            "Other": 0.2,
            "Netherlands": 0.14,
            "Canada": 0.13,
            "Bermuda": 0.11,
        },
        {
            "Technology Services": 21.08,
            "Electronic Technology": 18.45,
            "Finance": 12.34,
            "Health Technology": 9.51,
            "Retail Trade": 7.75,
            "Consumer Non-Durables": 4.48,
            "Producer Manufacturing": 3.61,
            "Consumer Services": 3.4,
            "Energy Minerals": 3.11,
            "Commercial Services": 2.92,
            "Utilities": 2.25,
            "Health Services": 2.21,
            "Consumer Durables": 1.91,
            "Process Industries": 1.78,
            "Transportation": 1.76,
            "Communications": 0.93,
            "Distribution Services": 0.92,
            "Industrial Services": 0.92,
            "Non-Energy Minerals": 0.54,
            "CASH": 0.2,
        },
        {"Large": 98.31, "Mid": 1.49, "Small": 0, "Micro": 0},
        {},
        {"Share/Common/Ordinary": 99.87, "CASH": 0.2},
        {
            "Technology Services": 21.08,
            "Electronic Technology": 18.45,
            "Finance": 12.34,
            "Health Technology": 9.51,
            "Retail Trade": 7.75,
            "Consumer Non-Durables": 4.48,
            "Producer Manufacturing": 3.61,
            "Consumer Services": 3.4,
            "Energy Minerals": 3.11,
            "Commercial Services": 2.92,
            "Utilities": 2.25,
            "Health Services": 2.21,
            "Consumer Durables": 1.91,
            "Process Industries": 1.78,
            "Transportation": 1.76,
            "Communications": 0.93,
            "Distribution Services": 0.92,
            "Industrial Services": 0.92,
            "Non-Energy Minerals": 0.54,
            "CASH": 0.2,
        },
    ],
    "performance": [
        {
            "1_month_return": "3.05%",
            "etf_database_category_average": "2.89%",
            "factset_segment_average": None,
        },
        {
            "3_month_return": "15.68%",
            "etf_database_category_average": "16.58%",
            "factset_segment_average": None,
        },
        {
            "ytd_return": "2.66%",
            "etf_database_category_average": "2.55%",
            "factset_segment_average": None,
        },
        {
            "1_year_return": "23.86%",
            "etf_database_category_average": "24.93%",
            "factset_segment_average": None,
        },
        {
            "3_year_return": "10.10%",
            "etf_database_category_average": "5.02%",
            "factset_segment_average": None,
        },
        {
            "5_year_return": "15.07%",
            "etf_database_category_average": "8.85%",
            "factset_segment_average": None,
        },
    ],
    "dividends": [
        {
            "dividend": "$ 1.93",
            "etf_database_category_average": "$ 0.35",
            "factset_segment_average": "$ 0.22",
        },
        {
            "dividend_date": "2023-12-20",
            "etf_database_category_average": "N/A",
            "factset_segment_average": "N/A",
        },
        {
            "annual_dividend_rate": "$ 6.90",
            "etf_database_category_average": "$ 0.92",
            "factset_segment_average": "$ 0.64",
        },
        {
            "annual_dividend_yield": "1.41%",
            "etf_database_category_average": "1.11%",
            "factset_segment_average": "1.42%",
        },
    ],
    "technicals": {
        "indicators": {
            "20_day_ma": "$478.81",
            "60_day_ma": "$461.74",
            "macd_15_period": "10.67",
            "macd_100_period": "40.06",
            "williams_%_range_10_day": "4.05",
            "williams_%_range_20_day": "3.43",
            "rsi_10_day": "77",
            "rsi_20_day": "71",
            "rsi_30_day": "68",
            "ultimate_oscillator": "65",
            "lower_bollinger_(10_day)": "$471.45",
            "upper_bollinger_(10_day)": "$492.45",
            "lower_bollinger_(20_day)": "$467.48",
            "upper_bollinger_(20_day)": "$489.54",
            "lower_bollinger_(30_day)": "$465.05",
            "upper_bollinger_(30_day)": "$488.05",
            "support_level_1": "n/a",
            "support_level_2": "$486.67",
            "resistance_level_1": "n/a",
            "resistance_level_2": "$492.45",
            "stochastic_oscillator_%d_(1_day)": "63.66",
            "stochastic_oscillator_%d_(5_day)": "86.50",
            "stochastic_oscillator_%k_(1_day)": "63.23",
            "stochastic_oscillator_%k_(5_day)": "80.88",
            "tracking_difference_median_(%)": "-0.03",
            "tracking_difference_max_upside_(%)": "-0.02",
            "tracking_difference_max_downside_(%)": "-0.06",
            "median_premium_discount_(%)": "0.01",
            "maximum_premium_discount_(%)": "0.07",
            "average_spread_(%)": "2.01",
            "average_spread_($)": "2.01",
        },
        "volatility": {
            "5_day_volatility": ["193.65%"],
            "20_day_volatility": ["8.87%"],
            "50_day_volatility": ["9.26%"],
            "200_day_volatility": ["11.69%"],
            "beta": ["1.0"],
            "standard_deviation": ["25.88%"],
        },
    },
    "realtime_rankings": [
        {
            "metric": "Liquidity",
            "metric_realtime_rating": "A",
            "a+_metric_rated_etf": "SPY",
        },
        {
            "metric": "Expenses",
            "metric_realtime_rating": "A",
            "a+_metric_rated_etf": "BKLC",
        },
        {
            "metric": "Performance",
            "metric_realtime_rating": "B",
            "a+_metric_rated_etf": "ESPO",
        },
        {
            "metric": "Volatility",
            "metric_realtime_rating": "B+",
            "a+_metric_rated_etf": "NUSI",
        },
        {
            "metric": "Dividend",
            "metric_realtime_rating": "A-",
            "a+_metric_rated_etf": "QYLD",
        },
        {
            "metric": "Concentration",
            "metric_realtime_rating": "A-",
            "a+_metric_rated_etf": "VT",
        },
    ],
}

```
## Help Needed!
I am working full-time, and as such don't have much time to constantly push commits or updates. I will appreciate if some help can be provided, such as: 
* Unit tests for the current code
* ETF Category has yet to be updated

## Disclaimer 
This package is built with some reference to the existing [pyetf](https://github.com/JakubPluta/pyetf) package.

## Contributing
Pull requests are welcome.

## License
GPLv3 