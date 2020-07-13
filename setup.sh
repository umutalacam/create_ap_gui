#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

dep_met=1
command -v foo >/dev/null 2>&1 || {dep_met=0}


echo "Installing create_ap package";
git clone "https://github.com/oblique/create_ap.git";
cd create_ap;
make install;
python3 ../gui/App.py;
