# Metodologi Pengembangan Sistem Informasi Arsip Digital Desa

Berikut adalah deskripsi narasi tahapan pengembangan aplikasi yang disesuaikan dengan alur Input, Proses, dan Pelaporan untuk **Sistem Informasi Arsip Digital Desa (Desa Sagaracipta)**.

---

## 1. Tahap Input
Tahap ini merupakan fase awal pengumpulan data untuk menentukan kebutuhan spesifik aplikasi agar tepat guna bagi perangkat Desa Sagaracipta.

### a. Data Primer
Data primer diperoleh melalui interaksi langsung dengan lingkungan kerja di kantor desa.
*   **Wawancara & Observasi**: Dilakukan tanya jawab dengan sekretaris desa dan staf administrasi untuk mengetahui kendala utama dalam pengelolaan arsip saat ini. Ditemukan bahwa pencarian dokumen lama memakan waktu dan risiko kerusakan fisik dokumen cukup tinggi.
*   **Analisis Kebutuhan Pengguna**: Mengidentifikasi fitur prioritas yang dibutuhkan perangkat desa, yaitu kemudahan pencarian (*search*), pengelompokan kategori (*categorization*), dan tampilan yang ramah pengguna (*user-friendly*).

### b. Data Sekunder
Data sekunder dikumpulkan sebagai referensi pendukung pengembangan sistem.
*   **Sampel Dokumen Arsip**: Mengumpulkan contoh fisik atau format digital dari *Surat Masuk*, *Surat Keluar*, *Dokumen Peraturan*, dan *Laporan Keuangan* untuk merancang struktur database yang sesuai.
*   **Studi Literatur**: Mempelajari regulasi kearsipan desa dan standar keamanan data untuk diterapkan pada sistem login administrator.

---

## 2. Tahap Proses
Pada tahap ini, data yang telah dikumpulkan diolah dan diterjemahkan ke dalam rancangan teknis serta implementasi program.

### a. Eksplorasi
Tahap eksplorasi bertujuan untuk memahami kondisi nyata pengelolaan arsip digital di Desa Sagaracipta secara mendalam.
*   **Pemetaan Alur Kerja (Workflow)**: Penulis memetakan alur pelayanan administrasi yang sedang berjalan, mulai dari penerimaan surat hingga penyimpanan.
*   **Analisis Masalah**: Mengidentifikasi titik lemah pada sistem manual, seperti duplikasi penomoran atau ketidakteraturan penyimpanan file di komputer lokal.
*   **Perancangan Solusi**: Merumuskan solusi berupa sistem berbasis web lokal yang dapat diakses melalui jaringan internal atau *stand-alone* di komputer admin.

### b. Pembangunan Aplikasi
Tahap ini adalah eksekusi teknis pembuatan perangkat lunak menggunakan teknologi **Python (Flask)** dan **SQLite**.
*   **Perancangan Database**: Membuat skema tabel `archives` untuk menyimpan metadata arsip (judul, kategori, deskripsi, tanggal, path file).
*   **Pengembangan Backend**: Membangun logika sistem untuk fitur *Create* (Tambah), *Read* (Lihat/Cari), *Update* (Edit), dan *Delete* (Hapus), serta fitur keamanan login admin.
*   **Desain Antarmuka (UI/UX)**: Mengimplementasikan desain antarmuka "Premium & Modern" menggunakan CSS kustom. Fokus utama adalah pada *dashboard* yang informatif (statistik) dan formulir input yang intuitif dengan fitur *drag-and-drop* file.
*   **Pengujian (Testing)**: Melakukan uji coba fungsionalitas (Black Box Testing) untuk memastikan fitur pencarian, filter kategori, dan upload file berjalan lancar tanpa *bug*.

---

## 3. Tahap Pelaporan (Output)
Tahap akhir adalah penyajian hasil dari seluruh rangkaian pengembangan sistem.

*   **Implementasi Sistem**: Aplikasi **Sistem Informasi Arsip Digital Desa** yang siap digunakan, memiliki kemampuan manajemen arsip elektronik yang terstruktur, aman, dan mudah diakses.
*   **Dokumentasi Pengguna**: Tersedianya *User Guide* (Panduan Pengguna) yang memuat instruksi lengkap penggunaan aplikasi dari login hingga manajemen arsip.
*   **Laporan Kerja Praktik**: Dokumen tertulis yang merangkum seluruh proses analisis, perancangan, hingga implementasi sistem di Desa Sagaracipta sebagai bentuk pertanggungjawaban akademis dan profesional.
