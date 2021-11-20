import hashlib
from termcolor import colored

Karaktergirin = input("Karakter Giriniz:  ")
print(colored(" <<<<<<<< Md5 >>>>>>>> ", "blue"))

md5 = hashlib.md5()
md5.update(Karaktergirin.encode())
print(colored(md5.hexdigest(), "green"))

print(colored(" <<<<<<<< SHA1 >>>>>>>> ", "blue"))

sha1 = hashlib.sha1()
sha1.update(Karaktergirin.encode())
print(colored(sha1.hexdigest(), "green"))

print(colored(" <<<<<<<< SHA224 >>>>>>>> ", "blue"))

sha224 = hashlib.sha224()
sha224.update(Karaktergirin.encode())
print(colored(sha224.hexdigest(), "green"))

print(colored(" <<<<<<<< SHA256 >>>>>>>> ", "blue"))

sha256 = hashlib.sha256()
sha256.update(Karaktergirin.encode())
print(colored(sha256.hexdigest(), "green"))

print(colored(" <<<<<<<< SHA384 >>>>>>>> ", "blue"))

sha384 = hashlib.sha384()
sha384.update(Karaktergirin.encode())
print(colored(sha384.hexdigest(), "green"))

print(colored(" <<<<<<<< SHA512 >>>>>>>> ", "blue"))

sha512 = hashlib.sha512()
sha512.update(Karaktergirin.encode())
print(colored(sha512.hexdigest(), "green"))










