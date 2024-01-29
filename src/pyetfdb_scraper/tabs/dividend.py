from bs4.element import ResultSet
from pyetfdb_scraper.utils import get_nested, _scrape_table, etfdividend_regex_header


def get_dividend(ticker_profile_soup: ResultSet):
    """Dividend Tab"""
    table_tag = (
        ticker_profile_soup.find(
            "div", {"id": "etf-ticker-valuation-dividend_tab"}
        )
        .find("div", {"id": "dividend-table"})
        .find("table")
    )
    data = _scrape_table(
        ticker_profile_soup,
        tag=table_tag,
        columns=4,
        text=etfdividend_regex_header,
    )['data']
    
    return [{
        "_".join(d[''].lower().replace("%", "pct").split(" ")).strip("_"): get_nested(d, ["Fund"]),
        "etf_database_category_average": get_nested(d, ['ETF Database Category Average']),
        "factset_segment_average": get_nested(d, ['FactSet Segment Average']),
    } for d in data]