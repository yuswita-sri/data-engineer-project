-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Bulan Mei 2025 pada 21.15
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nifi_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `penjualan`
--

CREATE TABLE `penjualan` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `produk` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `harga` decimal(12,2) DEFAULT NULL,
  `region` varchar(50) DEFAULT NULL,
  `profit` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penjualan`
--

INSERT INTO `penjualan` (`id`, `tanggal`, `produk`, `quantity`, `harga`, `region`, `profit`) VALUES
(1, '2024-01-01', 'Laptop', 5, 10000000.00, 'Jakarta', 10000000.00),
(2, '2024-02-02', 'Smartphone', 10, 50000000.00, 'Bandung', 460000000.00),
(3, '2024-03-03', 'Mouse', 20, 200000.00, 'Jakarta', 1000000.00),
(4, '2024-04-12', 'Laptop', 5, 10000000.00, 'Jakarta', 10000000.00),
(5, '2024-05-16', 'Smartphone', 10, 50000000.00, 'Bandung', 460000000.00),
(6, '2024-06-03', 'Mouse', 20, 200000.00, 'Jakarta', 1000000.00),
(7, '2024-07-01', 'Laptop', 5, 10000000.00, 'Jakarta', 10000000.00),
(8, '2024-08-20', 'Smartphone', 10, 50000000.00, 'Bandung', 460000000.00),
(9, '2024-09-03', 'Mouse', 20, 200000.00, 'Jakarta', 1000000.00),
(10, '2024-10-01', 'Laptop', 5, 10000000.00, 'Jakarta', 10000000.00);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `penjualan`
--
ALTER TABLE `penjualan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `penjualan`
--
ALTER TABLE `penjualan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
