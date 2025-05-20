import requests
import json

COOKIE="sc770430e=91k3f0v329lri5b0fmra5pq294; __utma=157766207.1995272977.1646882521.1646882521.1646882521.1; __utmc=157766207; __utmz=157766207.1646882521.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); think_var=en; __utmt=1; arp_scroll_position=174; __utmb=157766207.62.10.1646882521"

def submit():
  url = "https://www.ter-teradata.com/index/rot_order/submit_order.html"
  params = {
    'reCAPTCHA': '',
    'v': '3',
    'level': '0',
    'm': '1646885799946'
  }
  headers = {}
  headers["Cookie"] = COOKIE
  headers["Content-Type"] = "application/json"
  
  return requests.post(url, headers=headers, params=params)

def doOrder(oid):
  url = "https://www.ter-teradata.com/index/order/do_order"
  data = {
    'oid': oid
  }
  headers = {}
  headers["Cookie"] = COOKIE
  headers["Content-Type"] = "multipart/form-data"
  
  return requests.post(url, headers=headers, data=data)

for i in range(100):
  sub_resp = submit()
  if sub_resp.status_code != 200:
    print(f"error when submtting: {sub_resp.status_code} {sub_resp.text}")
    break

  data = json.loads(sub_resp.text)
  oid = data['oid']
  print(f"obtain oid: {oid}")

  do_resp = doOrder(oid)
  if do_resp.status_code != 200:
    print(f"error when doing order: {do_resp.status_code} {do_resp.text}")
    break
  data = json.loads(sub_resp.text)
  print(f"done: {data['info']}")
  