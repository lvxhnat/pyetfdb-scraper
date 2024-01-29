import os
import time
import random
import warnings
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import NewConnectionError

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
from pyetfdb_scraper.models import InfoModel, BaseInfoModel, ExpenseModel

class ETFScraper(object):
    
    def __init__(
        self, 
        ticker: str,
        user_agent: str = None,
    ):

        self.ticker = ticker
        self.base_url: str = "https://etfdb.com/etf"

        self.user_agents = load_user_agents()
        self.request_headers: dict = {
            "User-Agent": user_agent if not user_agent else random.choice(self.user_agents),
            "Referer": "https://etfdb.com/etfs/QQQ"
        }
        self.scrape_url: str = f"{self.base_url}/{ticker}"

        soup = self.__request_ticker()

        self.etf_ticker_body_soup = soup.find("div", {"id": "etf-ticker-body"})

    def __request_ticker(self, retries: int = 2) -> BeautifulSoup:
        try:
            print(f"Requesting for {self.ticker}", "\t\t")
            response: requests.Response = requests.get(
                self.scrape_url, headers=self.request_headers
            )
            print(f"Completed Requested for {self.ticker}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features="lxml")
                return soup
            elif response.status_code == 429:
                warnings.warn(
                    "Too many requests. Sleeping for 60 seconds and retrying..."
                )
                time.sleep(60)
                response: requests.Response = requests.get(
                    self.scrape_url, headers=self.request_headers
                )
                soup = BeautifulSoup(response.text)
                return soup
            else:
                raise Exception(
                    f"Request failed for {self.scrape_url}. Response code {str(response.status_code)}. Error string {response.text}"
                )
        except Exception as error:
            if retries:
                print(f"Exception raised. Retrying for {retries} time. Error code is {str(error)}")
                time.sleep(random.randrange(5))
                self.__request_ticker(retries=retries - 1)
            else:
                print(f"Reduced retries. Sleeping for 15 mins. Current symbol is {self.ticker}")
                time.sleep(15 * 60)

    def _get_base_etf_info(
        self,
    ) -> BaseInfoModel:
        return {
            "etf_name": " ".join(
                self.etf_ticker_body_soup.find("h2").contents
            ).replace("\n", ""),
        }

    def _get_etf_info(
        self,
    ) -> InfoModel:
        return get_info(self.etf_ticker_body_soup)

    def _get_etf_expense(
        self,
    ) -> ExpenseModel:
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

def load_user_agents() -> list:
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "user-agents.txt"
    )
    with open(path, "r") as f:
        return f.read().split("\n")

