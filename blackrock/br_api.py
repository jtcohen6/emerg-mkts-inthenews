import requests
import json
from pprint import pprint
from datetime import datetime
import csv
import sys

ticker = []

# country ETFs
f = open("tickers\\country_etfs_clean.csv", 'r')
for line in f:
    ticker.append(line.rstrip('\n').split(",")[2])

# emerging mkt ETFs
f = open("tickers\\commodity_etfs_clean.csv", 'r')
for line in f:
    ticker.append(line.rstrip('\n').split(",")[2])

# global/regional ETFs
f = open("tickers\\global_regional_etfs_clean.csv", 'r')
for line in f:
    ticker.append(line.rstrip('\n').split(",")[2])

# commodity ETFs
f = open("tickers\\commodity_etfs_clean.csv", 'r')
for line in f:
    ticker.append(line.rstrip('\n').split(",")[2])

# instantiate asset
asset = []

# run massive loop
for t in ticker:

    # set up BlackRock API
    payload = {
    'outputFormat': "json",
    'identifiers': t,
    'includePositionReturns': True,
    'returnsType': "DAILY",
    'startDate': 20060101,
    'endDate': 20160101,
    'useCache': False }

    # run BlackRock API
    portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/performance", params=payload)

    # open as json
    data = portfolioAnalysisRequest.json()
    level = []
    asOfDate = []
    drawdown = []
    level.append(data["resultMap"]["RETURNS"][0]["latestPerf"]["level"])
    level.append(data["resultMap"]["RETURNS"][0]["latestPerf"]["asOfDate"])
    level.append(data["resultMap"]["RETURNS"][0]["latestPerf"]["drawdown"])
    level.append(data["resultMap"]["RETURNS"][0]["monthEndPerf"]["level"])
    level.append(data["resultMap"]["RETURNS"][0]["monthEndPerf"]["asOfDate"])
    level.append(data["resultMap"]["RETURNS"][0]["monthEndPerf"]["drawdown"])
    for thing in data["resultMap"]["RETURNS"][0]["returnsMap"]:
        level.append(data["resultMap"]["RETURNS"][0]["returnsMap"][thing]["level"])
        badform = data["resultMap"]["RETURNS"][0]["returnsMap"][thing]["asOfDate"]
        asOfDate.append(datetime.strptime(str(badform),'%Y%m%d').strftime("%Y-%m-%d"))
        drawdown.append(data["resultMap"]["RETURNS"][0]["returnsMap"][thing]["drawdown"])

    with open ('performance\\' + t + '.csv', 'w') as csvFile:
        temp = []
        writer = csv.writer(csvFile)
        writer.writerow(['level','asOfDate','drawdown'])
        for l, a, d in zip(level, asOfDate, drawdown):
            temp.append((l, a, d))
            writer.writerow(temp.append)

    assets.append((t, level, asOfDate, drawdown))
