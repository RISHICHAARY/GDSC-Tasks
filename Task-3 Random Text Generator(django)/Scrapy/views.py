from django.shortcuts import render
import requests
import re
from bs4 import BeautifulSoup
import json
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
def Home(request):
	url = "https://jsonplaceholder.typicode.com/posts"
	response = requests.get(url)
	data_json =response.json()
	for i in range(100):
		data_json[i]["body"]=data_json[i]["body"].replace('\n',' ')
	df = pd.DataFrame(data_json)
	fl=["{% block content %}","{%  endblock %}",'<link href="https://fonts.googleapis.com/css2?family=Caveat&family=Inter:wght@300&family=Lobster&family=Montserrat:wght@100;200&family=Open+Sans:wght@300&family=Poppins:wght@800&display=swap" rel="stylesheet">',"<title>Scrapy</title>","<style>body{ font-family: 'Montserrat', sans-serif;background: #8e9eab;background: -webkit-linear-gradient(to right, #eef2f3, #8e9eab);background: linear-gradient(to right, #eef2f3, #8e9eab);}th{ text-decoration:underline 0.1em solid;text-underline-position:under;}th,td{text-transform: capitalize;}table,th,td{ border:0px solid;border-collapse:collapse;text-align:center;padding:1em;}</style>","<h1 style='text-align:center;text-decoration:underline 0.1em solid;text-underline-position:under;'>Scrappy</h1>",str(df.to_html())]
	fl1=''.join(fl)
	hfl=open('Scrapy/templates/cnt.html','w')
	hfl.write(fl1)
	hfl.close()
	return render(request,'Home.html',{'json':df})
# Create your views here.
