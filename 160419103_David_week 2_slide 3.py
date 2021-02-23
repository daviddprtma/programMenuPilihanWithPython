#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math;

def menuPilihan():
    print("Selamat datang, program menghitung luas");
    print("========================================");
    print("Menu Pilihan: ");
    print("1.Persegi Panjang");
    print("2.Lingkaran");
    print("3.Keluar");
    print("========================================");

def persegiPanjang():
    print("===== Menghitung Luas Persegi Panjang");
    a = int(input("Masukkan panjang: "));
    b = int(input("Masukkan lebar: "));
    luasPersegiPanjang = a * b;
    print("luas persegi panjang = ", luasPersegiPanjang);

def lingkaran():
    print("===== Menghitung Luas Lingkaran");
    a = int(input("Masukkan jari-jari: "));
    luasLingkaran = math.pi * math.pow(a,2);
    print("luas lingkaran = ", luasLingkaran);
    
while True:
    menuPilihan();
    pilihan = input("Masukkan pilihan: ");
    
    if pilihan == "1":
        persegiPanjang();
    elif pilihan == "2":
        lingkaran();
    elif pilihan == "3":
        break
    else:
        print("Ups tidak ada pilihan lagi.");


# In[ ]:




