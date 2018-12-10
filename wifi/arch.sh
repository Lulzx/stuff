sudo pacman-mirrors --fasttrack 5 && sudo pacman -Syyu
sudo pacman -S yay git dkms
git clone https://github.com/tomaspinho/rtl8821ce.git
cd rtl8821ce
yay bc rtl8821ce-dkms-git linux-header
reboot
sudo bash ./dkms-install.sh
sudo modprobe rtl8821ce
