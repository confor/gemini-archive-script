from pprint import pprint
import re
from functions import get, extract_links

import ignition  # type: ignore
ignition.set_default_timeout(10)

headers, response = get('/', 'gemini://gemini.elbinario.net')
pprint(headers)

pprint(extract_links(response))
