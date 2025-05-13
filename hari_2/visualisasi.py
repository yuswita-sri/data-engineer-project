import matplotlib.pyplot as plt
import pandas as pd

produk_terlaris = pd.read_csv('produk_terlaris.csv', sep=',')
profit_bulanan = pd.read_csv('profit_bulanan.csv', sep=',')

# Plot produk terlaris
produk_terlaris.plot(kind='bar', title='Produk Terlaris')
plt.ylabel('Jumlah Terjual')
plt.savefig('produk_terlaris.png') #menyimpan sebagai gambar
plt.show()

# plot profit bulanan
profit_bulanan.plot(kind='line', marker='o', title='Profit Bulanan')
plt.ylabel('Profit (Rp)')
plt.savefig('profit_bulanan.png')
plt.show()