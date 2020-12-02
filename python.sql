-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2020 at 09:32 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `order_id` int(5) NOT NULL,
  `member_id` int(5) NOT NULL,
  `book_id` int(5) NOT NULL,
  `issue_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`order_id`, `member_id`, `book_id`, `issue_date`, `return_date`) VALUES
(10001, 10008, 10005, '2020-11-28', NULL),
(10002, 10006, 10007, '2020-11-26', '2020-11-30'),
(10003, 10012, 10005, '2020-11-14', '2020-11-30'),
(10004, 10001, 10002, '2020-11-06', NULL),
(10005, 10007, 10009, '2020-11-25', '2020-11-28'),
(10006, 10011, 10001, '2020-11-30', NULL),
(10007, 10004, 10006, '2020-11-03', NULL),
(10008, 10003, 10009, '2020-10-15', NULL),
(10009, 10006, 10003, '2020-11-21', NULL),
(10010, 10009, 10010, '2020-11-17', '2020-11-23'),
(10012, 10001, 10006, '2020-10-01', NULL),
(10013, 10005, 10010, '2020-12-01', '2020-12-01'),
(10014, 10011, 10005, '2020-12-01', NULL),
(10015, 10006, 10006, '2020-12-01', '2020-12-01'),
(10016, 10009, 10006, '2020-12-01', NULL),
(10017, 10009, 10006, '2020-12-01', NULL),
(10018, 10010, 10009, '2020-12-01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int(5) NOT NULL,
  `name` varchar(25) NOT NULL,
  `genre` varchar(15) DEFAULT NULL,
  `author` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `name`, `genre`, `author`) VALUES
(10001, 'First Book', 'Science', 'Einstein'),
(10002, 'New Book', 'Fiction', 'Einstein 2'),
(10003, 'History of Mankind', 'history', 'socrates'),
(10004, 'The Silent Monk', 'philosophy', 'Confucuiuos'),
(10005, 'Dawn', 'philosophy', 'anonymous'),
(10006, 'India', 'history', 'tagore'),
(10007, 'Maths', 'maths', 'rd sharma'),
(10009, 'dummy', 'fiction', 'dummy'),
(10010, 'untitled', 'unknown', 'anonymous'),
(10011, 'titanic', 'mystery', 'rose'),
(10013, 'enigma', 'maths', 'peter shor');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `member_id` int(5) NOT NULL,
  `name` varchar(15) NOT NULL,
  `contact` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member_id`, `name`, `contact`) VALUES
(10001, 'Tasneem', '1234567890'),
(10002, 'Taher', '1234567890'),
(10003, 'Fatima', '1234567890'),
(10004, 'Ubai', '1234567890'),
(10005, 'Sakina', '1234567890'),
(10006, 'Rishabh', '1234567890'),
(10007, 'Ankit', '1234567890'),
(10008, 'Anita', '1234567890'),
(10009, 'Mayur', '1234567890'),
(10010, 'Frank', '1234567890'),
(10011, 'Anny', '1234567890'),
(10012, 'Dinesh', '1234567890');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `member_id` (`member_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`member_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `order_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10019;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10017;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `member_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10020;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
