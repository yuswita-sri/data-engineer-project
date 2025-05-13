import pandas as pd

# 1. ekstract data dari Excel
df = pd.read_csv("stores-data-set.csv", sep=';')
print("Data Asli")
print(df.head())

# 2. Transform = membersihkan data
# - hapus duplikasi data
df = df.drop_duplicates()

# - tambah kolom baru
df['full_name'] = df['first_name'] + ' ' + df['last_name']
df['total_harga'] = df['quantity']*df['harga']

# ubah format tanggal
df['tanggal'] = pd.to_datetime(df['tanggal'], format='%d/%m/%Y', errors='coerce')
df['tanggalstr'] = df['tanggal'].dt.strftime('%d %B %Y')

print("\nData Baru : ")
print(df.head())

# 3. Data load ke CSV
df.to_csv('data_penjualan_clean.csv', index=False)

# ke SQLite (db sederhana)
import sqlite3
conn = sqlite3.connect('database_penjualan.db')
df.to_sql('penjualan', conn, if_exists='replace', index=False)
conn.close()

print("Data behasil disimpan ke database sederhana")