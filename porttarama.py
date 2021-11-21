import socket
import datetime
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hedef = input('[+] Hedef IP adresini giriniz : ')
def tarama(port):
    try:
        sock.connect((hedef,port))
        return True
    except:
        return False
# buradada for döngüsü açıyoruz ve range() fonksiyonu ile 1 ile 500 arasındaki değerleri ekrana bastırıyoruz bunlar taranan port aralıklarıdır
# siz port aralığını değiştirebilirsiniz
# for döngüsü içerisinde açılan 'portNumarasi' true olursa bize açık olan portları bastıracaktır

for portNumarasi in range(1,500):
    print("Port taranıyor" , portNumarasi)
    if tarama(portNumarasi):
        print('[*] Port',portNumarasi,'/tcp','açık')