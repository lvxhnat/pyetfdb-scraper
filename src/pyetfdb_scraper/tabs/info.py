from bs4.element import ResultSet, Tag
from pyetfdb_scraper.utils import (
    _scrape_div_class_ticker_assets,
    _scrape_table,
    jump_siblings,
    unpack_tag_contents,
    get_nested,
    h4_regex,
    factset_regex_header,
    vitals_regex_header,
    dbtheme_regex_header,
    tradedata_regex_header,
    histdata_regex_header,
    altetfs2_regex_header,
    altetfs_regex_header,
)
from pyetfdb_scraper.models import InfoModel


def get_info(ticker_profile_soup: ResultSet) -> InfoModel:
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
    data = _scrape_div_class_ticker_assets(
        ticker_profile_soup, vitals_regex_header
    )
    
    return {
        "issuer": get_nested(data, ['data', 'data', 'Issuer', 'text']),
        "issuer_link": get_nested(data, ['data', 'data', 'Issuer', 'link']),
        "brand":  get_nested(data, ['data', 'data', 'Brand', 'text']),
        "brand_link":  get_nested(data, ['data', 'data', 'Brand', 'link']),
        "structure":  get_nested(data, ['data', 'data', 'Structure', 'text']),
        "structure_link": get_nested(data, ['data', 'data', 'Structure', 'link']),
        "expense_ratio": get_nested(data, ['data', 'data', 'Expense Ratio', 'text']),
        "hompage_link": get_nested(data, ['data', 'data', 'ETF Home Page', 'link']),
        "inception": get_nested(data, ['data', 'data', 'Inception', 'text']),
        "index_tracked": get_nested(data, ['data', 'data', 'Index Tracked', 'text']),
        "index_tracked_link": get_nested(data, ['data', 'data', 'Index Tracked', 'link']),
    }


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
    data = _scrape_div_class_ticker_assets(
        ticker_profile_soup, dbtheme_regex_header
    )
    
    return {
        "category": get_nested(data, ['data', 'Category', 'text']),
        "category_link": get_nested(data, ['data', 'Category', 'link']),
        "asset_class":  get_nested(data, ['data', 'Asset Class', 'text']),
        "asset_class_link":  get_nested(data, ['data', 'Asset Class', 'link']),
        "asset_class_size":  get_nested(data, ['data', 'Asset Class Size', 'text']),
        "asset_class_size_link": get_nested(data, ['data', 'Asset Class Size', 'link']),
        "asset_class_style": get_nested(data, ['data', 'Asset Class Style', 'text']),
        "asset_class_style_link": get_nested(data, ['data', 'Asset Class Style', 'link']),
        "general_region": get_nested(data, ['data', 'Region (General)', 'text']),
        "general_region_link": get_nested(data, ['data', 'Region (General)', 'link']),
        "specific_region": get_nested(data, ['data', 'Region (Specific)', 'text']),
        "specific_region_link": get_nested(data, ['data', 'Region (Specific)', 'link']),
    }


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
    data = _scrape_table(ticker_profile_soup, text=factset_regex_header)
    return {
        "segment": get_nested(data, ['data', 'fact_set', 'data', 'Segment']),
        "category": get_nested(data, ['data', 'fact_set', 'data', 'Category']),
        "focus": get_nested(data, ['data', 'fact_set', 'data', 'Focus']),
        "niche": get_nested(data, ['data', 'fact_set', 'data', 'Niche']),
        "strategy": get_nested(data, ['data', 'fact_set', 'data', 'Strategy']),
        "weighting_scheme": get_nested(data, ['data', 'fact_set', 'data', 'Weighting Scheme']),
    }


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
    aum_rows = jump_siblings(list_tag, 4)
    aum_rows = aum_rows.find_all("li") if aum_rows else []
    list_rows += aum_rows

    list_dict = {}

    for i in range(0, len(list_rows)):
        cleaned_content = [
            "".join(i.contents) for i in list_rows[i] if isinstance(i, Tag)
        ]
        list_dict[cleaned_content[0]] = cleaned_content[1]

    return {
        "open": get_nested(list_dict, ['data', 'Open']),
        "volume": get_nested(list_dict, ['data', 'Volume']),
        "day_low": get_nested(list_dict, ['data', 'Day Lo']),
        "day_high": get_nested(list_dict, ['data', 'Day Hi']),
        "52_week_low": get_nested(list_dict, ['data', '52 Week Lo']),
        "52_week_high": get_nested(list_dict, ['data', '52 Week Hi']),
        "aum": get_nested(list_dict, ['data', 'AUM']),
        "shares": get_nested(list_dict, ['data', 'Shares']),
    }


def _get_historicaltradedata(ticker_profile_soup: ResultSet):
    """
    Example Return
    ===============
    {'type': 'list',
    'data': {'1 Month Avg. Volume': '80,971,624',
    '3 Month Avg. Volume': '82,142,920'},
    'header': 'Historical Trade Data'}
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
        "1_month_avg_volume": get_nested(list_dict, ['data', '1 Month Avg. Volume']),
        "3_month_avg_volume": get_nested(list_dict, ['data', '3 Month Avg. Volume']),
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
    data = _scrape_table(
        ticker_profile_soup, text=altetfs_regex_header, columns=6
    )
    return [{
        "type": get_nested(input_data, ['Type']),
        "ticker": get_nested(input_data, ['Ticker']),
        "expense_ratio": get_nested(input_data, ['Expense Ratio']),
        "assets": get_nested(input_data, ['Assets']),
        "avg_daily_volume": get_nested(input_data, ['Avg. Daily Vol']),
        "ytd_return": get_nested(input_data, ['YTD Return'])
    } for input_data in get_nested(data, ['data'])]


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
    data = _scrape_table(
        ticker_profile_soup, text=altetfs2_regex_header, columns=6
    )
    return [{
        "type": get_nested(input_data, ['Type']),
        "ticker": get_nested(input_data, ['Ticker']),
        "expense_ratio": get_nested(input_data, ['Expense Ratio']),
        "assets": get_nested(input_data, ['Assets']),
        "avg_daily_volume": get_nested(input_data, ['Avg. Daily Vol']),
        "ytd_return": get_nested(input_data, ['YTD Return'])
    } for input_data in get_nested(data, ['data'])]
