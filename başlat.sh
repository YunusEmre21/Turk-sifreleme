clear 
echo Bu dosyalar etik amaçlar doğrultusunda yapılmıştır.Bu dosyalar kullanılarak yapılan hiçbir suçtan ben sorumlu değilim.Bu dosyaları kullanarak bunları okumuş ve kabul etmiş sayılırsınız.

read -p "İşlem Numarası: " islem

if [[ $islem == 1 || $islem == 01 ]]; then
cd $Turk-sifreleme
