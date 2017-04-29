from argparse import ArgumentParser
from re import findall
from sys import exit
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def get_rss(url: str) -> str:
    try:
        response = urlopen(Request(url))
    except HTTPError as e:
        print('[-] Error code: ', e.code)
        exit(1)
    except URLError as e:
        print('[-] Reason: ', e.reason)
        exit(1)
    else:
        rss_str = findall(r'channel-external-id="(.*?)"', response.read().decode('utf-8').strip())[1]

    return 'https://www.youtube.com/feeds/videos.xml?channel_id=' + rss_str

if __name__ == '__main__':
    parser = ArgumentParser(description='Fetches the RSS feed url of a given youtube channel.')
    parser.add_argument('url', help='The full youtube channel url.')
    print('[+] RSS Url: ', get_rss(parser.parse_args().url))
