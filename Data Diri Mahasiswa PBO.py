class Data_Diri_Mahasiswa:
    def __init__(self, nama, nim, prodi, kelas, fakultas, universitas, asal):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelas = kelas
        self.fakultas = fakultas
        self.universitas = universitas
        self.asal = asal


    def start(self):
        print(f"The {self.nama} {self.nim} {self.prodi} {self.kelas} {self.fakultas} {self.universitas} {self.asal} is starting.")

    def stop(self):
        print(f"The {self.nama} {self.nim} {self.prodi} {self.kelas} {self.fakultas} {self.universitas} {self.asal} has stopped.")

My_Data_Diri_Mahasiswa = Data_Diri_Mahasiswa ("Andini Rahmadina", "23091397115", "D4 Manajemen Informatika",  "2023D",  "Vokasi",  "Universitas Negeri Surabaya",  "Kediri")
Data_Diri_Mahasiswa2 = Data_Diri_Mahasiswa ("Putri Indah Lestari", "23091397123", "D4 Administrasi Negara", "2023C",  "Vokasi",  "Universitas Negeri Surabaya", "Surabaya")

My_Data_Diri_Mahasiswa.start()
Data_Diri_Mahasiswa2.stop()