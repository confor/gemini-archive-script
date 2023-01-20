from datetime import datetime
from typing import Tuple
import re

import ignition  # type: ignore
from cryptography.hazmat.primitives import hashes

# =>[<whitespace>]<URL>[<whitespace><USER-FRIENDLY LINK NAME>]
REGEX_LINK_LINE = r'=>\s*([^\s]+)(\s+(.*))?'


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


def get(url='/', base=None) -> Tuple[list[str], str]:
    url = ignition.url(url, base)
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M')

    headers = []
    headers.append(f'Date: {timestamp}')
    headers.append(f'URL: {url}')

    try:
        response = ignition.request(url)
    except ValueError:
        return headers, f'Fatal. Archive script crashed while crawling {url}'

    headers.append(f'Client status: {response.basic_status}')
    headers.append(f'Server status: {response.status}')

    if response.is_a(ignition.ErrorResponse):
        headers.append('Certificate: error')
    else:
        digest = response.certificate.fingerprint(hashes.MD5()).hex()
        headers.append(f'Certificate: {digest}')

    body = parse_body(response)

    if type(body) == bytes:
        body = '<binary data>'

    return headers, body


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
