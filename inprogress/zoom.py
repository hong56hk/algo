#-*- coding: UTF-8 -*-

'''
This script for batch creating Zoom meeting room

Retreive JWT from : https://marketplace.zoom.us/develop/apps/62E1LnEmT721N2vke-WEew/credentials
https://marketplace.zoom.us/develop/create

## sample in put file
# this is a comment line
#topic	datetime	candidate 
Selection for Recruitment of Engineering Graduates (2021) (Building Services)	2021-03-31 09:30	BS4	emsd-zoom10@emsd.gov.hk
Selection for Recruitment of Engineering Graduates (2021) (Building Services)	2021-03-31 09:45	BS8	emsd-zoom10@emsd.gov.hk


##  version
20210317
 - init commit

'''

import datetime
import requests
import logging
import random
import string
import json
import sys
import os

PROXY = {
  "http": "http://proxy.emsd.hksarg:80/",
  "https": "http://proxy.emsd.hksarg:80/",
}

PROXY_ACC = ('T06994DTD', "Abcd1234^")

USER_DICT = {
  "emsd-zoom05@emsd.gov.hk": {
    "user_id": "Q1RGh4NWSiSE2S-roYLa1Q",
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDY5MTg0NDAsImlhdCI6MTY0NjMxMzY0MH0.oaDzyUxXW7LiDvm6c2shSditce_zFWTqi54J0QxvSy8",
  },
  "emsd-zoom06@emsd.gov.hk": {
    "user_id": "1auruIu2Tm6ZSAHcKmDnCA",
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDcwMTIzOTksImlhdCI6MTY0NjQwNzU5OX0.lQrxs3tbQO4D1NPa8dy_yATjE_qcSL5ZquqvVmnioLI",
  }, 
  "emsd-zoom07@emsd.gov.hk": {
    "user_id": "fJpZmYAjRYK8llfpimGdXQ",
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDcwMTI0NTIsImlhdCI6MTY0NjQwNzY1Mn0.T23FR-oGDkRVU7g4yXhZoYnwNe_SHNyHJ1CRpmUCT_A",
  }, 
  "emsd-zoom08@emsd.gov.hk": {
    "user_id": "nRgNKFZvQ6K0S-p1cQULEw",
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDcwMTI0OTQsImlhdCI6MTY0NjQwNzY5NX0.bIK86IKKQt0MH8Ri7sPmhdzV0YjMDCWgqh80kc__Ca8",
  }, 
  "emsd-zoom09@emsd.gov.hk": {
    "user_id": "-ClySnDUQn2Gb5MkBZlV7A",
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDcwMTI1MjgsImlhdCI6MTY0NjQwNzcyOH0.3BGftdAFfo91QRoTXnBCkPgMfWags2XstqX6ONwl_CM",
  }, 
  "emsd-zoom10@emsd.gov.hk": {
    "user_id": "ZpS5T3V1REa6CqWYCaJh3g",
    "jwt" : "Bearer ",
  }
}

URL_CREATE_MEETING = "https://api.zoom.us/v2/users/{}/meetings"
MEETING_SETTING = {
  "host_video": True,
  "participant_video": True,
  "cn_meeting": False,
  "in_meeting": False,
  "join_before_host": False,
  "mute_upon_entry": False,
  "watermark": False,
  "use_pmi": False,
  "jbh_time": 0,
  "approval_type": 2,
  "waiting_room": True,
  "audio": "both",
  "auto_recording": "none",
  "alternative_hosts": None,
  "global_dial_in_countries": [],
  "registrants_email_notification": False,
  "approval_type": 2,
}

SEPARATER = "\t"

## init logger
log_name = "{}_{}.log".format(os.path.basename(__file__)[:-3], datetime.datetime.today().strftime("%Y%m%d"))
logpath = "./log/{}".format(log_name)
logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d <%(levelname).4s> %(threadName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

fh = logging.FileHandler(filename=logpath, mode="a")
fh.setFormatter(formatter)

logger = logging.getLogger("logger")
logger.addHandler(fh)

## ask user input
logger.info("start")

input_path = input("input file path: ")
if os.path.exists(input_path) == False:
  logger.error("error: {} not found".format(input_path))
  exit(0)

## result
report_path = os.path.basename(__file__)[:-3] + ".csv"
result_report = open(report_path, "w")
result_report.write(SEPARATER.join([
    "Topic",
    "Candidate",
    "Datetime",
    "Host",
    "Meeting ID",
    "Meeting Password",
    "Host URL",
    "Join URL"
  ]) + "\n")

input_file = open(input_path, "r")
for line in input_file:
  line = line.strip()
  if len(line) == 0 or line.startswith("#"):
    continue  
  
  line_arr = line.rstrip().split("\t")

  if len(line_arr) < 4:
    logger.info("skipped: invalid line: {}".format(line))
    continue
  topic = line_arr[0]
  start_time = line_arr[1]
  host_email = line_arr[2]
  candidate = line_arr[3]

  start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")

  user = USER_DICT[host_email]
  if len(user['jwt']) == 0:
    logger.error("invalid jwt for user: {}".format(host_email))
    continue

  password = ''.join(random.choices(string.digits, k = 6))
  payload = {
    "topic": f"{topic} {start_time} [{candidate}]",
    "type": 2,
    "start_time": start_datetime.strftime("%Y-%m-%dT%H:%M:00+0800"),
    "duration": 15,
    "timezone": "Asia/Hong_Kong",
    "password": password,
    "agenda": "",
    "settings": MEETING_SETTING
  }
  headers = {
    'content-type': "application/json",
    'Authorization': user['jwt']
  }
  url = URL_CREATE_MEETING.format(user['user_id'])
  # response = requests.request("POST", URL_CREATE_MEETING, json=payload, headers=headers, verify=False, proxies=PROXY, auth=PROXY_ACC)
  response = requests.request("POST", url, json=payload, headers=headers, verify=False)
  row = []
  if response.status_code == 201:
    resp_json = json.loads(response.text)
    row = [
      resp_json['topic'],
      start_datetime.strftime("%Y-%m-%d %H:%M:00"),
      candidate,
      resp_json['host_email'],
      str(resp_json['id']),
      password,
      resp_json['start_url'],
      resp_json['join_url'],
    ]
  else:
    logger.error(f"error: {host_email} {response.text}")
    row = [
      topic,
      start_datetime.strftime("%Y-%m-%d %H:%M:00"),
      candidate,
      host_email,
      '',
      '',
      '',
      '',
    ]
  logger.info(SEPARATER.join(row))
  result_report.write(SEPARATER.join(row) + "\n")
  
  
  

input_file.close()
result_report.close()


logger.info("report at: {}".format(report_path))
logger.info("log at: {}".format(logpath))
logger.info("done")
