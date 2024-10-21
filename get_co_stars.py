import requests
import asyncio


def get_co_stars(actor_name):
    titles_url = 'http://localhost:8983/solr/titles/query?q=%7B!parent%20which%3D\'content_type:parentDocument\'%7Dname:"' + actor_name.replace(' ', '%20') + '"&q.op=AND&indent=true&fl=id'

    titles = requests.get(titles_url)

    for title in titles.json()['response']['docs']:
        co_stars_url = 'http://localhost:8983/solr/titles/query?q=%7B!child%20of%3D\'content_type:parentDocument\'%7Did:"' + title['id'] + '"&q.op=AND&indent=true&fl=name'
        co_stars = requests.get(co_stars_url)
        for co_star in co_stars.json()['response']['docs']:
            print(co_star['name']) if co_star['name'] != actor_name else None

def main():
    get_co_stars('Christina Hendricks')

if __name__ == '__main__':
    main()