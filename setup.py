from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyetfdb_scraper",
    version="0.2.0",
    author="Yi Kuang",
    author_email="yikuang5@gmail.com",
    description="Scrape ETFs from ETFDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lvxhnat/pyetf-scraper",
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*tests"]),
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "bs4",
    ],
)
