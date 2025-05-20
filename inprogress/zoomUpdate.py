#-*- coding: UTF-8 -*-

'''
This script for batch adding alternative host for Zoom meeting

Retreive JWT from : https://marketplace.zoom.us/develop/apps/62E1LnEmT721N2vke-WEew/credentials

## sample in put file
# this is a comment line
# <MeetingID>	<title> <Host>	<setting>
94860625964	emsd-zoom09@emsd.gov.hk	emsd-zoom10@emsd.gov.hk


##  version
20210309
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
    "jwt" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImIxbm54dVNNVHRpbGF5NC1VUEZrRVEiLCJleHAiOjE2NDcxNDEzNDcsImlhdCI6MTY0NjUzNjU0N30.Sp5-cT3W_xqfaEtCUz-BZNDEcZRM-hPt_teiZtDGeh4",
  }
}

URL_UPDATE_MEETING = "https://api.zoom.us/v2/meetings/{}"
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


input_file = open(input_path, "r")
for line in input_file:
  line = line.strip()
  if len(line) == 0 or line.startswith("#"):
    continue  
  
  line_arr = line.rstrip().split("\t")

  if len(line_arr) < 2:
    logger.info("skipped: invalid line: {}".format(line))
    continue
  meeting_id = line_arr[0]
  old_host = line_arr[1]
  # new_host = line_arr[2]
  
  # start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")

  user = USER_DICT[old_host]

  payload = {
    "settings": {
      "approval_type": 2,
      "waiting_room": True,
      # "alternative_hosts": new_host,
    },
    # "start_time": start_datetime.strftime("%Y-%m-%dT%H:%M:00+0800"),
    # "topic": f"{topic} {start_time} [{setting}]"
  }
  headers = {
    'content-type': "application/json",
    'authorization': user['jwt']
  }
  url = URL_UPDATE_MEETING.format(meeting_id)
  response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)
  if response.status_code == 204:
    logger.info("meeting {} result: {}".format(meeting_id, response.status_code))
  #   logger.info("add alternative hosts. meeting id: {}, original host: {}, alternative host: {}".format(meeting_id, old_host, new_host))
  else:
    logger.info("meeting {} result: {} [Failed]".format(meeting_id, response.status_code))
  #   logger.info("add alternative hosts. meeting id: {}, original host: {}, alternative host: {} [Failed]".format(meeting_id, old_host, new_host))
  
input_file.close()

logger.info("log at: {}".format(logpath))
logger.info("done")
