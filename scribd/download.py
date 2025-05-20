# https://www.scribd.com/document/558331735/%E6%97%A5%E6%9C%AC%E8%AF%ADGoGoGo-1

import requests
import os

output_path = "downloads"
max_page = 218
full_page = list(range(1, max_page))

def download(link):
  response = requests.get(link)
  if response.status_code == 200:

    if not os.path.exists(output_path):
      os.makedirs(output_path)

    filename = os.path.join(output_path, link.split("/")[-1])
    with open(filename, "wb") as file:
      file.write(response.content)
    print(f"[done] {filename}")
  else:
    print(f"Failed to download {link}")


downloaded_pages = []
file = (open("./scribd/pages.txt", "r"))
for line in file:
  link = line.strip()
  if len(link) == 0:
    continue

  page = link.split("/")[-1]
  page_num = int(page.split("-")[0])
  if page_num in full_page:
    full_page.remove(page_num)

  if os.path.exists(os.path.join(output_path, page)):
    continue

  if link in downloaded_pages:
    continue


  print(f"downloading {link}...", end=" ")
  download(link)
  downloaded_pages.append(link)
file.close()

print(f"lack of below page...")
for i in full_page:
  print(i, end=", ")


print("done")
