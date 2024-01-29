import os 
import json
from typing import List
from pyetfdb_scraper.etf_scraper import ETFScraper

class ETF(ETFScraper):
    def __init__(self, ticker: str):
        super().__init__(ticker)

    @property
    def base_info(
        self,
    ):
        return self._get_base_etf_info()

    @property
    def info(
        self,
    ):
        info = self._get_etf_info()
        info['vitals']['etf_name'] = self.base_info['etf_name']
        
        return info

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


def load_etfs() -> List[str]:
    tickers: dict = {etf.get("symbol"): etf for etf in load_ticker_list()}
    return list(tickers.keys())

def load_ticker_list() -> list:
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "etfdb.json"
    )
    with open(path, "r") as f:
        data = json.load(f)
    return data