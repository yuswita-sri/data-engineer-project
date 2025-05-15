import pandas as pd

## 1. ekstract data dari Excel
data = pd.read_csv("stores-data-set.csv", sep=';')
print("Data Asli")
print(data.head())

## 2. Transform = membersihkan data
# - hapus duplikasi data
data = data.drop_duplicates()

# - hapus data kosong
data = data.dropna()

# - tambah kolom baru
data['full_name'] = data['first_name'] + ' ' + data['last_name']
data['total_harga'] = data['quantity']*data['harga']
data['total_per_produk'] = data.groupby('produk')['total_harga'].transform('sum')

print("\nData Baru : ")
print(data.head())

## 3. Data load ke CSV
data.to_csv('data_penjualan_clean.csv', index=False)

# ke SQLite (db sederhana)
import sqlite3
conn = sqlite3.connect('database_penjualan.db')
data.to_sql('penjualan', conn, if_exists='replace', index=False)
conn.close()
print("Data behasil disimpan ke database sederhana")