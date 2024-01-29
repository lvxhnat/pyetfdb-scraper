from bs4.element import ResultSet
from pyetfdb_scraper.utils import (
    get_nested,
    _scrape_table,
    sizecomparison_regex_header,
    holdingscomparison_regex_header,
)


def get_holdings(ticker_profile_soup: ResultSet):
    return {
        "top_holdings": _get_top_holdings(
            ticker_profile_soup=ticker_profile_soup
        ),
        "holding_comparison": _get_holding_comparison(
            ticker_profile_soup=ticker_profile_soup
        ),
        "size_comparison": _get_size_comparison(
            ticker_profile_soup=ticker_profile_soup
        ),
    }


def _get_top_holdings(ticker_profile_soup: ResultSet):
    """Holdings Tab

    Example Return
    ===============
    {'type': 'table-vertical',
     'data': [{'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 2.375% 15-MAY-2051',
       'Share': '2.89%',
       'Url': ''},
      {'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 1.75% 15-AUG-2041',
       'Share': '2.74%',
       'Url': ''},
      {'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 2.0% 15-AUG-2051',
       'Share': '2.65%',
       'Url': ''},
      {'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 2.875% 15-MAY-2052',
       'Share': '2.58%',
       'Url': ''},
      {'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 3.0% 15-AUG-2052',
       'Share': '2.56%',
       'Url': ''},
      {'Symbol': 'N/A',
       'Holding': 'United States Treasury Bond 1.875% 15-FEB-2041',
       'Share': '2.56%',
       'Url': ''}, ...
    """
    results = []
    try:
        tbody = ticker_profile_soup.find(
            "div", {"id": "holding_section"}
        ).find("tbody")
        holdings = [x for x in tbody.find_all("tr")]
        for record in holdings:
            record_texts = record.find_all("td")
            try:
                holding_url = "https://etfdb.com" + record.find("a")["href"]
            except TypeError as e:
                holding_url = ""
            texts = dict(
                zip(
                    ["Symbol", "Holding", "Share"],
                    [x.text for x in record_texts],
                )
            )
            texts.update({"Url": holding_url})
            results.append(texts)
    except AttributeError:
        results = []

    return [{
        "symbol": get_nested(d, ["Symbol"]),
        "holding": get_nested(d, ["Holding"]),
        "share": get_nested(d, ["Share"]),
        "url": get_nested(d, ["Url"]),
    } for d in results]


def _get_holding_comparison(ticker_profile_soup: ResultSet):
    """Holdings Tab

    Example Return
    ===============
    {'type': 'table-vertical',
     'data': [{'': 'Number of Holdings',
       'Fund': '73',
       'ETF Database Category Average': '52',
       'FactSet Segment Average': '37'},
      {'': '% of Assets in Top 10',
       'Fund': '25.72%',
       'ETF Database Category Average': '60.98%',
       'FactSet Segment Average': '64.09%'},
      {'': ' % of Assets in Top 15',
       'Fund': '36.59%',
       'ETF Database Category Average': '73.46%',
       'FactSet Segment Average': '74.03%'},
      {'': '% of Assets in Top 50',
       'Fund': '86.69%',
       'ETF Database Category Average': '93.20%',
       'FactSet Segment Average': '94.78%'}],
     'header': 'Holding Comparison'}
    """

    holding_table = ticker_profile_soup.find("table", {"id": "holdings-table"})
    data = _scrape_table(
        ticker_profile_soup,
        text=holdingscomparison_regex_header,
        tag=holding_table,
        columns=4,
    )['data']
    return [{
        "_".join(d[''].lower().replace("%", "pct").split(" ")).strip("_"): get_nested(d, ["Fund"]),
        "etf_database_category_average": get_nested(d, ['ETF Database Category Average']),
        "factset_segment_average": get_nested(d, ['FactSet Segment Average']),
    } for d in data]


def _get_size_comparison(ticker_profile_soup: ResultSet):
    """Holdings Tab

    Example Return
    ===============
    {'type': 'table-vertical',
     'data': [{'': 'Large (>12.9B)',
       'Fund': 'N/A',
       'ETF Database Category Average': 'N/A',
       'FactSet Segment Average': 'N/A'},
      {'': 'Mid (>2.7B)',
       'Fund': 'N/A',
       'ETF Database Category Average': 'N/A',
       'FactSet Segment Average': 'N/A'},
      {'': 'Small (>600M)',
       'Fund': 'N/A',
       'ETF Database Category Average': 'N/A',
       'FactSet Segment Average': 'N/A'},
      {'': 'Micro (<600M)',
       'Fund': 'N/A',
       'ETF Database Category Average': 'N/A',
       'FactSet Segment Average': 'N/A'}],
     'header': 'Size Comparison'}
    """
    size_table = ticker_profile_soup.find("table", {"id": "size-table"})
    data = _scrape_table(
        ticker_profile_soup,
        text=sizecomparison_regex_header,
        tag=size_table,
        columns=4,
    )['data']
    return [{
        "_".join(d[''].lower().replace("%", "pct").split(" ")).strip("_"): get_nested(d, ["Fund"]),
        "etf_database_category_average": get_nested(d, ['ETF Database Category Average']),
        "factset_segment_average": get_nested(d, ['FactSet Segment Average']),
    } for d in data]
