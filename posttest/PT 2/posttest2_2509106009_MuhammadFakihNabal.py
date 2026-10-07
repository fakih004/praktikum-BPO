#superclass
class TenagaMedis:
    def __init__(self,nama,peran,idTenagaMedis):
        self._nama = nama #protected
        self.peran = peran
        self.__idTenagaMedis = idTenagaMedis #private

    def getId(self):
        return self.__idTenagaMedis

    # Asosiasi
    def periksaPasien(self, pasien):
        print(f"{self._nama} sedang memeriksa {pasien.nama}, pasien dengan diagnosis {pasien.RekamMedis.diagnosis}")



#subclass
class Dokter(TenagaMedis):
    def __init__(self, nama, peran,spesialis,idTenagaMedis):
        super().__init__(nama, peran,idTenagaMedis)
        self.spesialis = spesialis

    #overriding
    def periksaPasien(self, pasien):
        print(f"Dokter {self._nama} spesialis {self.spesialis} sedang mendiagnosis pasien {pasien.nama}")



class Perawat(TenagaMedis):
    def __init__(self, nama, peran,shift,idTenagaMedis):
        super().__init__(nama, peran,idTenagaMedis,)
        self.shift = shift


    
#komposisi
class RekamMedis:
    def __init__(self,diagnosis):
        self.diagnosis = diagnosis

class Pasien:
    def __init__(self,nama,umur,catatanMedis):
        self.nama = nama
        self.umur = umur
        self.RekamMedis = RekamMedis(catatanMedis)

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
    namaInstansi = "Rumah Sakih Sayang Anak"
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



dokter = Dokter("dr.Badrul", "Dokter Anak", "pediatri", "D001")
dokter2 = Dokter("dr.Dodi", "dokter bedah", "Ortopedi", "D002")
perawat = TenagaMedis("Budi", "perawat", "UGD")
pasien1 = Pasien("Andi",14,"demam tinggi sejak kemarin")
pasien2 = Pasien("Dina",12,"batuk pilek")
pasien3 = Pasien("Rasil", 24, "fraktur di lengan")
janji1 = JanjiTemu(pasien1,dokter,"23 september 2070", "telah dikonfirmasi")
janji2 = JanjiTemu(pasien1,dokter,"29 september 2070", "masih dipending")


# coba asosiasi
print("1. Coba asosiasi")
dokter.periksaPasien(pasien2)

# #coba agregasi
print("2. Coba agredasi")
print(janji1.lihatStatus())

# #coba komposisi
print("3. Coba komposisi")
print(f"Catatan rekam medis {pasien1.nama}: {pasien1.RekamMedis.diagnosis}")

# coba overridingg
print("4. Coba overriding")
dokter2.periksaPasien(pasien3)

# coba protacted
print("5. Coba protected")
dokter.periksaPasien(pasien1)

# coba private
print("4. Coba private")
print(f"ID dokter {dokter._nama} : {dokter.getId()}")  #memanggil id dokter Badrul
print(f"ID dokter {dokter2._nama} : {dokter2.getId()}") #memanggil id dokter Dodi
