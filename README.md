# gamer-news 🕹
A game news aggregrator 

github actions will run the scrapy script on `42 */4 * * *` (At minute 42 past every 4th hour)

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
