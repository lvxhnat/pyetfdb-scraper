from bs4.element import ResultSet, Tag
from pyetfdb_scraper.utils import _scrape_table, taxanalysis_regex_header, get_nested


def get_expense(ticker_profile_soup: ResultSet):
    return {
        "tax_analysis": get_tax_analysis(
            ticker_profile_soup=ticker_profile_soup
        ),
        "expense_ratio_analysis": get_expense_ratio_analysis(
            ticker_profile_soup=ticker_profile_soup
        ),
    }


def get_tax_analysis(ticker_profile_soup: ResultSet):
    """Expense Ratio & Fees Tab"""
    table_tag = ticker_profile_soup.find("div", {"id": "expense_tab"}).find(
        "table"
    )
    data = _scrape_table(
        ticker_profile_soup, tag=table_tag, text=taxanalysis_regex_header
    )
    return {
        "max_short_term_capital_gains_rate": get_nested(data, ['data', 'Max ST Capital Gains Rate']),
        "max_long_term_capital_gains_rate": get_nested(data, ['data', 'Max LT Capital Gains Rate']),
        "tax_on_distributions": get_nested(data, ['data', 'Tax On Distributions']),
        "distributes_k1": get_nested(data, ['data', 'Distributes K1'])
    }


def get_expense_ratio_analysis(ticker_profile_soup: ResultSet):
    """Expense Ratio & Fees Tab"""
    item = ticker_profile_soup.find("div", {"id": "expense_tab"}).find_all(
        "div", class_="row"
    )[3]
    expense_rations = [
        [*filter(lambda s: isinstance(s, Tag), tag.contents)]
        for tag in item.find_all(
            "div", {"class": "col-md-4 col-sm-4 col-xs-4"}
        )
    ]

    return [
            {"_".join("".join(entry[0].contents).lower().split(" ")): "".join(entry[3].contents)}
            for entry in expense_rations
        ]