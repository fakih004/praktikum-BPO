##Program ini adalah simulasi Sistem manajemen dan layanan rumah sakit berbasis OOP sistem ini dirancang untuk mengelola data tenaga medis, pasien dan janji temu di rumah sakit##

Program ini menerapkan konsep relasi UML yang berupa
Asosiasi:

    def periksaPasien(self, pasien):
        print(f"{self._nama} sedang memeriksa {pasien.nama}, pasien dengan diagnosis {pasien.RekamMedis.diagnosis}")
Class TenagaMedis butuh data pasien hanya saat menjalankan method periksaPasien setelah selesai pasien dan TenagaMedis kembali sendiri-sendiri.

Agregasi:

    def lihatStatus(self):
        return f"Status janji temu pasien {self.pasien.nama} dengan {self.tenagaMedis._nama}: {self.__status} "
Class janjiTemu meyimpan objek Pasien dan TenagaMedis di atribut, tapi objek-objek tersebut tetap berdiri sendiri.

Komposisi:

    class RekamMedis:
        def __init__(self,diagnosis):
            self.diagnosis = diagnosis
    
    class Pasien:
        def __init__(self,nama,umur,catatanMedis):
            self.nama = nama
            self.umur = umur
            self.RekamMedis = RekamMedis(catatanMedis)
Objek RekamMedis diciptakan langsung di dalam class pasien.

Program ini juga menerapkan konsep inheritance
Superclass dan Subclass:

    #superclass
    class TenagaMedis:
        def __init__(self,nama,peran,idTenagaMedis):
            self._nama = nama 
            self.peran = peran
            self.__idTenagaMedis = idTenagaMedis

    #subclass
    class Dokter(TenagaMedis):
        def __init__(self, nama, peran,spesialis,idTenagaMedis):
            super().__init__(nama, peran,idTenagaMedis)
            self.spesialis = spesialis

    class Perawat(TenagaMedis):
    def __init__(self, nama, peran,shift,idTenagaMedis):
        super().__init__(nama, peran,idTenagaMedis,)
        self.shift = shift

Di setiap subclass memiliki atribut unik yang membedakan subclass dengan parent class.


Overriding:

    #overriding
    def periksaPasien(self, pasien):
        print(f"Dokter {self._nama} spesialis {self.spesialis} sedang mendiagnosis pasien {pasien.nama}")
Ketika menjalankan kode dokter2.periksaPasien(pasien3) program akan menjalankan isi method milik dokter(Subclass) bukan milik TenagaMedis (parentclass).

Protected dan private:

    class TenagaMedis:
        def __init__(self,nama,peran,idTenagaMedis):
            self._nama = nama #protected
            self.peran = peran
            self.__idTenagaMedis = idTenagaMedis #private

Atribut nama menjadi protected, dan menambahkan atribut baru bernama idTenagaMedis sebagai private. 

Panduan Pengujian:
1. Untuk menguji asosiasi menjalankan kode

       # coba asosiasi
        print("1. Coba asosiasi")
        dokter.periksaPasien(pasien2)
Jika outputnya "Dokter dr.Badrul spesialis pediatri sedang mendiagnosis pasien Dina", maka asosiasi pemanggilan berhasil dijalankan

2. Untuk menguji agregasi jalankan kode
        
        # #coba agregasi
        print("2. Coba agredasi")
        print(janji1.lihatStatus())
Jika outputnya "Status janji temu pasien Andi dengan dr.Badrul: telah dikonfirmasi", maka pemanggilan agregasi berhasil dijalankan

3. Untuk menguji komposisi jalankan kode
   
        # #coba komposisi
        print("3. Coba komposisi")
        print(f"Catatan rekam medis {pasien1.nama}: {pasien1.RekamMedis.diagnosis}")
Jika outputnya "Catatan rekam medis Andi: demam tinggi sejak kemarin", maka pemanggilan komposisi berhasil dijalankan

4. Untuk menguji protected jalankan kode
        
        # coba protacted
        print("5. Coba protected")
        dokter.periksaPasien(pasien1)
Jika outputnya "Dokter dr.Badrul spesialis pediatri sedang mendiagnosis pasien Andi", maka pemanggilan komposisi berhasil dijalankan

5. Untuk menguji atribut protected dan private jalankan kode

        # coba private
        print("4. Coba private")
        print(f"ID {dokter._nama} : {dokter.getId()}")  #memanggil id dokter Badrul
        print(f"ID {dokter2._nama} : {dokter2.getId()}") #memanggil id dokter Dodi
Jika outputnya:
"ID dr.Badrul : D001
 ID dr.Dodi : D002"
 maka pemanggilan atribut protected dan private berhasil

