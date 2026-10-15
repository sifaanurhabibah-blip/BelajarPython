print("Belajar Phyton")
print("###############")

a = 3
b = 7
c = a ** b 

print("Nilai c = ", c)
print ("=============")

d = 8
e = 9
f = (d>e)

print("Nilai F", f)
print("===========")

## Logika

g = 7
h = 10

if (g<h):
    print ("Jika Benar Cetak Ini")
else :
    print ("Jika Salah, Cetak Ini")

print("==========================")
## Perulangan

umur =[34, 24, 82, 63, 22, 19]

n_umur = len_(umur)
print("Panjang = ", n_umur)

##loop for

r_umur = range(n_umur)
print("range: ", r_umur)

for i in range (len(umur)):
    print("Data Umur ke=",i," = ", umur[i])

###
##
def LuasSegiTiga(a, t):
    return 0.5 * a * t 
    print("Luas Segi Tiga")
    print("=============")
    alas = 7
    tinggi = 4
    print ("Alas = ", alas, " , Tinggi = ", tinggi, ", Luas = ", LuasSegiTiga(alas))

def hitunganratarata(data_x):
    jumlah = 0
    for i in range(len(data_x)):
        jumlah i = data_x[i]
        return jumlah/len(data_x)

print("Nilai rata-rata umur: ", hitunganrata(umur))

rata = [umur[i] *2 for i in range(len(umur))]
print(rata)