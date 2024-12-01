-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2024 at 06:50 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quan_ly_viec_lam`
--

-- --------------------------------------------------------

--
-- Table structure for table `cong_viec`
--

CREATE TABLE `cong_viec` (
  `cong_viec_id` int(11) NOT NULL,
  `ten_cong_viec` varchar(100) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `luong` float DEFAULT NULL,
  `ngay_dang` date DEFAULT NULL,
  `nha_tuyen_dung_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cong_viec`
--

INSERT INTO `cong_viec` (`cong_viec_id`, `ten_cong_viec`, `mo_ta`, `luong`, `ngay_dang`, `nha_tuyen_dung_id`) VALUES
(4, 'cccccc', 'cccccccc', 222, '2024-06-11', 1);

-- --------------------------------------------------------

--
-- Table structure for table `lich_tiep_nhan_giao_dich_lam`
--

CREATE TABLE `lich_tiep_nhan_giao_dich_lam` (
  `lich_tiep_nhan_id` int(11) NOT NULL,
  `ung_vien_id` int(11) DEFAULT NULL,
  `cong_viec_id` int(11) DEFAULT NULL,
  `nha_tuyen_dung_id` int(11) DEFAULT NULL,
  `ngay_nop_hs` date DEFAULT NULL,
  `trang_thai` enum('Đã tiếp nhận','Đã xử lý','Đã hủy') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lich_tiep_nhan_giao_dich_lam`
--

INSERT INTO `lich_tiep_nhan_giao_dich_lam` (`lich_tiep_nhan_id`, `ung_vien_id`, `cong_viec_id`, `nha_tuyen_dung_id`, `ngay_nop_hs`, `trang_thai`) VALUES
(6, 3, 4, 1, '0000-00-00', 'Đã tiếp nhận');

-- --------------------------------------------------------

--
-- Table structure for table `nha_tuyen_dung`
--

CREATE TABLE `nha_tuyen_dung` (
  `nha_tuyen_dung_id` int(11) NOT NULL,
  `ten_cong_ty` varchar(100) NOT NULL,
  `dia_chi` text DEFAULT NULL,
  `dien_thoai` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nha_tuyen_dung`
--

INSERT INTO `nha_tuyen_dung` (`nha_tuyen_dung_id`, `ten_cong_ty`, `dia_chi`, `dien_thoai`, `email`, `created_at`) VALUES
(1, 'cccccc', 'cccccccc', '22222222222', 'vvvvvvv', '2024-06-26 02:31:15');

-- --------------------------------------------------------

--
-- Table structure for table `thong_ke`
--

CREATE TABLE `thong_ke` (
  `thong_ke_id` int(11) NOT NULL,
  `ten_bieu_do` varchar(100) DEFAULT NULL,
  `mo_ta` text DEFAULT NULL,
  `du_lieu` text DEFAULT NULL,
  `ngay_tao` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ung_vien`
--

CREATE TABLE `ung_vien` (
  `ung_vien_id` int(11) NOT NULL,
  `ho_ten` varchar(100) NOT NULL,
  `ngay_sinh` date DEFAULT NULL,
  `gioi_tinh` enum('Nam','Nữ','Khác') DEFAULT NULL,
  `dia_chi` text DEFAULT NULL,
  `dien_thoai` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ung_vien`
--

INSERT INTO `ung_vien` (`ung_vien_id`, `ho_ten`, `ngay_sinh`, `gioi_tinh`, `dia_chi`, `dien_thoai`, `email`, `created_at`) VALUES
(2, 'cccccccc', '0000-00-00', 'Nam', 'ccccccccc', '11111111', 'cccccccc', '2024-06-26 02:36:04'),
(3, 'cccccc', '2024-06-11', 'Nữ', 'cc', '22', 'cccccc', '2024-06-26 03:10:57');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cong_viec`
--
ALTER TABLE `cong_viec`
  ADD PRIMARY KEY (`cong_viec_id`),
  ADD KEY `fk_nha_tuyen_dung` (`nha_tuyen_dung_id`);

--
-- Indexes for table `lich_tiep_nhan_giao_dich_lam`
--
ALTER TABLE `lich_tiep_nhan_giao_dich_lam`
  ADD PRIMARY KEY (`lich_tiep_nhan_id`),
  ADD KEY `fk_ung_vien` (`ung_vien_id`),
  ADD KEY `fk_cong_viec` (`cong_viec_id`),
  ADD KEY `fk_nha_tuyen_dung_lich_tiep_nhan` (`nha_tuyen_dung_id`);

--
-- Indexes for table `nha_tuyen_dung`
--
ALTER TABLE `nha_tuyen_dung`
  ADD PRIMARY KEY (`nha_tuyen_dung_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `thong_ke`
--
ALTER TABLE `thong_ke`
  ADD PRIMARY KEY (`thong_ke_id`);

--
-- Indexes for table `ung_vien`
--
ALTER TABLE `ung_vien`
  ADD PRIMARY KEY (`ung_vien_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cong_viec`
--
ALTER TABLE `cong_viec`
  MODIFY `cong_viec_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `lich_tiep_nhan_giao_dich_lam`
--
ALTER TABLE `lich_tiep_nhan_giao_dich_lam`
  MODIFY `lich_tiep_nhan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `nha_tuyen_dung`
--
ALTER TABLE `nha_tuyen_dung`
  MODIFY `nha_tuyen_dung_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `thong_ke`
--
ALTER TABLE `thong_ke`
  MODIFY `thong_ke_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ung_vien`
--
ALTER TABLE `ung_vien`
  MODIFY `ung_vien_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cong_viec`
--
ALTER TABLE `cong_viec`
  ADD CONSTRAINT `fk_nha_tuyen_dung` FOREIGN KEY (`nha_tuyen_dung_id`) REFERENCES `nha_tuyen_dung` (`nha_tuyen_dung_id`);

--
-- Constraints for table `lich_tiep_nhan_giao_dich_lam`
--
ALTER TABLE `lich_tiep_nhan_giao_dich_lam`
  ADD CONSTRAINT `fk_cong_viec` FOREIGN KEY (`cong_viec_id`) REFERENCES `cong_viec` (`cong_viec_id`),
  ADD CONSTRAINT `fk_nha_tuyen_dung_lich_tiep_nhan` FOREIGN KEY (`nha_tuyen_dung_id`) REFERENCES `nha_tuyen_dung` (`nha_tuyen_dung_id`),
  ADD CONSTRAINT `fk_ung_vien` FOREIGN KEY (`ung_vien_id`) REFERENCES `ung_vien` (`ung_vien_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
