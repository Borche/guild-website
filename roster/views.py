
from django.http import HttpResponse
from django.shortcuts import render
from collections import OrderedDict

import urllib2, json
from guild.misc import *

# Create your views here.

class Member(object):
	
	def __init__(self):
		self.name = ""
		self.rank = ""
		self.level = ""
		self.xclass = ""
		self.race = ""
		
def extract_rank(rank):
	if rank == 0: 
		return RANK_0
	elif rank == 1:
		return RANK_1
	elif rank == 2:
		return RANK_2
	elif rank == 3:
		return RANK_3
	elif rank == 4:
		return RANK_4
	elif rank == 5:
		return RANK_5
	return "Secret Rank"
	
def extract_class(xclass):
	if xclass == 1:
		return "Death Knight"
	elif xclass == 2:
		return "Druid"
	elif xclass == 3:
		return "Hunter"
	elif xclass == 4:
		return "Mage"
	elif xclass == 5:
		return "Monk"
	elif xclass == 6:
		return "Paladin"
	elif xclass == 7:
		return "Priest"
	elif xclass == 8:
		return "Rogue"
	elif xclass == 9:
		return "Shaman"
	elif xclass == 10:
		return "Warlock"
	elif xclass == 11:
		return "Warrior"
	return "Secret Class"

def roster(request, attr, ord):
	print ord
		
	host = "http://eu.battle.net"
	
	# Fetch guild members
	url = host + "/api/wow/guild/" + REALM_URL + "/" + GUILD_NAME_URL + "?fields=members"
	
	#print url
	response = urllib2.urlopen(url).read()
	
	guild = json.loads(response)
	
	members = guild['members']   
	
	# Fetch class info
	url = host + "/api/wow/data/character/classes"
	response = urllib2.urlopen(url).read()
	classdata = json.loads(response)
	classes = classdata['classes']
	cl = {}
	
	# Construct a dictionary to be able to lookup classes
	for c in classes:
		cl[c['id']] = c['name']
		
	# Fetch race data
	url = host + "/api/wow/data/character/races"
	response = urllib2.urlopen(url).read()
	racedata = json.loads(response)
	races = racedata['races']
	rl = {}
	
	for r in races:
		rl[r['id']] = r['name']
		
	# Fetch rank data
	
	list = []
	
	for m in members:
		char = m['character']
		mem = Member()
		mem.name = char['name']
		mem.xclass = cl[char['class']]
		mem.race = rl[char['race']]
		mem.level = char['level']
		mem.rank = extract_rank(m['rank'])
		list.append(mem)
	
	if ord == 'asc':
		ord = 'desc'
		list.sort(key=lambda x: getattr(x, attr), reverse=False)
	else:
		ord = 'asc'
		list.sort(key=lambda x: getattr(x, attr), reverse=True)
    
	return render(request, 'roster/roster.html', {'members': list, 'ord': ord })