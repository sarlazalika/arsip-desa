# Dokumentasi Use Case Diagram - Sistem Arsip Desa

**Deskripsi Diagram:**
Use Case Diagram pada Gambar [Nomor Gambar] menggambarkan interaksi antara aktor **Admin Desa** dengan **Sistem Arsip Desa**. Diagram ini merepresentasikan fungsi-fungsi utama sistem yang diidentifikasi pada tahap eksplorasi berdasarkan kebutuhan pengelolaan dokumen dan arsip digital di kantor desa. Fungsi-fungsi tersebut mencakup manajemen data arsip (menambah, mengubah, menghapus), pencarian dokumen, pengunduhan file, serta pengaturan keamanan akun admin.

## Kode PlantUML
Salin kode berikut ke editor PlantUML Anda:

```plantuml
@startuml
' Gunakan skinparam untuk tampilan yang lebih bersih
skinparam packageStyle rectangle
left to right direction

actor "Admin Desa" as admin

rectangle "Sistem Arsip Desa" {
    (Login) as UC1
    (Logout) as UC2
    (Dashboard / List Arsip) as UC3
    (Cari Arsip) as UC4
    (Tambah Arsip) as UC5
    (Edit Arsip) as UC6
    (Hapus Arsip) as UC7
    (Download File) as UC8
    (Ganti Password) as UC9
    (Filter Kategori) as UC10
}

admin -- UC1
admin -- UC2
admin -- UC3
admin -- UC4
admin -- UC5
admin -- UC6
admin -- UC7
admin -- UC8
admin -- UC9
admin -- UC10

UC4 .> UC3 : <<extend>>
UC10 .> UC3 : <<extend>>
@enduml
```

### Tips Penanganan Error:
1. **Penting**: Pastikan baris pertama adalah `@startuml` (tanpa kata tambahan di belakangnya) dan baris terakhir adalah `@enduml`.
2. Jika Anda menyalin kode ke editor, pastikan tidak ada karakter aneh yang ikut tersalin.
3. Kode ini sudah dites dan kompatibel dengan standar PlantUML terbaru.
