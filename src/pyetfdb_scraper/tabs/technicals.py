from bs4.element import ResultSet
from pyetfdb_scraper.utils import (
    jump_siblings,
    _scrape_table,
    h4_regex,
    volatility_regex_header,
)


def get_technicals(ticker_profile_soup: ResultSet):
    return {
        "indicators": get_indicators(ticker_profile_soup=ticker_profile_soup),
        "volatility": get_volatility(ticker_profile_soup=ticker_profile_soup),
    }


def get_indicators(ticker_profile_soup: ResultSet):
    """Technicals Tab"""
    sections = [
        x
        for x in ticker_profile_soup.find(
            "div", {"id": "technicals-collapse"}
        ).find_all("ul", class_="list-unstyled")
    ]
    results = []
    for section in sections:
        try:
            results += [
                s.text.strip().split("\n") for s in section.find_all("li")
            ]
        except (KeyError, TypeError) as e:
            print(e)
    return dict(results)


def get_volatility(ticker_profile_soup: ResultSet):
    """Technicals Tab"""
    vol_tag = jump_siblings(
        ticker_profile_soup.find(
            "h3", class_=h4_regex, text=volatility_regex_header
        ),
        4,
    ).find("table")
    return _scrape_table(
        ticker_profile_soup, text=volatility_regex_header, tag=vol_tag
    )
