import requests
from bs4 import BeautifulSoup



def decode_secret_message(url: str) -> None:
  """
  Fetches the content of a Google Document and prints the decoded message

  Args:
      url (str): The URL of the Google Document to fetch.
  """
  secret_msg: dict = {}
  max_x = 0
  max_y = 0

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

  except requests.exceptions.RequestException as e:
    raise ConnectionError(f"HTTP error occurred: {e}")


  soup = BeautifulSoup(response.text, 'html.parser')
  table = soup.find('table', recursive=True)

  if table is None:
    raise ReferenceError("Table not found in the document.")

  rows = table.find_all('tr')
  for row in rows[1:]:
    # Extract cell text for each row
    cell = [cell.get_text(strip=True) for cell in row.find_all(['td'])]

    x = int(cell[0])
    y = int(cell[2])
    msg = cell[1]

    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y

    if x not in secret_msg:
      secret_msg[x] = {}
    secret_msg[x][y] = msg



  # Print the secret message
  for y in range(max_y, -1, -1):
    for x in range(max_x + 1):
      msg = secret_msg.get(x, {}).get(y, " ")
      print(msg, end='')
    print()




url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
try:
  decode_secret_message(url)
except Exception as e:
  print(f"Connection error: {e}")
