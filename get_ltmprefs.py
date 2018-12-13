#!/usr/bin/python3
# Version 1
# Get and show Longterm and Aggregate PCM stats settings

import hmc_pcm as hmc
import sys
import os

if len(sys.argv) != 5:   # five including the program name entry [0]
	print("Usage: %s HMC-hostname HMC-username HMC-password  servername|ALL" %(sys.argv[0]))
	sys.exit(1)
hostname=sys.argv[1]
user    =sys.argv[2]
password=sys.argv[3]
mgServer=sys.argv[4]

print("HMC hostanme=%s User=%s Password=%s Server(s)=%s"  %( hostname, user, password, mgServer))

debug=False
debugDir = "./debug"

if not os.path.exists(debugDir):
	os.makedirs(debugDir)

print("-> Logging on to %s as user %s" % (hostname,user))
hmc = hmc.HMC(hostname, user, password)
print("-> Get server details")
serverDetails = hmc.get_server_details_pcm()
print("-> Get current preferences") # returns XML text
prefstripped = hmc.get_stripped_preferences_pcm()

## If debug is enabled save a copy of the current prefernces
if debug:
	print("-> Saving current repferences to directory: %s" %debugDir)
	hmc.save_to_file("server_perferences.xml",prefstripped)

print("-> Parse current Preferences")
serverlist = hmc.parse_prefs_pcm(prefstripped)  # returns a list of dictionaries one per Server
perflist = []
all_true = True

for num,server in enumerate(serverlist):
	## Process all managed servers for this HMC
	if mgServer == "ALL":
		print('-> Server name=%-16s agg=%-5s longterm=%-5s' %(server['name'], server['agg'], server['lterm']))
	## Process just the individual managed server specified in parameter 5    
	elif not mgServer == "ALL":
		if server['name'] == mgServer:
			print('-> Server name=%-16s agg=%-5s longterm=%-5s' %(server['name'], server['agg'], server['lterm']))
	else:
		print("-> Ignoring server=%-16s"%server['name'])

print("Logging off the HMC")
hmc.logoff()
