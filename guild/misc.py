'''
Created on 24 mar 2014

@author: Andreas
'''

GUILD_NAME = 'Back Again Pew Pew'
GUILD_NAME_URL = 'Back%20Again%20Pew%20Pew'
TITLE = 'Deorum Guild'
REALM = 'Shattered Hand'
REALM_URL = 'shattered-hand'

# Ranks
RANK_0 = "Guild Master"
RANK_1 = "Officer"
RANK_2 = "Veteran"
RANK_3 = "Member"
RANK_4 = "Trial"
RANK_5 = "Alt"

''' Include the variables that should be available to all templates '''
def guild_info(request):
	return { 
		'GUILD_NAME': GUILD_NAME,
		'TITLE': TITLE, 
		'REALM': REALM,
	}