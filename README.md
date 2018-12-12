# HMCpcm
Python access to HMC REST APIs to process PCM preferences and statistics


Files:
hmc_pcm.py         - Contains function used to access the REST APIs<BR>
nchart.py          - Used to create charts for certain stats<BR>
nextract_server.py - Extracts PCM stats for servers and LPARs
set_ltmprefs.py    - Set Long Term and Aggregate stats on/off 


Use:
set_ltmstats.py is used to set the stats on(true) or off(false) for all LPARs on all servers managed by an HMC. It is also possible to
specify a specific server to turn on/off the PCM statistics. See usage in the comments


nextract_server.py is used to gather the PCM stats from those server which have Long Term and Aggregate stats set to true. By defualt
csv files are created per server and per LPAR.

The stats must be collected at no more that 30 minute intervals as the HMC purges stats more that 30 minutes old.

At the end of each collection the csv files are added to the tarball file pcmstats.tar and the svc files delete.

It is recommended to use cron to execute the script every 30 minutes:
*,30 * * * * /path/to/script/nextract_server.py hostname_or_IP_of HMC HMC_user_name HMC_password
