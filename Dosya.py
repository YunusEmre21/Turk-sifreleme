import tkinter as tk

pencere=tk.Tk()

def dosyaYap():

    dosya = open("deneme.txt", "w")

dugme = tk.Button(text = "Dosya Oluştur", command=dosyaYap())

dugme.pack()

dugme2 = tk.Button(text = "ÇIKIŞ", command=pencere.quit)

dugme2.pack()

pencere.mainloop()
