from abc import ABC, abstractmethod

#superclass
class TenagaMedis(ABC):
    def __init__(self,nama,peran,idTenagaMedis):
        self._nama = nama #protected
        self.peran = peran
        self.__idTenagaMedis = idTenagaMedis #private

    def getId(self):
        return self.__idTenagaMedis

    # Asosiasi
    @abstractmethod #polimorfime via pewarisan
    def periksaPasien(self, pasien):
        pass

    @abstractmethod #polimorfime via pewarisan
    def daftarTugas(self):
        pass
#subclass
class Dokter(TenagaMedis):
    def __init__(self, nama, peran,spesialis,idTenagaMedis):
        super().__init__(nama, peran,idTenagaMedis)
        self.spesialis = spesialis

    #overriding
    def periksaPasien(self, pasien):
        print(f"Dokter {self._nama} spesialis {self.spesialis} sedang mendiagnosis pasien {pasien.nama}")
        
    # abstract
    def daftarTugas(self):
        print(f"Dokter {self._nama} bertugas memeriksa pasien dan menulis laporan medis")

class Perawat(TenagaMedis):
    def __init__(self, nama, peran,shift,idTenagaMedis):
        super().__init__(nama, peran,idTenagaMedis,)
        self.shift = shift

    # abstract
    def daftarTugas(self):
        print(f"Perawat {self._nama} bertugas merawat pasien")
    # abstract
    def periksaPasien(self, pasien):
        print(f"Perawat {self._nama} sedang memeriksa pasien {pasien.nama} di shift {self.shift}")

#komposisi
class RekamMedis:
    def __init__(self,diagnosis):
        self.diagnosis = diagnosis

class Pasien:
    def __init__(self,nama,umur,catatanMedis):
        self.nama = nama
        self.umur = umur
        self.RekamMedis = RekamMedis(catatanMedis)

    def __str__(self):
        return f"Pasien: {self.nama}, (Umur: {self.umur} tahun)"

    def __eq__(self,other):
        if isinstance(other, Pasien):
            return self.nama == other.nama and self.umur == other.umur
        return False

    @property
    def catatanMedis(self):
        return self.__catatanMedis

    @catatanMedis.setter
    def catatanMedis(self, catatanMedisBaru):
        if len(catatanMedisBaru.strip()) == 0:
            print("Catatan medis tidak boleh kosong")
        else:
            self.__catatanMedis = catatanMedisBaru

        

class JanjiTemu:
    namaInstansi = "Rumah Sakit Sayang anak"
    totalJanjiTemu = 0
    jamOprasional = "07.00 - 00.00"

    def __init__(self,pasien,tenagaMedis,tanggal,status):
        self.pasien = pasien
        self.tenagaMedis = tenagaMedis
        self.tanggal = tanggal
        self.__status = status
        JanjiTemu.totalJanjiTemu += 1

    # agregasi
    def lihatStatus(self):
        return f"Status janji temu pasien {self.pasien.nama} dengan {self.tenagaMedis._nama}: {self.__status} "

    @classmethod
    def ubahJamOperasional(cls, jamBaru):
        cls.jamOprasional = jamBaru

    @staticmethod
    def validasiStatus(status):
        statusValid = ["pending", "dikonfirmasi", "selesai"]
        return status in statusValid

# Duck typing
class Ambulan:
    def Layanan(self):
        print("Ambulan sedang menjemput pasien")

class Apotek:
    def Layanan(self):
        print("Apoteker sedang menyiapkan obat pasien")

def JalankanLayanan(unit):
    unit.Layanan()

dokter = Dokter("dr.Badrul", "Dokter Anak", "pediatri", "D001")
dokter2 = Dokter("dr.Dodi", "dokter bedah", "Ortopedi", "D002")
perawat = Perawat("Budi", "perawat", "Malam", "P001")
pasien1 = Pasien("Andi",14,"demam tinggi sejak kemarin")
pasien2 = Pasien("Dina",12,"batuk pilek")
pasien3 = Pasien("Rasil", 24, "fraktur di lengan")
janji1 = JanjiTemu(pasien1,dokter,"23 september 2070", "telah dikonfirmasi")
janji2 = JanjiTemu(pasien1,dokter,"29 september 2070", "masih dipending")


# # coba asosiasi
# print("1. Coba asosiasi")
# dokter.periksaPasien(pasien2)

# # #coba agregasi
# print("2. Coba agredasi")
# print(janji1.lihatStatus())

# # #coba komposisi
# print("3. Coba komposisi")
# print(f"Catatan rekam medis {pasien1.nama}: {pasien1.RekamMedis.diagnosis}")

# # coba overridingg
# print("4. Coba overriding")
# dokter2.periksaPasien(pasien3)

# # coba protacted
# print("5. Coba protected")
# dokter.periksaPasien(pasien1)

# # coba private
# print("4. Coba private")
# print(f"ID {dokter._nama} : {dokter.getId()}")  #memanggil id dokter Badrul
# print(f"ID {dokter2._nama} : {dokter2.getId()}") #memanggil id dokter Dodi

# coba abstract
# print("6. Coba abstract")
# try:
#         bluePrint = TenagaMedis("dr. Dahlah", "Perawat", "D004")
# except TypeError as e:
#         print("Gagal membuat objek karena abstrak class")
#         print(f"Errornya: {e}")


print("7. coba polimorfisme via pewarisan")
pekerjaRS = [dokter,perawat]

for pekerja in pekerjaRS:
    pekerja.daftarTugas()   
    pekerja.periksaPasien(pasien1)

print("8. duck typing")
JalankanLayanan(Apotek())
JalankanLayanan(Ambulan())

print("9. coba magic method")
#coba __str__
print(pasien1)
#coba __eq__
pasienSama = Pasien("Andi",14,"demam tinggi")
print(f"Apakah pasien1 dan paseinSama punya data yang sama? {pasien1 == pasienSama}")
print(f"Apakah pasien1 dan pasein2 punya data yang sama? {pasien1 == pasien2}")