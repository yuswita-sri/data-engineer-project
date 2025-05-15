import pandas as pd

data = pd.read_csv('data_penjualan_profit.csv', sep=',')

produk_terlaris = data.groupby('produk')['quantity'].sum().sort_values(ascending=False)
print("Produk terlaris : \n", produk_terlaris)

produk_terlaris.to_csv("produk_terlaris.csv")
print("Produk terlaris berhasil disimpan")
