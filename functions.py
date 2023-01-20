from datetime import datetime
from typing import Tuple
import re

import ignition  # type: ignore
from cryptography.hazmat.primitives import hashes

# =>[<whitespace>]<URL>[<whitespace><USER-FRIENDLY LINK NAME>]
REGEX_LINK_LINE = r'=>\s*([^\s]+)(\s+(.*))?'


class Response:
    headers: list = []
    client_status: int = 0
    server_status: int = 0

    data: str = ''

    def __init__(self, url):
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M')

        self.headers = []
        self.headers.append(f'Date: {timestamp}')
        self.headers.append(f'URL: {url}')

    def set_status(self, client: int, server: int):
        self.client_status = client
        self.server_status = server

        self.headers.append(f'Client status: {client}')
        self.headers.append(f'Server status: {server}')

    def set_raw_data(self, data: str):
        self.data = data


def parse_body(response) -> str:
    if response.is_a(ignition.ErrorResponse):
        return f'Error while archiving: {response.data()}\n'
    elif response.is_a(ignition.InputResponse):
        return f'Error while archiving: input required for this URL.\r\nServer says: {response.data()}'
    elif response.is_a(ignition.SuccessResponse):
        return response.data()
    elif response.is_a(ignition.RedirectResponse):
        return f'Redirect data: {response.data()}'
    elif response.is_a(ignition.TempFailureResponse):
        return f'Temporal failure. Server says: {response.data()}'
    elif response.is_a(ignition.PermFailureResponse):
        return f'Permanent failure. Server says: {response.data()}'
    elif response.is_a(ignition.ClientCertRequiredResponse):
        return f'Error while archiving: client certificate needed for this URL.\r\nServer says: {response.data()}'

    return f'Unknown response type or unknown status code. Server says: {response.data()}'


def get(url='/', base=None) -> Tuple[Response, str]:
    url = ignition.url(url, base)

    res = Response(url)

    try:
        response = ignition.request(url)
    except ValueError:
        return res, f'Fatal. Archive script crashed while crawling {url}'

    res.set_status(int(response.basic_status), int(response.status))
    res.set_raw_data(response.data())

    if response.is_a(ignition.ErrorResponse):
        res.headers.append('Certificate: error')
    else:
        digest = response.certificate.fingerprint(hashes.MD5()).hex()
        res.headers.append(f'Certificate: {digest}')

    body = parse_body(response)

    if type(body) == bytes:
        body = '<binary data>'

    return res, body


def extract_links(body: str) -> list[Tuple[str, str]]:
    links = []

    for line in body.splitlines():
        if len(line) < 3:
            continue

        if line[0] != '=':
            continue

        match = re.match(REGEX_LINK_LINE, line)
        if match is None:
            continue

        links.append((match.group(1), match.group(3)))

    return links
