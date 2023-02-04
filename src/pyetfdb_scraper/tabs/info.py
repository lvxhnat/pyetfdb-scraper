from bs4.element import ResultSet, Tag
from pyetfdb_scraper.utils import (
    _scrape_div_class_ticker_assets,
    _scrape_table,
    jump_siblings,
    unpack_tag_contents,
    h4_regex,
    factset_regex_header,
    vitals_regex_header,
    dbtheme_regex_header,
    tradedata_regex_header,
    histdata_regex_header,
    altetfs2_regex_header,
    altetfs_regex_header,
)


def get_info(ticker_profile_soup: ResultSet):
    return {
        "vitals": _get_vitals(ticker_profile_soup=ticker_profile_soup),
        "dbtheme": _get_dbtheme(ticker_profile_soup=ticker_profile_soup),
        "fact_set": _get_factset(ticker_profile_soup=ticker_profile_soup),
        "analyst_report": _get_analyst_report(
            ticker_profile_soup=ticker_profile_soup
        ),
        "trade_data": _get_tradedata(ticker_profile_soup=ticker_profile_soup),
        "historical_trade_data": _get_historicaltradedata(
            ticker_profile_soup=ticker_profile_soup
        ),
        "alternative_etfs": _get_altetfs(
            ticker_profile_soup=ticker_profile_soup
        ),
        "other_alternative_etfs": _get_altetfs2(
            ticker_profile_soup=ticker_profile_soup
        ),
    }


# Get the actual data tables
def _get_vitals(ticker_profile_soup: ResultSet):
    """_summary_

    Example Return
    ===============
    {
        'type': 'list',
        'header': 'Vitals',
        'data': {
            'issuer': {'text': 'BlackRock Financial Management', 'link': '/issuer/blackrock-financial-management/'},
            'brand': {'text': 'iShares', 'link': '/issuer/ishares/'},
            'structure': {'text': 'Grantor Trust', 'link': ''},
            'expense_ratio': {'text': '0.25%', 'link': ''},
            'etf_home_page': {'text': 'Home page', 'link': 'http://us.ishares.com/product_info/fund/overview/IAU.htm?qt=IAU'},
            'inception': {'text': 'Jan 21, 2005', 'link': ''},
            'index_tracked': {'text': 'LBMA Gold Price PM ($/ozt)', 'link': '/index/lbma-gold-price-pm-ozt/'}
            }
    }
    """
    return _scrape_div_class_ticker_assets(
        ticker_profile_soup, vitals_regex_header
    )


def _get_dbtheme(ticker_profile_soup: ResultSet):
    """_summary_

    Example Return
    ===============
    {
        'type': 'list',
        'header': 'ETF Database Themes',
        'data': {
            'category': {'text': 'Precious Metals', 'link': ''},
            'asset_class': {'text': 'Commodity', 'link': '/etfs/commodity/'},
            'commodity_type': {'text': 'Precious Metals', 'link': '/etfs/natural-resources/precious-metals/'},
            'commodity': {'text': 'Gold', 'link': '/etfs/commodity/gold/'},
            'commodity_exposure': {'text': 'Physically-Backed', 'link': '/etfs/commodity-exposure/physically-backed/'}
        }
    }
    """
    return _scrape_div_class_ticker_assets(
        ticker_profile_soup, dbtheme_regex_header
    )


def _get_factset(ticker_profile_soup: ResultSet):
    """_summary_

    Example Return
    ===============
    {
        'type': 'table-horizontal',
        'header': 'FactSet Classifications'
        'data': {
            'Segment': ['Commodities: Precious Metals Gold'],
            'Category': ['Precious Metals'],
            'Focus': ['Gold'],
            'Niche': ['Physically Held'],
            'Strategy': ['Vanilla'],
            'Weighting Scheme': ['Single Asset']
        },
    }
    """
    return _scrape_table(ticker_profile_soup, text=factset_regex_header)


def _get_analyst_report(ticker_profile_soup: ResultSet):
    """Get the text description of the ETF based on Analyst Report

    Example Return
    ===============
    'This fund offers exposure to one of the world’s most famous metals, gold.....'
    """
    for entry in ticker_profile_soup.find("div", class_="row").find_all("p"):
        # Make sure the tags arent empty. since tags like <p></p> exists.
        if entry.contents:
            # Remove tags like <caps> in our description string
            cleaned_desc = "".join(
                [
                    *map(
                        lambda s: unpack_tag_contents(s)
                        if not isinstance(s, str)
                        else s,
                        entry.contents,
                    )
                ]
            )
    return cleaned_desc


