from scholarly import scholarly
import json
from datetime import datetime, timezone
import os
from pathlib import Path
import re
from urllib.parse import parse_qs, urlparse

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
if not scholar_id:
    config = (Path(__file__).resolve().parent.parent / '_config.yml').read_text()
    profile = re.search(r'^\s*googlescholar\s*:\s*["\']([^"\']+)["\']', config, re.MULTILINE)
    if profile:
        scholar_id = parse_qs(urlparse(profile.group(1)).query).get('user', [''])[0]
if not scholar_id:
    raise ValueError('Configure a Google Scholar profile or GOOGLE_SCHOLAR_ID.')

scholarly.set_timeout(30)
scholarly.set_retries(2)
author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
if not isinstance(author.get('citedby'), int) or author['citedby'] < 0:
    raise ValueError('Google Scholar did not return a valid citation count.')
author['updated'] = datetime.now(timezone.utc).isoformat()
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
