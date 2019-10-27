'''
NIM     : 13518075         
NAMA    : Daniel Riyanto   
Tanggal : 27 Oktober 2019   
Topik   : Research "Omniwheel 3 Roda" 
Membuat kode untuk "Omniwheel 3 Roda" 
'''

import math

# KAMUS 
'''
[Omni 3 Roda]
Keterangan :
V0 = Kecepatan roda pertama
V1 = Kecepatan roda kedua
V2 = Kecepatan roda ketiga   
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

  V0 = (-1) * Vt * math.sin(math.pi / 3) + Vn * math.cos(math.pi / 3) + W * d
  V1 = (-1) * Vn + W * d
  V2 = Vt * math.sin(math.pi / 3) + Vn * math.cos(math.pi / 3) + W * d
  print("V0 = ", V0)
  print("V1 = ", V1)
  print("V2 = ", V2)

