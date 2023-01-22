import re
import os
from functions import get, extract_links

import ignition  # type: ignore
ignition.set_default_timeout(4)

ROOT = 'gemini://aperalesf.flounder.online/'
TARGET = 'aperalesf'

CRAWLER = {}


def safe_name(string: str) -> str:
    pattern = re.compile('[^a-zA-Z0-9_]')
    return re.sub(pattern, '_', string)


def store(name, body):
    file = open(TARGET + '/' + name, 'w')
    file.write(body)
    file.flush()
    file.close()


def fetch(url, previous_url):
    url = ignition.url(url, previous_url)

    if not url.startswith(ROOT):
        print(f'Skipping {url}')
        CRAWLER[url] = True
        return

    print(f'Downloading {url} as {safe_name(url)}')
    CRAWLER[url] = True
    res, body = get(url)

    file_data = '\r\n'.join(res.headers) + '\r\n\r\n' + body
    store(safe_name(url), file_data)

    if res.client_status == 3:
        print(f'Found redirect: {res.data}')
        fetch(res.data, url)

    for new_url, title in extract_links(body):
        new_url_normal = ignition.url(new_url, url)
        if new_url_normal in CRAWLER:
            print(f'Found old url: {new_url_normal}')
        else:
            print(f'Found new url: {new_url}')
            fetch(new_url, url)

    return


if not os.path.isdir(TARGET):
    os.mkdir(TARGET)

print(f'Crawling {ROOT} and storing in {TARGET}...')
fetch('/', ROOT)
