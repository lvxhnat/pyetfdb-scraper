import os
import json
import time
import warnings
import requests
from typing import List
from pyetfdb_scraper.tabs import (
    get_info,
    get_expense,
    get_holdings,
    get_holdings_analysis,
    get_performance,
    get_dividend,
    get_technicals,
    get_realtime_ratings,
)
from bs4 import BeautifulSoup


class ETFScraper(object):
    def __init__(self, ticker: str):

        self.ticker = ticker
        base_url: str = "https://etfdb.com/etf/"

        request_headers: dict = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "application/json",
        }

        response: requests.Response = requests.get(
            f"{base_url}/{ticker}", headers=request_headers
        )

        if response.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.text)
        elif response.status_code == 429: 
            warnings.warn("Too many requests. Sleeping for 60 seconds and retrying...")
            time.sleep(60)
            response: requests.Response = requests.get(
                f"{base_url}/{ticker}", headers=request_headers
            )
            soup: BeautifulSoup = BeautifulSoup(response.text)
        else: 
            raise Exception(f"Request failed. Response code {str(response.status_code)}. Error string {response.text}")
        
        self.etf_ticker_body_soup = soup.find("div", {"id": "etf-ticker-body"})

    def _get_etf_info(
        self,
    ):
        return get_info(self.etf_ticker_body_soup)

    def _get_etf_expense(
        self,
    ):
        return get_expense(self.etf_ticker_body_soup)

    def _get_etf_holdings(
        self,
    ):
        return get_holdings(self.etf_ticker_body_soup)

    def _get_etf_holdings_analysis(
        self,
    ):
        return get_holdings_analysis(self.etf_ticker_body_soup)

    def _get_etf_performance(
        self,
    ):
        return get_performance(self.etf_ticker_body_soup)

    def _get_etf_dividend(
        self,
    ):
        return get_dividend(self.etf_ticker_body_soup)

    def _get_etf_technicals(
        self,
    ):
        return get_technicals(self.etf_ticker_body_soup)

    def _get_etf_realtime_rankings(
        self,
    ):
        return get_realtime_ratings(self.etf_ticker_body_soup)


class ETF(ETFScraper):
    def __init__(self, ticker: str):
        super().__init__(ticker)

    @property
    def info(
        self,
    ):
        return self._get_etf_info()

    @property
    def expense(
        self,
    ):
        return self._get_etf_expense()

    @property
    def holdings(
        self,
    ):
        return self._get_etf_holdings()

    @property
    def holdings_analysis(
        self,
    ):
        return self._get_etf_holdings_analysis()

    @property
    def performance(
        self,
    ):
        return self._get_etf_performance()

    @property
    def dividend(
        self,
    ):
        return self._get_etf_dividend()

    @property
    def technicals(
        self,
    ):
        return self._get_etf_technicals()

    @property
    def realtime_rankings(
        self,
    ):
        return self._get_etf_realtime_rankings()

    def to_dict(
        self,
    ):
        return {
            "info": self.info,
            "expense": self.expense,
            "holdings": self.holdings,
            "holdings_analysis": self.holdings_analysis,
            "performance": self.performance,
            "dividends": self.dividend,
            "technicals": self.technicals,
            "realtime_rankings": self.realtime_rankings,
        }


def load_ticker_list() -> list:
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "etfdb.json"
    )
    with open(path, "r") as f:
        data = json.load(f)
    return data


def load_etfs() -> List[str]:
    tickers: dict = {etf.get("symbol"): etf for etf in load_ticker_list()}
    return list(tickers.keys())
