if [ -e items.jl ] ; then
    rm items.jl
fi

scrapy list | xargs -n 1 scrapy crawl

python ./add_to_mp_database.py

git config user.name "Automated"
git config user.email "actions@users.noreply.github.com"
git add -A
timestamp=$(date -u)
git commit -m "Latest data: ${timestamp}" || exit 0
git push