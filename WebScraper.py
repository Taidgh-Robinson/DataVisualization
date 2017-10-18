# -*- coding: utf8 -*-
# Pokemon Webscraper
# Author: Taidgh Ronbinson


from lxml import html # Used to xpath over an HTML element
import requests # Used to download the web page
import re # Currently used to search over a string. 
import CSVReader

mainURL = 'https://pokemondb.net/pokedex/' #The base URL 


#Need to get all the pokemon names so we can add them to the base URL to get the pokemon's page. 
def getPokemonNames():
	page = requests.get('https://pokemondb.net/pokedex/national') # A page with all the names
	tree = html.fromstring(page.content) 
	
	return tree.xpath('//a[@class="ent-name"]/text()') # All the names, needed for the page URLS

#Some of the funky pokemon names don't translate to URL form so they have to be "cleaned" to work properly
def nameCleaner(name):
	nameDict = {"Nidoran♂" : "nidoran-m", "Nidoran♀" : "nidoran-f", "Farfetch'd" : "farfetchd", "Type: Null" : "type-null",
	"Mr. Mime" : "mr-mime", "Mime Jr." : "mime-jr", "Flabébé" : "flabebe"} #All the names that a regex sub would be unnessacary to use

	return nameDict.get(name, re.sub(' ', '-', name)) #Return the name if in the dict, else return the name with spaces subbed by -

#Get the base EXP
def getPokemonBaseEXP(pokeName, pkdex):
	page = requests.get(mainURL + pokeName) #Get the page for the pokemon
	tree = html.fromstring(page.content) #Convert to a tree that can be xpathd
	expArr = tree.xpath('//*[@id="svtabs_basic_' + str(pkdex) + '"]/div[1]/div[3]/div/div[1]/table/tbody/tr[4]/td/text()')  
	#The xpath, the reason pkdex is used is cause the xpath changes based on its pokedex number
	return int(expArr[0]) #Return the EXP as an int; 

def getPokemonType(pokeName, pkdex):
	page = requests.get(mainURL + pokeName) #Get the page for the pokemon
	tree = html.fromstring(page.content) #Convert to a tree that can be xpathd
	typArr = tree.xpath('//*[@id="svtabs_basic_' + str(pkdex) + '"]/div[1]/div[2]/table/tbody/tr[2]/td/a/text()')  
	#The xpath, the reason pkdex is used is cause the xpath changes based on its pokedex number
	return typArr


def toCSV():
	lines = [] 
	names = getPokemonNames(); 
	
	lines.append(['Pokemon Name']+['Type(s)']+['Base EXP'])
	i = 1; 
	for mon in names:
		print(i)
		t = getPokemonType(nameCleaner(mon), i)
		exp = getPokemonBaseEXP(nameCleaner(mon), i)
		i += 1;
		lines.append([nameCleaner(mon)]+[t]+[str(exp)])

	return lines


