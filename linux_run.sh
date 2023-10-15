sudo dpkg --configure -a
sudo apt-get install android-tools-adb

python3 -m venv ./scrd
chmod -R 777 scrd
source scrd/bin/activate

sudo apt-get install -r requirementsLinux.txt
python3 main.py

deactivate
