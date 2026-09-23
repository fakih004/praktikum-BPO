Program ini adalah simulasi Sistem manajemen dan layanan rumah sakit berbasis OOP
sistem ini dirancang untuk mengelola data tenaga medis, pasien dan janji temu di rumah sakit

konsep oop yang diimplementasikan 
- class dan object: pembentukan cetakan objek untuk tenaga medis, pasien dan janji temu
- Encapsulasi: perlindungan data seperti catatan medis pasien (__catatanMedis) dan status janji temu (__status)
- Getter dan Setter: penggunaan decorator @property untuk memvalidasi dan mengakses perubahan data catatan agar perubahan tidak boleh kosong
- Class method: untuk mengubah jam operasional
- static method: untuk memvalidasi status janji temu pasien 


1. Struktur Class

- Class TenagaMedis
Digunakan untuk merepresentasikan data tenaga medis yang bertugas di rumah sakit.
Atribut :
- nama: nama tenaga medis
- peran: peran di rumah sakit(contoh: dokter,perawat)
- spesialis: bidang setiap tenaga medis(contoh: spesialis jantung, UGD)

