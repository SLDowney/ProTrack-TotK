-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.26 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table botw.armor_sets
CREATE TABLE IF NOT EXISTS `armor_sets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sets` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table botw.armor_sets: ~29 rows (approximately)
/*!40000 ALTER TABLE `armor_sets` DISABLE KEYS */;
REPLACE INTO `armor_sets` (`id`, `sets`) VALUES
	(1, 'Ancient'),
	(2, 'Barbarian'),
	(3, 'Breath of the Wild'),
	(4, 'Climbing'),
	(5, 'Desert Voe'),
	(6, 'Dark'),
	(7, 'Fierce Deity'),
	(8, 'Flamebreaker'),
	(9, 'Hero'),
	(10, 'Hylian'),
	(11, 'Ocarina of Time'),
	(12, 'Phantom'),
	(13, 'Phantom Ganon'),
	(14, 'Radiant'),
	(15, 'Royal Guard'),
	(16, 'Rubber'),
	(17, 'Skyward Sword'),
	(18, 'Snowquill'),
	(19, 'Soldier’s'),
	(20, 'Stealth'),
	(21, 'Tingle'),
	(22, 'Twilight Princess'),
	(23, 'Wind Waker'),
	(24, 'Xenoblade'),
	(25, 'Zora'),
	(26, 'Singles'),
	(27, 'Circlets'),
	(28, 'Divine Helms'),
	(29, 'Monster Masks');
/*!40000 ALTER TABLE `armor_sets` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
