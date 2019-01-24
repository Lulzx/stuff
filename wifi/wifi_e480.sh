sudo apt update
sudo apt install build-essential git dkms
git clone --depth=1 https://github.com/tomaspinho/rtl8821ce.git rtl8821ce
cd rtl8821ce
sudo bash ./dkms-install.sh
sudo modprobe 8821ce
