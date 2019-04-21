echo "Installing create_ap package";
cd create_ap;
make install;
echo "Installation of create_ap complete.";
python3 gui/App.py;
