from functions import get, extract_links

import ignition  # type: ignore
ignition.set_default_timeout(4)

ROOT = 'gemini://vodoraslo.xyz'

CRAWLER = {}


def fetch(url, previous_url):
    url = ignition.url(url, previous_url)

    if not url.startswith(ROOT):
        print(f'Skipping {url}')
        CRAWLER[url] = True
        return

    print(f'Downloading {url}')
    CRAWLER[url] = True
    res, body = get(url)

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


fetch('/', ROOT)
