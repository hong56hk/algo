import requests
import time
import json

ACCOUNTS = [
  {
    "acc": "stevechan1996@gmail.com",
    "pwd": "Onfvnd11!",
    "gain": 0
  }, {
    "acc": "moomin456@gmail.com",
    "pwd": "a123123.",
    "gain": 0
  }
]

GAME_ID_SPIN = 1

def login(email, pwd):
  url = "https://api.freejackpot.com/auth"
  headers = {}
  headers["Content-Type"] = "application/json"
  data = {
    "query": "mutation($email: String!, $password: String!, $rememberMe: Boolean) {\n  userToken(email: $email, password: $password, rememberMe: $rememberMe){\n    userId\n    token\n    error\n  }\n}",
    "variables": {
      "email": email,
      "password": pwd,
      "rememeberMe":False
    }
  }
  return requests.post(url, headers=headers, json=data)

def queryAccount(jwt):
  url = "https://api.freejackpot.com/graphql"
  headers = {}
  headers["Authorization"] = "Bearer " + jwt
  headers["Content-Type"] = "application/json"
  data = {
    "query":"query {\n  info {\n    userId\n    firstname\n    lastname\n    dob\n    gender\n    email\n    phoneNumber\n    standardAccount\n    facebookAccount\n    paypalAccount\n    profilePicture\n    fb_age_range {\n      min\n      max\n    }\n    error\n  }\n  emailNotifications {\n    bestOffers\n    reminders\n    promotions\n  }\n  favourites {\n    favourites {\n      favouriteId\n      merchantId\n      merchantName\n    }\n  }\n  wallet {\n    balance\n    tickets\n    tickets_pending\n    daily_tickets\n    lastLotteryWinnings {\n      currency\n      cash\n      prize\n      tickets\n    }\n    spin_count\n    draw_count\n    scratch_count\n   video_count\n    game_count\n    error\n  }\n  unreadNotifications {\n    notifications {\n      notificationId\n      message\n      title\n      type\n      read\n      created\n      userId\n    }\n    amount\n    error\n  }\n}\n",
    "variables":{}
  }
  return requests.post(url, headers=headers, json=data)

def getBalance(jwt):
  acc_resp = queryAccount(jwt)
  data = json.loads(acc_resp.text)
  wallet = data['data']['wallet'] 

  return wallet['balance']
   

#===========================================================================
# work on 2022-07-08
def allocateScratchReward(jwt:str):
  url = "https://api.freejackpot.com/graphql"
  headers = {}
  headers["Authorization"] = "Bearer " + jwt
  headers["Content-Type"] = "application/json"
  data = {
    "query":"mutation {\n allocateScratchReward {\n id\n type \n amount\n }\n}",
    "variables":{}
  }
  return requests.post(url, headers=headers, json=data)

def addScratchMoney(jwt:str, amt:float):
  url = "https://api.freejackpot.com/graphql"
  headers = {}
  headers["Authorization"] = "Bearer " + jwt
  headers["Content-Type"] = "application/json"
  data = {
    "query":"mutation($game_id: Int!, $amount: Float, $matches: Int, $prize_api_key: String) {\n gameCashReward(game_id: $game_id, amount: $amount, matches: $matches, prize_api_key: $prize_api_key) {\n message\n error\n }\n}",
    "variables":{
      "game_id":4,
      "amount": amt,
      "type": "freejackpot balance",
      "prize_api_key": None
    }
  }
  return requests.post(url, headers=headers, json=data)

def addSpinMoney(jwt:str, amt:float):
  url = "https://api.freejackpot.com/graphql"
  headers = {}
  headers["Authorization"] = "Bearer " + jwt
  headers["Content-Type"] = "application/json"
  data = {
    "query":"mutation($game_id: Int!, $amount: Float, $matches: Int, $prize_api_key: String) {\n gameCashReward(game_id: $game_id, amount: $amount, matches: $matches, prize_api_key: $prize_api_key) {\n message\n error\n }\n}",
    "variables":{
      "game_id":1,
      "amount": amt
    }
  }
  return requests.post(url, headers=headers, json=data)

def addLottoMoney(jwt:str, matches:int):
  url = "https://api.freejackpot.com/graphql"
  headers = {}
  headers["Authorization"] = "Bearer " + jwt
  headers["Content-Type"] = "application/json"
  data = {
    "query":"mutation($game_id: Int!, $amount: Float, $matches: Int, $prize_api_key: String) {\n gameCashReward(game_id: $game_id, amount: $amount, matches: $matches, prize_api_key: $prize_api_key) {\n message\n error\n }\n}",
    "variables":{
      "game_id": 2,
      "matches": matches,
      "prize_api_key": None
    }
  }
  return requests.post(url, headers=headers, json=data)

#===========================================================================

for account in ACCOUNTS:
  acc = account['acc']
  pwd = account['pwd']
  print("Account: {}".format(acc))
  print("logging in...")
  resp = login(acc, pwd)
  if resp.status_code == 200:
    data = json.loads(resp.text)
    jwt = data['data']['userToken']['token']

    acc_resp = queryAccount(jwt)
    data = json.loads(acc_resp.text)
    wallet = data['data']['wallet']
    scratch_count = wallet['scratch_count']
    before_balance = wallet['balance']
    new_bal = before_balance
    
    print("current balance: {}".format(before_balance))

    print("=== scratch game ({}) ===".format(scratch_count))
    for i in range(scratch_count):
      alloc_resp = allocateScratchReward(jwt)
      print("  attempt {}: allocated: {}".format(i, alloc_resp.text))

      resp_json = json.loads(alloc_resp.text)
      add_resp = addScratchMoney(jwt, resp_json['data']['allocateScratchReward']['amount'])
      print("    done: {}".format(add_resp.text))

      # query account
      balance = getBalance(jwt)
      print("    new balance: {}".format(balance))
      
      # seem too fast will have problem
      time.sleep(1)

    print("=== spin game ({}) ===".format(wallet['spin_count']))
    for i in range(wallet['spin_count']):
      add_resp = addSpinMoney(jwt, 0.03)
      print("  attempt {}: {}".format(i+1, add_resp.text))
      
      balance = getBalance(jwt)
      print("    new balance: {}".format(balance))
      time.sleep(1)
    
    print("=== totto ({}) ===".format(wallet['draw_count']))
    for i in range(wallet['draw_count']):
      add_resp = addLottoMoney(jwt, 4)
      print("  attempt {}: {}".format(i+1, add_resp.text))

      
      new_bal = getBalance(jwt)
      print("    new balance: {}".format(new_bal))
      time.sleep(1)

    gain = new_bal - before_balance
    account['gain'] = gain
    print("Gained: {}".format(gain))
  else:
    print("failed for account: {}".format(acc))

  print("end for this account")


# print result
for account in ACCOUNTS:
  acc = account['acc']
  gain = account['gain']
  print("{} gained: {}".format(acc, gain))
