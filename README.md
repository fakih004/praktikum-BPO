Program ini adalah simulasi Sistem manajemen dan layanan rumah sakit berbasis OOP
sistem ini dirancang untuk mengelola data tenaga medis, pasien dan janji temu di rumah sakit

konsep oop yang diimplementasikan 
- class dan object: pembentukan cetakan objek untuk tenaga medis, pasien dan janji temu
- Encapsulasi: perlindungan data seperti catatan medis pasien (__catatanMedis) dan status janji temu (__status)
- Getter dan Setter: penggunaan decorator @property untuk memvalidasi dan mengakses perubahan data catatan agar perubahan tidak boleh kosong
- Class method: untuk mengubah jam operasional
- static method: untuk memvalidasi status janji temu pasien 


1. Class TenagaMedis
Digunakan untuk merepresentasikan data tenaga medis yang bertugas di rumah sakit.
Atribut:
 - nama: nama tenaga medis
 - peran: peran di rumah sakit(contoh: dokter,perawat)
 - spesialis: bidang setiap tenaga medis(contoh: spesialis jantung, UGD)

2. Class Pasien
Digunakan untuk mengelola data pasien seperti nama,umur dan catatanMedis
Atribut
 - nama : Nama pasien
 - umur : umur pasien
 - __catatanMedis : catatan medis pasien, atribut privilage sehingga tidak bisa di akses secara langsung
Method
 - catatanMedis(getter) : mengembalikan nilai catatan medis pasien
 - catatanMedis(setter) : mengubah nilai catatan medis dengan validasi perubahan tidak boleh kosong('len(catatanMedisBaru.strip()==0')

3. Class JanjiTemu 
Digunakan untuk mencatat dan mengelola jadwal janji temu pasien dengan dokter 
Atribut
 - namaInstansi : nama instansi/rumah sakit
 - totalJanjiTemu : menghitung jumlah total janji temu yang sudah dibuat
 - jamOprasional : jam buka rumah sakit ("07.00 - 00.00")
 - pasien : nama pasien
 - tenagaMedis : nama tenaga medis
 - tanggal : tanggal janji temu
 - __status : status janji temu (pending/dikonfirmasi/selesai)
Method
 - lihatStatus() : mengembalikan status janji temu saat ini
 - ubahJamOperasional(jamBaru) : mengubah jam operasional
 - validasiStatus(status) : melindungi status janji temu agar tidak diubah sembarangan

-PANDUAN PENGUJIAN
#catatan di objek class janjiTemu yang ke 2 (janji2) ubah pasien1 menjadi pasien2

 -Pengujian objek dan atribut
Di program sudah tersedia 2 objek untuk masing-masing kelas dan sudah ada kode untuk menguji apakah total janji temu akan terhitung, jika output menunjukkan "total janji temu sekarang : 2" maka program berhasil

 -Pengujian Getter dan setter
 Di program juga sudah tersedia kode untuk menguji getter dan setter:
 #getter & setter
pasien1.catatanMedis = "batuk berdahak" # valid
pasien1.catatanMedis = "" # gak valid
print("Catatan:", pasien1.catatanMedis)
Kasih tanda (#) di salah satu objek yang sudah tersedia dan jalankan programnya

 -pengujian class method dan static method


