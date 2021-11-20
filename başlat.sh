clear

echo instagram/byunussluemre
echo github.com/YunusEmre21
     
echo [1] Termux Güncelle         [2]Şifreleme




read -p "İşlem Numarası: " islem
if [[ $islem == 1 || $islem == 01 ]]; then
pkg install git -y
pkg install python python2 -y
pkg install wget -y
pkg install curl -y
pkg install ruby -y
pkg install php -y
pkg install pip pip2 -y
pkg install clang -y
pkg install vim -y
pkg install nano -y
apt install proot -y
pkg install cat -y
pkg install figlet -y
pkg install cmatrix -y
pkg install perl -y
apt update
apt upgrade -y
clear

echo kurulum bitti
sleep 2

if [[ $islem == 2 || $islem == 2 ]]; then
python hasholuşturma.py
clear

sleep 2
