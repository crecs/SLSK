#!/bin/bash

# =========================================================================
# ---[SLSK - Install Script]---
# Copyright (C) 2017 Supremist (aka supremesonicbrazil)
# This file is part of Steam Linux Swiss Knife (or SLSK for short).
# Steam Linux Swiss Knife is available under the GNU GPL v3.0 license. See the
# accompanying COPYING file for more details.
# =========================================================================

# Checking if running as sudo
if [ $UID = 0 ]
then
	# Moving and copying stuff to the right places
	clear
	echo "----------[Installing SLSK to /opt/SLSK...]----------"
	sleep 1
	rm -r /opt/SLSK
	mkdir /opt/SLSK
	mv ./bin/SteamLinuxSwissKnife /opt/SLSK/SteamLinuxSwissKnife
	mv ./bin/SteamLinuxGames.db /opt/SLSK/SteamLinuxGames.db
	cp -r ./img /opt/SLSK/img
	rm -r ./bin
			
	# Finishing
	clear
	echo "Done! Steam Linux Swiss Knife was successfully installed in '/opt/SLSK'."
	echo "If you want to uninstall it anytime, just do a 'sudo rm -r /opt/SLSK'."
	echo "Enjoy!"
	echo "--------------------------------------------------------------------------------"
else
	echo "Please run this script as sudo."
	echo "Aborting..."
	echo "--------------------------------------------------------------------------------"
	exit
fi

