from bs4.element import ResultSet
from pyetfdb_scraper.utils import _scrape_table, ratings_regex_header


def get_realtime_ratings(ticker_profile_soup: ResultSet):
    """Realtime Ratings Tab"""
    ratings_tag = ticker_profile_soup.find(
        "div", {"id": "realtime-collapse"}
    ).find("table")
    return _scrape_table(
        ticker_profile_soup,
        text=ratings_regex_header,
        tag=ratings_tag,
        columns=3,
    )
