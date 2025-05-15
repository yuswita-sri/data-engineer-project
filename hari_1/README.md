# PROYEK DATA ENGINEER

Latihan ini menunjukkan proses ETL (Extract, Transform, Load) sederhana menggunakan Python dan pandas. Data diekstrak dari file Excel (CSV format), dibersihkan dan ditransformasi, lalu disimpan ke dalam file CSV baru dan database SQLite.

- Hari 1 : Extract, Transform dan Load Data Penjualan menggunakan Python dan pandas

## Fitur

- Membaca data dari Excel
- Menghapus duplikasi data
- Menghapus data kosong
- Menambah kolom baru
- Menyimpan hasil ke CSV dan SQLite

## Langkah-langkah

### 1. Extract

- Membaca data dari File 'stores-data-set'.csv
- Delimiter yang digunakan adalah ';'

### 2. Transform

- Menghapus data duplikat
- Menghapus baris yang memiliki atribut kosong
- Menambahkan dua kolom baru :
  - 'full_name' = gabungan dari 'first_name' dan 'last_name'
  - 'total_harga' = hasil perkalian 'quantity' dan 'harga'
  - 'total_per_produk' = hasil pengelompokan (grouping) berdasarkan kolom produk kemudian menjumlahkan nilai pada
    kolom total_harga

### 3. Load

- Load data menjadi file data_penjualan_clean.csv
- Load data menjadi database_penjualan.db
