import re
from typing import Union
from bs4.element import ResultSet, Tag

h4_regex = re.compile("h4")

vitals_regex_header = re.compile("Vitals")
dbtheme_regex_header = re.compile("ETF Database Themes")
factset_regex_header = re.compile("FactSet Classifications")
tradedata_regex_header = re.compile("Trading Data")
histdata_regex_header = re.compile("Historical Trading Data")
altetfs_regex_header = re.compile("Alternative ETFs in the ETF")
altetfs2_regex_header = re.compile("Alternative ETFs in the FactSet")

etfdividend_regex_header = re.compile("ETF Dividend")
taxanalysis_regex_header = re.compile("Tax Analysis")

holdingscomparison_regex_header = re.compile("Holding Comparison")
sizecomparison_regex_header = re.compile("Size Comparison")

ratings_regex_header = re.compile("RealTime Ratings")

volatility_regex_header = re.compile("Volatility Analysis")


def jump_siblings(root_tag: Tag, jumps: int) -> Union[Tag, str]:
    """Jump to the next ```jump``` sibling (The number of element tag after the current one stated)"""
    if jumps == 0:
        return root_tag
    else:
        return jump_siblings(root_tag.next_sibling, jumps - 1)


def unpack_tag_contents(tag: Tag) -> str:
    """There are instances where tag contents might contain nested tags. This function unpacks those tags and joins them to form one coherent content. E.g.
    <td><strong><italic> sssss </italic></strong></td> --> ssss
    """
    if isinstance(tag, str):
        return tag.replace("\n", "")
    else:
        return "".join([*map(unpack_tag_contents, tag.contents)])


# Generalised scraper functions
def _scrape_div_class_ticker_assets(
    ticker_profile_soup: ResultSet, text: re.Pattern
):
    """General scraper function to extract text with class tag of 'ticker-assets'"""
    g_tag: Tag = jump_siblings(
        ticker_profile_soup.find("h3", class_=h4_regex, text=text), 2
    )
    g_dict = {}
    for entry in g_tag.find_all("div", class_="row"):
        span_content = entry.find_all("span")

        row_text: str = unpack_tag_contents(span_content[1])

        row_tag: Tag = span_content[1].contents[0]
        row_link: str = ""

        if isinstance(row_tag, Tag):
            if row_tag.has_attr("href"):
                row_link: str = row_tag["href"]

        row_key: str = span_content[0].contents[0]
        g_dict[row_key] = {"text": row_text, "link": row_link}

    return {
        "type": "list",
        "header": text.pattern,
        "data": g_dict,
    }


def _scrape_table(
    ticker_profile_soup: ResultSet,
    text: re.Pattern,
    tag: Tag = None,
    columns: int = 2,
):

    if not tag:
        header_tag: Tag = ticker_profile_soup.find("h3", class_=h4_regex, text=text)
        if header_tag:
            table_rows = jump_siblings(
                header_tag, 2
            )
        else:
            return None
    if tag:
        if isinstance(tag, Tag):
            table_rows = tag
        else:
            raise ValueError(
                f"Tag provided if of type {str(type(tag))} which is not allowed."
            )

    table_dict = {}
    table_content = []

    final_output = {}

    table_rows = table_rows.find_all("td")

    for i in range(0, len(table_rows), columns):
        # print(table_rows[i])
        if table_rows[i + 1].has_attr("data-th"):
            final_output["type"] = "table-vertical"
            entry = {}
            for inc in range(columns):
                # Remove new line if it is a string, otherwise get the contents of the inner tag
                cleaned_content = [
                    *map(unpack_tag_contents, table_rows[i + inc].contents)
                ]
                entry_contents = [item for item in cleaned_content if item]
                entry[table_rows[i + inc]["data-th"]] = (
                    entry_contents[0].replace("\n", "")
                    if entry_contents
                    else ""
                )
            table_content.append(entry)
        else:
            final_output["type"] = "table-horizontal"
            table_dict[table_rows[i].contents[0].replace("\n", "")] = [
                table_rows[i + inc].contents[0].replace("\n", "")
                for inc in range(1, columns)
            ]

    if final_output["type"] == "table-horizontal":
        final_output["data"] = table_dict
    else:
        final_output["data"] = table_content

    final_output["header"] = text.pattern

    return final_output
