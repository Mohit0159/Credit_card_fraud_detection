-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2023 at 11:41 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `credit_card_fraud_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `prediction_page`
--

CREATE TABLE `prediction_page` (
  `distance_from_home` int(50) NOT NULL,
  `distance_from_last_transaction` double NOT NULL,
  `ratio_to_median_purchase_price` double NOT NULL,
  `repeatretailer` varchar(50) NOT NULL,
  `chip` varchar(50) NOT NULL,
  `pin_number` varchar(50) NOT NULL,
  `onlineorder` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `prediction_output` varchar(350) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `prediction_page`
--

INSERT INTO `prediction_page` (`distance_from_home`, `distance_from_last_transaction`, `ratio_to_median_purchase_price`, `repeatretailer`, `chip`, `pin_number`, `onlineorder`, `date`, `prediction_output`) VALUES
(42, 12, 75, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-10', '[1.]'),
(45, 47, 25, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(45, 45, 75, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(12, 56, 74, 'No', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(12, 24, 42, 'Yes', 'No', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(12, 24, 42, 'Yes', 'No', 'No', 'Yes', '2023-11-11', '[1.]'),
(12, 24, 32, 'Yes', 'No', 'No', 'Yes', '2023-11-11', '[1.]'),
(12, 24, 32, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(24, 24, 32, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(32, 12, 43, 'Yes', 'Yes', 'No', 'Yes', '2023-11-11', '[1.]'),
(34, 65, 45, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(34, 65, 43, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(45, 24, 35, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '[1.]'),
(45, 36, 78, 'No', 'No', 'No', 'No', '2023-11-11', '[1.]'),
(32, 12, 43, 'Yes', 'Yes', 'No', 'Yes', '2023-11-11', '[1.]'),
(54, 24, 32, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '1'),
(34, 65, 45, 'Yes', 'Yes', 'Yes', 'Yes', '2023-11-11', '1'),
(34, 54, 67, 'No', 'No', 'Yes', 'Yes', '2023-11-11', '1');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
