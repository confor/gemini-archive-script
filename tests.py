from pprint import pprint
from urllib.parse import quote_plus as urlencode
from functions import get

import ignition  # type: ignore
ignition.set_default_timeout(10)

tests = {
    # '1.1: domain wont resolve': 'gemini://invalid.invalid/',
    # '1.1: port not open': 'gemini://pitr.ca/',
    # '1.1: server takes too long to reply': 'gemini://egsam.glv.one/1.1.write.timeout',
    # '1.1: server doesnt close connection': 'gemini://egsam.glv.one/1.1.no.close',
    # '3: malformed data': 'gemini://egsam.glv.one/3.no.cr',
    '3.1: non-numeric status code': 'gemini://egsam.glv.one/3.1.bad.status',
    '3.1: no spaces after status code': 'gemini://egsam.glv.one/3.1.no.space',
    '3.1: meta too long': 'gemini://egsam.glv.one/3.1.long.meta',
    '3.2: 1-digit status': 'gemini://egsam.glv.one/3.2.one.digit',
    '3.2: 3-digit status': 'gemini://egsam.glv.one/3.2.three.digits',
    '3.2: status 19': 'gemini://egsam.glv.one/3.2.status.1',
    '3.2: status 29': 'gemini://egsam.glv.one/3.2.status.2',
    '3.2: status 39': 'gemini://egsam.glv.one/3.2.status.3',
    '3.2: status 48': 'gemini://egsam.glv.one/3.2.status.4',
    '3.2: status 59': 'gemini://egsam.glv.one/3.2.status.5',
    '3.2: status 69': 'gemini://egsam.glv.one/3.2.status.6',
    '3.2: status 99': 'gemini://egsam.glv.one/3.2.status.9',
    '3.2.1: input urlencode': 'gemini://egsam.glv.one/3.2.1.percent?' + urlencode('1% + #x = -1 & ?'),
    '3.2.1: input too long': 'gemini://egsam.glv.one/3.2.1.long?' + ('x' * 1300),
    '3.2.2: text/plan': 'gemini://egsam.glv.one/3.2.2.text',
    '3.2.2: text/html': 'gemini://egsam.glv.one/3.2.2.html',
    '3.2.2: image/jpeg': 'gemini://egsam.glv.one/3.2.2.jpg',
    '3.2.2: image/jpeg but actually text/plain': 'gemini://egsam.glv.one/3.2.2.jpg.bad',
    '3.2.3: redirect': 'gemini://egsam.glv.one/3.2.3.redirect',
    '3.2.4: temp failure': 'gemini://egsam.glv.one/3.2.4.fail',
    '3.2.5: perm failure': 'gemini://egsam.glv.one/3.2.5.fail',
    '3.2.6: cert required': 'gemini://egsam.glv.one/3.2.6.check',
    '4.1: tls 1.3': 'gemini://egsam13.glv.one/',
}


for test_name, url in tests.items():
    print(f'Running test: {test_name}')
    res, body = get(url)
    pprint(res.headers)
    pprint(body)
    print('-' * 80)
