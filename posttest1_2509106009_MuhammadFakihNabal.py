class TenagaMedis:
    def __init__(self,nama,peran,spesialis):
        self.nama = nama
        self.peran = peran
        self.spesialis = spesialis

class Pasien:
    def __init__(self,nama,umur,catatanMedis):
        self.nama = nama
        self.umur = umur
        self.__catatanMedis = catatanMedis

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
    namaInstansi = "Klinik sayang anak"
    totalJanjiTemu = 0
    jamOprasional = "07.00 - 00.00"

    def __init__(self,pasien,tenagaMedis,tanggal,status):
        self.pasien = pasien
        self.tenagaMedis = tenagaMedis
        self.tanggal = tanggal
        self.__status = status
        JanjiTemu.totalJanjiTemu += 1

    def lihatStatus(self):
        return f"status janji temu saat ini : {self.__status}"

    @classmethod
    def ubahJamOperasional(cls, jamBaru):
        cls.jamOprasional = jamBaru

    @staticmethod
    def validasiStatus(status):
        statusValid = ["pending", "dikonfirmasi", "selesai"]
        return status in statusValid

    


dokter = TenagaMedis("dr. Badrul", "Dokter Anak", "pediatri")
perawat = TenagaMedis("Budi", "perawat", "UGD")
pasien1 = Pasien("Andi",14,"demam tinggi sejak kemarin")
pasien1 = Pasien("Dina",12,"batuk pilek")
janji1 = JanjiTemu(pasien1.nama,dokter.nama,"23 september 2070", "telah dikonfirmasi")
janji1 = JanjiTemu(pasien1.nama,dokter.nama,"29 september 2070", "masih dipending")

# #instancemethod
# janji1.lihatStatus()
# print(janji1.lihatStatus())

# #classmethod
# JanjiTemu.ubahJamOperasional("05.00 - 12.00")
# print("Jam operasional baru:", JanjiTemu.jamOprasional)

# #staticmethod
# status = JanjiTemu.validasiStatus("selesa")
# print("apakah statusnya valid?:", status)

# #getter & setter
# pasien1.catatanMedis = "batuk berdahak" # valid
# pasien1.catatanMedis = "" # gak valid
# print("Catatan:", pasien1.catatanMedis)

print("Nama Instansi : ",JanjiTemu.namaInstansi)
print("jam operasional : ",JanjiTemu.jamOprasional)
print("total janji temu sekarang : ",JanjiTemu.totalJanjiTemu)
print(janji1.lihatStatus())