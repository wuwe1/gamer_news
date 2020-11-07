if [ -e items.jl ] ; then
    rm items.jl
fi

scrapy list | xargs -n 1 scrapy crawl