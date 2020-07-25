## USAGE
- spider
    - `pip install scrapy`
    - `cd spider`
    - `scrapy list | xargs -n 1 scrapy crawl`

- app
    - `uvicorn app.main:app --reload`