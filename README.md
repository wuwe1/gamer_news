# gamer_news 🕹
![scrape-workflow-badge](https://github.com/wuwe1/gamer_news/workflows/Scrape%20latest%20data/badge.svg)

A game news aggregrator 

![wx mini program](https://tva1.sinaimg.cn/large/0081Kckwly1gkhse4cd5dj30by0bydht.jpg)

scan the qr code the to the wechat miniprogram

view the news on [git-history](https://github.githistory.xyz/wuwe1/gamer_news/blob/master/spider/items.jl)

Currently supported site:
- https://indienova.com/channel/news
- https://www.gamersky.com/news/pc/zx/
- https://www.gcores.com/news
- http://www.gamelook.com.cn/page/2
- http://www.sfw.cn/game
- https://gnn.gamer.com.tw/
- https://gouhuo.qq.com/
- http://nga.cn/v/games/
- https://www.vgtime.com/topic/index.jhtml
- http://www.ign.xn--fiqs8s/ 

## How it works
`spider/` directory holds a scrapy script will extract the news on the sites above

`app/` directory holds a RESTful api for the news

github actions will run the scrapy script on `42 */4 * * *` (At minute 42 past every 4th hour)


## USAGE
- spider
    - `pip install scrapy`
    - `cd spider`
    - `chmod +x spider/run_spider.sh`
    - `./spider/run_spider.sh`

- app
    - `pip install uvicorn`
    - `cd app`
    - `uvicorn app.main:app --reload`
