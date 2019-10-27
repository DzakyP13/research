'''
NIM     : 13518075         
NAMA    : Daniel Riyanto   
Tanggal : 27 Oktober 2019   
Topik   : Research "Omniwheel 4 Roda" 
Membuat kode untuk "Omniwheel 4 Roda" 
'''

import math

# KAMUS 
'''
[Omni 4 Roda]
Keterangan :
V0 = Kecepatan roda pertama
V1 = Kecepatan roda kedua
V2 = Kecepatan roda ketiga
V3 = Kecepatan roda keempat   
Vt = Kecepatan robot
Vn = Kecepatan robot?
W  = Kecepatan sudut robot
d  = perpindahan? yang ditempuh robot
'''

# ALGORITMA
while (1):
  Vt = float(input("Vt = "))
  Vn = float(input("Vn = "))
  W = float(input("W = "))
  d = float(input("d = "))

  V0 = Vn + W * d
  V1 = (-1) * Vt + W * d
  V2 = (-1) * Vn + W * d
  V3 = Vt + W * d

  print("V0 = ", V0)
  print("V1 = ", V1)
  print("V2 = ", V2)
  print("V3 = ", V3)