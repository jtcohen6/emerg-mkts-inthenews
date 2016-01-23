import json
import urllib
import pandas


"""
Scrape data from 
http://seekingalpha.com/insight/etf-hub/asset_class_performance/  #scrape for countries, commodities, emerging markets, globals and regionals

Kimono Labs has nice API for extraction of symbols from sites with strict robots.txt (403 error)

AND then create database using pandas for etf codes and associated titles

"""
def clean_data():
	# em_market_etfs = json.load(urllib.urlopen("https://www.kimonolabs.com/api/cut3sada?apikey=sE0SgLwuvZqtrtIvXuEgHbxoEDGY2W92"))
	# em_market_etfs = em_market_etfs['results']['collections']

	# commodity_etfs = json.load(urllib.urlopen("https://www.kimonolabs.com/api/3slr23ho?apikey=sE0SgLwuvZqtrtIvXuEgHbxoEDGY2W92"))
	# commodity_etfs = commodity_etfs['results']['collections']

	global_etfs = json.load(urllib.urlopen("https://www.kimonolabs.com/api/252s3rwq?apikey=sE0SgLwuvZqtrtIvXuEgHbxoEDGY2W92"))
	global_etfs = global_etfs['results']['collection1']

	for entry in global_etfs:
		print entry['world_etfs']

	countries_etfs = json.load(urllib.urlopen("https://www.kimonolabs.com/api/d0xnsorc?apikey=sE0SgLwuvZqtrtIvXuEgHbxoEDGY2W92"))
	countries_etfs = countries_etfs['results']['collection1']

	print(" ")

	for country in countries_etfs:
		print country['country_codes']
	

# 1: world_etfs
# 2: emerging_etfs
# 3: regions_etfs


# Clean data should create csvs
clean_data()