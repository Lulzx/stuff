sudo pacman-mirrors --fasttrack 5 && sudo pacman -Syu
sudo pacman -S yay git dkms
git clone --depth=1 https://github.com/tomaspinho/rtl8821ce.git
cd rtl8821ce
yay linux-headers
sudo bash ./dkms-install.sh
reboot
sudo modprobe 8821ce
