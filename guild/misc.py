'''
Created on 24 mar 2014

@author: Andreas
'''

GUILD_NAME = 'Deorum'
TITLE = 'Deorum Guild'

''' Include the variables that should be available to all templates '''
def guild_info(request):
    return { 
            'GUILD_NAME': GUILD_NAME,
            'TITLE': TITLE, 
            }