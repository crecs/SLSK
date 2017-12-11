 #!/bin/bash

# =========================================================================
# ---[SLSK - Build Script]---
# Copyright (C) 2017 Supremist (aka supremesonicbrazil)
# This file is part of Steam Linux Swiss Knife (or SLSK for short).
# Steam Linux Swiss Knife is available under the GNU GPL v3.0 license. See the
# accompanying COPYING file for more details.
# =========================================================================

# Compiling from source code in a temporary folder
clear
echo "----------[Compiling SLSK...]----------"
sleep 1
mkdir bin
qmake -o ./bin/Makefile ./src/SteamLinuxSwissKnife.pro
cd bin
make
cd ..

# Creating desktop entry and setting it as executable
clear
echo "----------[Creating desktop entry...]----------"
sleep 1
echo '[Desktop Entry]
Version=1.0
Name=Steam Linux Swiss Knife
Comment=Backup automation for Steam games, saves and configs
Exec=/opt/SLSK/SteamLinuxSwissKnife
Icon=/opt/SLSK/img/SLSK_icon.png
Terminal=false
Type=Application
Categories=Utility;Application;' > ./Steam\ Linux\ Swiss\ Knife.desktop
chmod +x ./Steam\ Linux\ Swiss\ Knife.desktop

# Finishing
clear
echo "Done! Steam Linux Swiss Knife was successfully built in 'bin'."
echo "Now, please run INSTALL.sh as sudo."
echo "--------------------------------------------------------------------------------"