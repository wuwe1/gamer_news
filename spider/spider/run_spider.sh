if [ -e items.jl ] ; then
    rm items.jl
fi

/root/miniconda3/bin/python -m scrapy list | xargs -n 1 scrapy crawl

/root/miniconda3/bin/python ./add_to_mp_database.py

git config user.name "wuwe1"
git config user.email "wu_we1@outlook.com"
git add -A
timestamp=$(date -u)
git commit -m "Latest data: ${timestamp}" || exit 0
git push