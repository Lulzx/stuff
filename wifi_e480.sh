sudo apt update
sudo apt install build-essential git dkms && clear
git clone https://github.com/tomaspinho/rtl8821ce.git
cd rtl8821ce
sudo bash ./dkms-install.sh && sudo modprobe 8821ce
