import hashlib


Karaktergirin = input("Karakter Giriniz:  ")
print(colored(" <<<<<<<< Md5 >>>>>>>> "))

md5 = hashlib.md5()
md5.update(Karaktergirin.encode())
print(md5.hexdigest())

print(" <<<<<<<< SHA1 >>>>>>>> ")

sha1 = hashlib.sha1()
sha1.update(Karaktergirin.encode())
print(sha1.hexdigest())

print(" <<<<<<<< SHA224 >>>>>>>> ")

sha224 = hashlib.sha224()
sha224.update(Karaktergirin.encode())
print(sha224.hexdigest())

print(" <<<<<<<< SHA256 >>>>>>>> ")

sha256 = hashlib.sha256()
sha256.update(Karaktergirin.encode())
print(sha256.hexdigest())

print(" <<<<<<<< SHA384 >>>>>>>> ")

sha384 = hashlib.sha384()
sha384.update(Karaktergirin.encode())
print(sha384.hexdigest())

print(" <<<<<<<< SHA512 >>>>>>>> ")

sha512 = hashlib.sha512()
sha512.update(Karaktergirin.encode())
print(sha512.hexdigest())










