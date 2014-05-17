
from django.http import HttpResponse
from django.shortcuts import render
from collections import OrderedDict

import urllib2, json, datetime
from guild.misc import *
from django.utils import timezone

from roster.models import JsonData

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
	members = get_member_data()
	cl = get_class_data()
	rl = get_race_data()
	
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
	
def get_race_data():
	host = "http://eu.battle.net"
	
	try:
		races = JsonData.objects.get(description='races')
	except JsonData.DoesNotExist:
		races = None
	
	if races is None or races.date <= timezone.now() - datetime.timedelta(hours=12):
		print "Updating races in DB"	
		
		# Fetch class info from blizzard
		url = host + "/api/wow/data/character/races"
		response = urllib2.urlopen(url).read()
		
		try:
			old = JsonData.objects.get(description='races')
			old.delete()
		except JsonData.DoesNotExist:
			pass
		jsonData = JsonData(description='races', json=response)
		jsonData.save()			
	else:
		print "Using races classes from DB"
		response = races.json
	
	racedata = json.loads(response)
	races = racedata['races']
	rl = {}
	
	# Construct a dictionary to be able to lookup classes
	for r in races:
		rl[r['id']] = r['name']
	return rl
	
def get_class_data():
	host = "http://eu.battle.net"
	
	try:
		classes = JsonData.objects.get(description='classes')
	except JsonData.DoesNotExist:
		classes = None
	
	if classes is None or classes.date <= timezone.now() - datetime.timedelta(hours=12):
		print "Updating classes in DB"	
		
		# Fetch class info from blizzard
		url = host + "/api/wow/data/character/classes"
		response = urllib2.urlopen(url).read()
		
		try:
			old = JsonData.objects.get(description='classes')
			old.delete()
		except JsonData.DoesNotExist:
			pass
		jsonData = JsonData(description='classes', json=response)
		jsonData.save()			
	else:
		print "Using existing classes from DB"
		response = classes.json
	
	classdata = json.loads(response)
	classes = classdata['classes']
	cl = {}
	
	# Construct a dictionary to be able to lookup classes
	for c in classes:
		cl[c['id']] = c['name']
	return cl
	
def get_member_data():
	host = "http://eu.battle.net"
	
	# Check if we have recently updated data in DB
	try:
		members = JsonData.objects.get(description='members')
	except JsonData.DoesNotExist:
		members = None
	print members
	
	# If we dont have an entry for members, or if its too old, fetch new data from blizzard
	if members is None or members.date <= timezone.now() - datetime.timedelta(minutes=15):
		# Fetch guild members
		print "Updating members in DB"
		url = host + "/api/wow/guild/" + REALM_URL + "/" + GUILD_NAME_URL + "?fields=members"
		response = urllib2.urlopen(url).read()
		
		# Remove old entry if one exists
		try:
			old = JsonData.objects.get(description='members')
			old.delete()
		except JsonData.DoesNotExist:
			pass
		jsonData = JsonData(description='members', json=response)
		jsonData.save()
	else:
		response = members.json
		print "Using existing members from DB"
	
	guild = json.loads(response)
	return guild['members']
	# members = guild['members']