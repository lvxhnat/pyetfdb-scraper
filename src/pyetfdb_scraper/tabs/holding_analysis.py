import json
from bs4.element import ResultSet


def get_holdings_analysis(ticker_profile_soup: ResultSet):
    """Holdings Analysis Charts

    Example Return
    ===============
    [{'Sovereign': 99.95, 'CASH': 0.06},
    {},
    {'Less Than 1 Year': 0,
    '1-3 Years': 0,
    '3-5 Years': 0,
    '5-7 Years': 0,
    '7-10 Years': 0,
    '10-15 Years': 0,
    '15-20 Years': 0,
    '20-30 Years': 0,
    '30+ Years': 0},
    {'Sovereign': 99.95, 'CASH': 0.06}]
    """
    charts_data = ticker_profile_soup.find_all("table", class_="chart base-table")

    parse_data = []
    chart_series = [x.get("data-chart-series") for x in charts_data]
    chart_titles = [x.get("data-title").replace("<br>", " ") for x in charts_data]
    chart_series_dicts = [json.loads(series) for series in chart_series]
    for chart_dict in chart_series_dicts:
        parse_data.append({x["name"]: x["data"][0] for x in chart_dict})

    return parse_data
