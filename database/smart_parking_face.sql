-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 10, 2024 at 11:08 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `smart_parking_face`
--

-- --------------------------------------------------------

--
-- Table structure for table `ev_booking`
--
UPDATE `smart_parking_face`.`ev_register` SET `uname` = 'skk3' WHERE `ev_register`.`id` =5

CREATE TABLE `ev_booking` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `station` varchar(30) NOT NULL,
  `carno` varchar(20) NOT NULL,
  `reserve` varchar(20) NOT NULL,
  `slot` int(11) NOT NULL,
  `cimage` varchar(20) NOT NULL,
  `mins` int(11) NOT NULL,
  `plan` int(11) NOT NULL,
  `amount` double NOT NULL,
  `rtime` varchar(20) NOT NULL,
  `etime` varchar(20) NOT NULL,
  `rdate` varchar(15) NOT NULL,
  `edate` varchar(15) NOT NULL,
  `otp` varchar(10) NOT NULL,
  `charge` double NOT NULL,
  `charge_time` int(11) NOT NULL,
  `charge_min` int(11) NOT NULL,
  `charge_sec` int(11) NOT NULL,
  `charge_st` int(11) NOT NULL,
  `pay_mode` varchar(20) NOT NULL,
  `pay_st` int(11) NOT NULL,
  `sms_st` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `verify_mode` int(11) NOT NULL,
  `fimg` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ev_booking`
--


-- --------------------------------------------------------

--
-- Table structure for table `ev_register`
--

CREATE TABLE `ev_register` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(40) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `account` varchar(20) NOT NULL,
  `card` varchar(20) NOT NULL,
  `bank` varchar(20) NOT NULL,
  `amount` double NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ev_register`
--

INSERT INTO `ev_register` (`id`, `name`, `address`, `mobile`, `email`, `account`, `card`, `bank`, `amount`, `uname`, `pass`) VALUES
(1, 'Prem', '55,DD', 9894442716, 'prem@gmail.com', '265454985554', '5236745865219652', 'SBI', 10000, 'prem', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `ev_station`
--

CREATE TABLE `ev_station` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `stype` varchar(20) NOT NULL,
  `num_charger` int(11) NOT NULL,
  `area` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `lat` varchar(20) NOT NULL,
  `lon` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ev_station`
--

INSERT INTO `ev_station` (`id`, `name`, `stype`, `num_charger`, `area`, `city`, `lat`, `lon`, `uname`, `pass`) VALUES
(1, 'station1', 'Private', 8, 'Chatram', 'Trichy', '10.3443', '78.34432', 'station1', '1234'),
(2, 'Station2', 'Private', 10, '33,GG', 'Trichy', '10.4351', '78.4343', 'station2', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `vt_face`
--

CREATE TABLE `vt_face` (
  `id` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `vface` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vt_face`
--

INSERT INTO `vt_face` (`id`, `vid`, `vface`) VALUES
(1, 1, 'User.1.2.jpg'),
(2, 1, 'User.1.3.jpg'),
(3, 1, 'User.1.4.jpg'),
(4, 1, 'User.1.5.jpg'),
(5, 1, 'User.1.6.jpg'),
(6, 1, 'User.1.7.jpg'),
(7, 1, 'User.1.8.jpg'),
(8, 1, 'User.1.9.jpg'),
(9, 1, 'User.1.10.jpg'),
(10, 1, 'User.1.11.jpg'),
(11, 1, 'User.1.12.jpg'),
(12, 1, 'User.1.13.jpg'),
(13, 1, 'User.1.14.jpg'),
(14, 1, 'User.1.15.jpg'),
(15, 1, 'User.1.16.jpg'),
(16, 1, 'User.1.17.jpg'),
(17, 1, 'User.1.18.jpg'),
(18, 1, 'User.1.19.jpg'),
(19, 1, 'User.1.20.jpg'),
(20, 1, 'User.1.21.jpg'),
(21, 1, 'User.1.22.jpg'),
(22, 1, 'User.1.23.jpg'),
(23, 1, 'User.1.24.jpg'),
(24, 1, 'User.1.25.jpg'),
(25, 1, 'User.1.26.jpg'),
(26, 1, 'User.1.27.jpg'),
(27, 1, 'User.1.28.jpg'),
(28, 1, 'User.1.29.jpg'),
(29, 1, 'User.1.30.jpg'),
(30, 1, 'User.1.31.jpg'),
(31, 1, 'User.1.32.jpg'),
(32, 1, 'User.1.33.jpg'),
(33, 1, 'User.1.34.jpg'),
(34, 1, 'User.1.35.jpg'),
(35, 1, 'User.1.36.jpg'),
(36, 1, 'User.1.37.jpg'),
(37, 1, 'User.1.38.jpg'),
(38, 1, 'User.1.39.jpg'),
(39, 1, 'User.1.40.jpg');


AND CONVERT( `ev_register`.`name` USING utf8 ) = 'abdul kader'
AND CONVERT( `ev_register`.`address` USING utf8 ) = 'Nagore'
AND `ev_register`.`mobile` =8667060779
AND CONVERT( `ev_register`.`email` USING utf8 ) = 'abdulkadermr7@gmail.com'
AND CONVERT( `ev_register`.`account` USING utf8 ) = '12243243232'
AND CONVERT( `ev_register`.`card` USING utf8 ) = '245788666543'
AND CONVERT( `ev_register`.`bank` USING utf8 ) = 'Indian Bank'
AND CONCAT( `ev_register`.`amount` ) =10000
AND CONVERT( `ev_register`.`uname` USING utf8 ) = 'skk'
AND CONVERT( `ev_register`.`pass` USING utf8 ) = 'pbkdf2:sha256:150000$zMZm53lg$81c3d5b1914c88864bd019dd95e537bc8ad0453b0ed0a65aceee047994a06e51' LIMIT 1 ;
