# coding: utf-8

import json 
import csv 
import requests 

fichier = "banq.csv"

entete = {
	"User-Agent":"Camille Payant",
	"From":"camille.payant@hotmail.com"
}

for id in range(1000,2000):
	url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/{0}".format(id)

	req = requests.get(url,headers=entete)

	item = req.json()

	if item["type"] == "audio":
		liste = []
		liste.append(item["titre"].split(" /")[0])
		liste.append(item["createurs"][0])
		liste.append(item["dateCreation"])
		liste.append(item["descriptionMat"])
		liste.append(item["noticeComplete"][0]["liens"][0]["url"])

		print(item["titre"].split(" /")[0])
		print(item["createurs"][0])
		print(item["dateCreation"])
		print(item["descriptionMat"])
		print(item["noticeComplete"][0]["liens"][0]["url"])
		print("$"*80)

		f2 = open(fichier,"a")
		pouet = csv.writer(f2)
		pouet.writerow(liste)