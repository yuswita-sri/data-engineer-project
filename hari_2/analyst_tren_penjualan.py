import pandas as pd

data = pd.read_csv('data_penjualan_profit.csv', sep=",")

# konversi tanggal ke bulan 
data['bulan'] = pd.to_datetime(data['tanggal']).dt.month_name()

# 1. Produk terlaris
produk_terlaris = data.groupby('produk')['quantity'].sum().sort_values(ascending=False)
print("Produk terlaris : \n", produk_terlaris)

# 2. Profit perbulan
profit_bulanan = data.groupby('bulan')['profit'].sum()
print("\nProfit Bulanan :\n", profit_bulanan)

# output
produk_terlaris.to_csv("produk_terlaris.csv")
print("Produk terlaris berhasil disimpan")
profit_bulanan.to_csv("profit_bulanan.csv")
print("\nProfit bulanan berhasil disimpan")
