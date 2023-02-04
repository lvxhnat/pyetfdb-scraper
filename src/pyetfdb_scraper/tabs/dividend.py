from bs4.element import ResultSet
from pyetfdb_scraper.utils import _scrape_table, etfdividend_regex_header


def get_dividend(ticker_profile_soup: ResultSet):
    """Dividend Tab"""
    table_tag = (
        ticker_profile_soup.find(
            "div", {"id": "etf-ticker-valuation-dividend_tab"}
        )
        .find("div", {"id": "dividend-table"})
        .find("table")
    )
    return _scrape_table(
        ticker_profile_soup,
        tag=table_tag,
        columns=4,
        text=etfdividend_regex_header,
    )