def _get_tradedata(ticker_profile_soup: ResultSet):
    """
    Example Return
    ===============
    {
        'Open': '',
        'Volume': '',
        'Day Lo': '',
        'Day Hi': '',
        '52 Week Lo': '$30.69',
        '52 Week Hi': '$39.36',
        'AUM': '$28,058.7 M',
        'Shares': '768.1 M'
    },
    """

    list_tag: Tag = jump_siblings(
        ticker_profile_soup.find(
            "h3", class_=h4_regex, text=tradedata_regex_header
        ),
        4,
    )
    list_rows = list_tag.find_all("li")
    aum_rows = jump_siblings(list_tag, 4).find_all("li")
    list_rows += aum_rows

    list_dict = {}

    for i in range(0, len(list_rows)):
        cleaned_content = [
            "".join(i.contents) for i in list_rows[i] if isinstance(i, Tag)
        ]
        list_dict[cleaned_content[0]] = cleaned_content[1]

    return list_dict


def _get_historicaltradedata(ticker_profile_soup: ResultSet):
    """
    Example Return
    ===============
    {
        '1 Month Avg. Volume': '5,263,078',
        '3 Month Avg. Volume': '4,885,578'
    }
    """
    list_tag = jump_siblings(
        ticker_profile_soup.find(
            "h3", class_=h4_regex, text=histdata_regex_header
        ),
        2,
    )
    list_rows = list_tag.find_all("li")

    list_dict = {}

    for i in range(0, len(list_rows)):
        cleaned_content = [
            "".join(i.contents) for i in list_rows[i] if isinstance(i, Tag)
        ]
        list_dict[cleaned_content[0]] = cleaned_content[1]

    return {
        "type": "list",
        "data": list_dict,
        "header": "Historical Trade Data",
    }


def _get_altetfs(ticker_profile_soup: ResultSet):

    """_summary_

    Example Return
    ===============
    {
        'type': 'table-vertical',
        'data': [
            {'Type': 'Cheapest', 'Ticker': 'GLDM', 'Expense Ratio': '0.10%', 'Assets': '$5.9 B', 'Avg. Daily Vol': '2 M', 'YTD Return': '4.89%'},
            {'Type': 'Largest (AUM)', 'Ticker': 'GLD', 'Expense Ratio': '0.40%', 'Assets': '$57.0 B', 'Avg. Daily Vol': '6 M', 'YTD Return': '4.87%'},
            {'Type': 'Most Liquid (Volume)', 'Ticker': 'SLV', 'Expense Ratio': '0.50%', 'Assets': '$11.2 B', 'Avg. Daily Vol': '18 M', 'YTD Return': '-2.04%'},
            {'Type': 'Top YTD Performer', 'Ticker': 'BAR', 'Expense Ratio': '0.17%', 'Assets': '$955.6 M', 'Avg. Daily Vol': '486,063', 'YTD Return': '4.93%'}
        ],
        'header': 'Alternative ETFs in the ETF'
    }
    """
    return _scrape_table(
        ticker_profile_soup, text=altetfs_regex_header, columns=6
    )


def _get_altetfs2(ticker_profile_soup: ResultSet):
    """_summary_

    Example Return
    ===============
    {
        'type': 'table-vertical',
        'data': [
            {'Type': 'Cheapest', 'Ticker': 'GLDM', 'Expense Ratio': '0.10%', 'Assets': '$5.9 B', 'Avg. Daily Vol': '2 M', 'YTD Return': '4.89%'},
            {'Type': 'Largest (AUM)', 'Ticker': 'GLD', 'Expense Ratio': '0.40%', 'Assets': '$57.0 B', 'Avg. Daily Vol': '6 M', 'YTD Return': '4.87%'},
            {'Type': 'Most Liquid (Volume)', 'Ticker': 'GLD', 'Expense Ratio': '0.40%', 'Assets': '$57.0 B', 'Avg. Daily Vol': '6 M', 'YTD Return': '4.87%'},
            {'Type': 'Top YTD Performer', 'Ticker': 'BAR', 'Expense Ratio': '0.17%', 'Assets': '$955.6 M', 'Avg. Daily Vol': '486,063', 'YTD Return': '4.93%'}
        ],
        'header': 'Alternative ETFs in the FactSet'}
    }
    """
    return _scrape_table(
        ticker_profile_soup, text=altetfs2_regex_header, columns=6
    )
