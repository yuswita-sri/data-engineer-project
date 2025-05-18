import pandas as pd

data_penjualan = pd.read_csv('data_penjualan_clean.csv', sep=',')
data_produk = pd.read_csv('data_produk.csv', sep=',')

# merge data
data_merge = pd.merge(data_penjualan, data_produk, on='produk', how='left')

# Hitung Profit
data_merge['profit'] = data_merge['total_harga'] - (data_merge['harga_beli']*data_merge['quantity'])

# Rata-rata profit per Kategori
print("Rata-rata profit per kategori : ")
rata_rata = data_merge.groupby('kategori')['profit'].mean()
print(rata_rata)

# output
data_merge.to_csv("data_penjualan_profit.csv", index=False)
print("\nData profit berhasil disimpan")