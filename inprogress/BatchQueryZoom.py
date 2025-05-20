#-*- coding: UTF-8 -*-

'''
This script for query info of zoom meeting using zoom API

Retreive JWT from : https://marketplace.zoom.us/develop/apps/62E1LnEmT721N2vke-WEew/credentials

## sample in put file
# this is a comment line
# Topic	Datetime	Candidate	Setting	Host	Correct?	Create Host	Alternative host	Done?	meeting id	Meeting Password	Host URL	Join URL
Selection for Recruitment of Engineering Graduates (2021) (Electrical Engineering)	2021-03-25 09:30:00	E63	A	emsd-zoom06@emsd.gov.hk	NO	emsd-zoom07@emsd.gov.hk	emsd-zoom06@emsd.gov.hk	YES	96944855682	564725	https://emsd-gov-hk.zoom.us/s/96944855682?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiJmSnBabVlBalJZSzhsbGZwaW1HZFhRIiwiaXNzIjoid2ViIiwic3R5IjoxMDAsIndjZCI6ImF3MSIsImNsdCI6MCwic3RrIjoibDJmQTdITWpoR3U0ZmhQUWZWYzliNlZtSi15MkhiRU9OVEJMUTl6dlZZYy5CZ1lnTXpGSFRsaHNUMXBpVHpkNWFGbFVXVmxLT1d0c2NrWXJNVGhGVkUxVU9GTkFZV05rTVRBM09EVXpOekkwTlRZeFpUYzJaalJpWVdaak5EUTFOVEUzTm1ZMk16azJZMll3WW1Ga01XVm1OVFk1TlRVM056VmtaakU1WkdRM1ltRTFNd0FnWlZabFlqaGhNMjVtTm1wTldrRmFaamxCVlhsSGJuQm5NakI1ZGtZNFZFSUFBMkYzTVFBQUFYZ2duQWh1QUJKMUFBQUEiLCJleHAiOjE2MTU0NjE5OTksImlhdCI6MTYxNTQ1NDc5OSwiYWlkIjoiVWlDN0tVWkNSY2lWMWFOdU4xajBmZyIsImNpZCI6IiJ9.d-bv1l4VnMmHvy75by83fs_aBITjY-ma6mka1Dlc9qI	https://emsd-gov-hk.zoom.us/j/96944855682?pwd=TWlkOWQ3YmhYTXRPOWVjMTlvOFJYZz09



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

URL_MEETING = "https://api.zoom.us/v2/meetings/{}"
SEPARATER = "\t"

APPROVAL_TYPE = {
  0: "Automatically",
  1: "Manually",
  2: "No Registration Required",
}

## init logger
log_name = "{}_{}.log".format(os.path.basename(__file__)[:-3], datetime.datetime.today().strftime("%Y%m%d"))
logpath = "./log/{}".format(log_name)
logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d <%(levelname).4s> %(threadName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

fh = logging.FileHandler(filename=logpath, mode="a")
fh.setFormatter(formatter)

logger = logging.getLogger("logger")
logger.addHandler(fh)
logger.info("start")

## ask user input
input_path = input("input file path: ")
if os.path.exists(input_path) == False:
  logger.error("error: {} not found".format(input_path))
  exit(0)

## prepare result report
report_path = os.path.basename(__file__)[:-3] + ".csv"
result_report = open(report_path, "w")
result_report.write(SEPARATER.join([
    "Meeting ID",
    # "Meeting Password",
    "Topic",
    "Start datetime",
    "Duration",
    "Host",
    "Alternative hosts",
    "Host URL",
    "Join URL",
    "Enable waiting room",
    "Approval type"
  ]) + "\n")

user = USER_DICT["emsd-zoom05@emsd.gov.hk"]

input_file = open(input_path, "r")
for line in input_file:
  line = line.strip()
  if len(line) == 0 or line.startswith("#"):
    continue  
  
  line_arr = line.rstrip().split("\t")

  # if len(line_arr) < 2:
  #   logger.info("skipped: invalid line: {}".format(line))
  #   continue
  
  # topic = line_arr[0]
  # start_datetime = line_arr[1]
  # expected_host = line_arr[4]
  # old_host = line_arr[6]
  meeting_id = line_arr[0]
  # meeting_pwd = line_arr[10]
  # host_url = line_arr[11]
  # join_url = line_arr[12]

  
  # set header
  headers = {
    'Content-Type': "application/json",
    'Authorization': user['jwt']
  }

  # get the meeting room first
  url = URL_MEETING.format(meeting_id)
  response = requests.request("GET", url, headers=headers, verify=False)
  if response.status_code == 200:
    meeting_info = response.json()
    
    start_datetime = datetime.datetime.strptime(meeting_info['start_time'], "%Y-%m-%dT%H:%M:%SZ")
    hkt_starttime = start_datetime + datetime.timedelta(hours=8)
    row = [
      str(meeting_info['id']),
      # meeting_info['password'],
      meeting_info['topic'],
      hkt_starttime.strftime("%Y-%m-%d %H:%M"),
      str(meeting_info['duration']),
      meeting_info['host_email'],
      meeting_info['settings']['alternative_hosts'],
      meeting_info['start_url'],
      meeting_info['join_url'],
      "Enabled" if meeting_info['settings']['waiting_room'] else "Disabled",
      APPROVAL_TYPE[meeting_info['settings']['approval_type']],
    ]

    
    # response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)
    # if response.status_code == 204:
    #   logger.info("meeting {} result: {}".format(meeting_id, response.status_code))
    #   logger.info("add alternative hosts. meeting id: {}, original host: {}".format(meeting_id, old_host))
    # else:
    #   logger.info("meeting {} result: {} [Failed]".format(meeting_id, response.status_code))
    #   logger.info("add alternative hosts. meeting id: {}, original host: {} [Failed]".format(meeting_id, old_host))
  
  else:
    row = [
      meeting_id,
      "",
      "",
      # "",
      # "",
      # "",
      # "",
      # "",
      "",
      "",
      "",
    ]
  logger.info(SEPARATER.join(row))
  result_report.write(SEPARATER.join(row) + "\n")
  
 
input_file.close()
result_report.close()

logger.info("report at: {}".format(report_path))
logger.info("log at: {}".format(logpath))
logger.info("done")
