#!/bin/bash
#Yaman Efkar Tarafından Kodlandı.
if [[ -e "hasholusturma.py" ]]; then
        clear
        rm -rf hasholusturma.py
        read -p $'\e[31m[\e[32m!\e[31m]\e[37mUsername : ' user
        read -p $'\e[31m[\e[32m!\e[31m]\e[37mPassword : ' pass
        sleep 0.8
        echo -e '\e[31mLütfen Bekleyiniz.'
        clear
        read -p $'\e[31m[\e[32m!\e[31m]\e[37mTelefon Numarası :-90 ' tel
        echo -e ""
        read -p $'\e[31m[\e[32m!\e[31m]\e[37mGönderilecek Sms [Max:50] : ' for
        sleep 0.8
        echo -e '\e[31mAtak Başlıyor....'
        cd Api/ &&
        echo 'import requests
string = """
