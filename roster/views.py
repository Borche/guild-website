
from django.http import HttpResponse
from django.shortcuts import render

import urllib2, json
from guild.misc import *

# Create your views here.

def members(request):
    host = "http://eu.battle.net"
    url = host + "/api/wow/guild/" + REALM + "/" + GUILD_NAME + "?fields=members"
    
    response = urllib2.urlopen(url).read()
    
    guild = json.loads(response)
    
    members = guild['members']   
    
    return render(request, 'roster/roster.html', {'members': members})