-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: 0.0.0.0    Database: football_eng
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bets`
--

DROP TABLE IF EXISTS `bets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bets` (
  `id` int NOT NULL,
  `B365H` float DEFAULT NULL,
  `B365D` float DEFAULT NULL,
  `B365A` float DEFAULT NULL,
  `BWH` float DEFAULT NULL,
  `BWD` float DEFAULT NULL,
  `BWA` float DEFAULT NULL,
  `GBH` float DEFAULT NULL,
  `GBD` float DEFAULT NULL,
  `GBA` float DEFAULT NULL,
  `IWH` float DEFAULT NULL,
  `IWD` float DEFAULT NULL,
  `IWA` float DEFAULT NULL,
  `LBH` float DEFAULT NULL,
  `LBD` float DEFAULT NULL,
  `LBA` float DEFAULT NULL,
  `SBH` float DEFAULT NULL,
  `SBD` float DEFAULT NULL,
  `SBA` float DEFAULT NULL,
  `WHH` float DEFAULT NULL,
  `WHD` float DEFAULT NULL,
  `WHA` float DEFAULT NULL,
  `SJH` float DEFAULT NULL,
  `SJD` float DEFAULT NULL,
  `SJA` float DEFAULT NULL,
  `VCH` float DEFAULT NULL,
  `VCD` float DEFAULT NULL,
  `VCA` float DEFAULT NULL,
  `Bb1X2` float DEFAULT NULL,
  `BbMxH` float DEFAULT NULL,
  `BbAvH` float DEFAULT NULL,
  `BbMxD` float DEFAULT NULL,
  `BbAvD` float DEFAULT NULL,
  `BbMxA` float DEFAULT NULL,
  `BbAvA` float DEFAULT NULL,
  `BbOU` float DEFAULT NULL,
  `BbMxG2_5` float DEFAULT NULL,
  `BbAvG2_5` float DEFAULT NULL,
  `BbMxS2_5` float DEFAULT NULL,
  `BbAvS2_5` float DEFAULT NULL,
  `BbAH` float DEFAULT NULL,
  `BbAHh` float DEFAULT NULL,
  `BbMxAHH` float DEFAULT NULL,
  `BbAvAHH` float DEFAULT NULL,
  `BbMxAHA` float DEFAULT NULL,
  `BbAvAHA` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clubs`
--

DROP TABLE IF EXISTS `clubs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clubs` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `id` int NOT NULL,
  `date` date DEFAULT NULL,
  `HomeTeam` int DEFAULT NULL,
  `AwayTeam` int DEFAULT NULL,
  `FullTimeHomeGoals` int DEFAULT NULL,
  `FullTimeAwayGoals` int DEFAULT NULL,
  `FullTimeResult` varchar(10) DEFAULT NULL,
  `HalfTimeHomeGoals` int DEFAULT NULL,
  `HalfTimeAwayGoals` int DEFAULT NULL,
  `HalfTimeResult` varchar(10) DEFAULT NULL,
  `Referee` int DEFAULT NULL,
  `HomeShots` int DEFAULT NULL,
  `AwayShots` int DEFAULT NULL,
  `HomeShotsTarget` int DEFAULT NULL,
  `AwayShotsTarget` int DEFAULT NULL,
  `HomeFouls` int DEFAULT NULL,
  `AwayFouls` int DEFAULT NULL,
  `HomeCorners` int DEFAULT NULL,
  `AwayCorners` int DEFAULT NULL,
  `HomeYellowCards` int DEFAULT NULL,
  `AwayYellowCards` int DEFAULT NULL,
  `HomeRedCards` int DEFAULT NULL,
  `AwayRedCards` int DEFAULT NULL,
  `Season` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `referee`
--

DROP TABLE IF EXISTS `referee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `referee` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-21 10:18:40
