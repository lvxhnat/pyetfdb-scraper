from bs4.element import ResultSet
from pyetfdb_scraper.utils import (
    get_nested,
)

def get_performance(ticker_profile_soup: ResultSet):
    """Performance Tab"""
    table_tag = ticker_profile_soup.find("div", {"id": "performance_tab"}).find("table")
    headers_tag = table_tag.find_all("th")
    headers = [
        " ".join([tag.replace("\n", "") for tag in i.contents if isinstance(tag, str)])
        for i in headers_tag
    ]

    table_body = [tr_tag.find_all("td") for tr_tag in table_tag.find_all("tr")]
    results = []

    for body_el in table_body:
        if len(body_el) == 0:
            continue
        d = {}
        for index, header in enumerate(headers):
            d[header] = "".join(body_el[index].contents).replace("\n", "")
        results.append(d)
        
    ticker = ""
    try: ticker = [*results[0].keys()][1] 
    except: pass
    
    return [{
        "_".join(d[""].lower().split(" ")): get_nested(d, [ticker]),
        "etf_database_category_average": get_nested(d, ['ETF Database Category Average']),
        "factset_segment_average": get_nested(d, ['FactSet Segment Average']),
    } for d in results]
