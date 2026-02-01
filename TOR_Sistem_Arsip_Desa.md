# TERMS OF REFERENCE (TOR)
# KERANGKA ACUAN KERJA (KAK)

**Nama Proyek** : Pengembangan Sistem Informasi Arsip Digital Desa Berbasis Web  
**Platform**    : Web Application (Python Flask)  
**Tahun**       : 2026

---

## 1. LATAR BELAKANG
Pengelolaan arsip administrasi di kantor desa saat ini seringkali masih dilakukan secara konvensional (manual). Dokumen fisik memiliki risiko hilang, rusak karena faktor usia/bencana, dan sulit untuk dicari kembali ketika dibutuhkan dalam waktu cepat.

Seiring dengan perkembangan teknologi informasi, transformasi digital di tingkat pemerintahan desa menjadi kebutuhan mendesak untuk meningkatkan efisiensi pelayanan dan tata kelola administrasi yang lebih baik. Oleh karena itu, dibutuhkan sebuah **Sistem Informasi Arsip Digital** yang sederhana namun handal, yang dapat membantu perangkat desa dalam menyimpan, mengelola, dan menelusuri dokumen penting secara digital.

## 2. MAKSUD DAN TUJUAN
### 2.1 Maksud
Membangun sebuah aplikasi berbasis web untuk digitalisasi arsip surat masuk, surat keluar, dan dokumen penting lainnya di lingkungan kantor desa.

### 2.2 Tujuan
1.  **Efisiensi**: Mempercepat proses pencarian dokumen (searching & filtering).
2.  **Keamanan**: Mencegah kehilangan data fisik dengan adanya backup digital.
3.  **Aksesibilitas**: Memudahkan perangkat desa mengakses arsip kapan saja melalui dashboard yang terpusat.
4.  **Modernisasi**: Meningkatkan citra pelayanan desa dengan antarmuka sistem yang modern dan profesional.

## 3. RUANG LINGKUP PEKERJAAN (SCOPE OF WORK)
Sistem yang dikembangkan akan mencakup fitur-fitur utama sebagai berikut:

### 3.1 Manajemen Pengguna (Authentication)
*   Sistem Login untuk Administrator (Keamanan Akses).
*   Manajemen Password Admin.

### 3.2 Manajemen Arsip (CRUD)
*   **Create**: Input data arsip baru (Judul, Kategori, Deskripsi, Upload File).
*   **Read**: Menampilkan daftar arsip dalam bentuk tabel yang rapi.
*   **Update**: Mengubah data atau mengganti file arsip yang salah.
*   **Delete**: Menghapus data arsip yang tidak diperlukan lagi.

### 3.3 Fitur Unggulan
*   **Pencarian Cerdas**: Mencari arsip berdasarkan kata kunci judul atau deskripsi.
*   **Filter Kategori**: Menyaring dokumen berdasarkan jenis (Surat Masuk, Surat Keluar, SK, Laporan, dll).
*   **File Viewer**: Fitur untuk melihat langsung (Preview) atau mengunduh (Download) lampiran dokumen (PDF/Gambar).
*   **Dashboard Statistik**: Ringkasan jumlah total dokumen yang tersimpan.

### 3.4 Antarmuka Pengguna (UI/UX)
*   Desain **Premium & Modern** dengan gaya visual yang bersih (Clean Look).
*   **Responsive**, dapat diakses dengan baik melalui Laptop/PC mapun Tablet.
*   Navigasi Sidebar yang intuitif.

## 4. SPESIFIKASI TEKNIS
Sistem ini dibangun menggunakan teknologi *Open Source* yang handal dan mudah dikembangkan:

*   **Bahasa Pemrograman**: Python 3.x
*   **Framework Web**: Flask (Microframework yang ringan dan cepat)
*   **Database**: SQLite (Ringan, *Serverless*, mudah di-backup berupa file tunggal `.db`)
*   **Frontend**: HTML5, CSS3 (Modern Floating/Glassmorphism Design), JavaScript (Chart.js optional)
*   **Environment**: Localhost (Dapat dideploy ke server hosting/VPS)

## 5. KELUARAN (DELIVERABLES)
1.  **Source Code Aplikasi**: Kode program lengkap yang siap dijalankan.
2.  **Database**: File database `arsip.db`.
3.  **Dokumentasi**: Panduan instalasi dan penggunaan singkat.

## 6. PENUTUP
Kerangka Acuan Kerja ini disusun sebagai pedoman dalam pengembangan Sistem Informasi Arsip Digital Desa, dengan harapan dapat diimplementasikan untuk mendukung kinerja administrasi desa yang lebih tertib dan efisien.
