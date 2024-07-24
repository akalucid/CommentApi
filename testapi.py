import requests
import json

url = "https://api.bitbucket.org/2.0/pullrequests/{avijay}"

headers = {
  "Accept": "application/json",
  "Authorization": "Bearer {ATATT3xFfGF06hO3N-M23nlVyZFN5xVkZ_m77g1zVkKQNuFm75gN9AQAAnO-Z24jETCdgEGc2hgcGRRtY29s2zQBcIwWkGFFzfGjfnXYuyAeMICAXCo8t3ZwpfgENiqiTgm28g-v-LE5sTRPnyxEZpPkXwCO1lXRYsnKQFzIzYGpHpJE_gyFDf0=6091A36D}"
}


response = requests.request(
   "GET",
   url,
   headers=headers
)

if response.status_code == 200:
    print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))
else:
    print(response.status_code)
    print(response.text)
