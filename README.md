# Python Web Scraping
This repository contains a Python-based web scraper built using the Scrapy framework. The scraper is designed to collect book data from online sources, such as online bookstores and libraries. The collected data can include titles, authors, prices, publication dates, and other relevant information.


### Scrapy vs. BeautifulSoup
- Scrapy is a comprehensive Python framework designed for web scraping and crawling. It provides a full suite of tools for making HTTP requests, parsing web pages, and organizing data. It’s well-suited for complex and large-scale scraping projects.

- Beautiful Soup is a Python library focused on parsing HTML and XML documents to extract data. It is often used in combination with external HTTP clients, like requests, to handle the scraping part.

Choose BeautifulSoup for a simple way to scrape static HTML content from a web page quickly. Scrapy is ideal for large-scale web scraping that requires extracting content from multiple web pages.

## Getting Started
To get this project up and running on your local machine, follow these steps

#### Clone the repository
```sh
git clone https://github.com/nattanan-cm/python-web-scraping.git
cd python-web-scraping
```

#### Create and activate a virtual environment (optional but recommended)
```sh
python -m venv <your_env_name>
$ source <your_env_name>/bin/activate # For macOS/Linux
$ <your_env_name>\Scripts\activate # For Windows
```


#### Install the required packages
```sh
pip install scrapy ipython
```

### Start Scrapy project
```sh
scrapy startproject <your_project_name>
scrapy startproject book_scraping # For this example
```

### Generate spider
```sh
cd /<path>/spiders
scrapy genspider book_spider <your_scrape_site>
scrapy genspider book_spider books.toscrape.com # For this example
```

### Run spider
```sh
scrapy crawl <your_spider_name>
scrapy crawl book_spider # For this example
```

### Configure Scrapy shell
scrapy.cfg
```
[settings]
default = book_scraping.settings
shell = ipython # Right here
```


## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## Contact
<picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" /> </picture
