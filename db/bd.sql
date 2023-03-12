-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: 34.170.25.61    Database: dns_test
-- ------------------------------------------------------
-- Server version	8.0.26-google

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '0410f3f7-a88a-11ed-b3b6-42010a800018:1-539843';

--
-- Table structure for table `DNS`
--

DROP TABLE IF EXISTS `DNS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DNS` (
  `id_dns` int NOT NULL AUTO_INCREMENT,
  `id_dominio` int NOT NULL,
  `id_tipo` int NOT NULL,
  `nombre_dns` varchar(255) NOT NULL,
  PRIMARY KEY (`id_dns`),
  KEY `id_dominio` (`id_dominio`),
  KEY `id_tipo` (`id_tipo`),
  CONSTRAINT `DNS_ibfk_1` FOREIGN KEY (`id_dominio`) REFERENCES `dominios` (`id_dominio`),
  CONSTRAINT `DNS_ibfk_2` FOREIGN KEY (`id_tipo`) REFERENCES `tipos_dns` (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DNS`
--

LOCK TABLES `DNS` WRITE;
/*!40000 ALTER TABLE `DNS` DISABLE KEYS */;
INSERT INTO `DNS` VALUES (94,115,1,'10 smtp.google.com.'),(95,115,2,'172.217.173.206'),(96,115,3,'2800:3f0:4005:407::200e'),(97,115,4,'ns1.google.com.'),(98,115,5,'ns1.google.com. dns-admin.google.com. 515861724 900 900 1800 60'),(99,115,6,'\"v=spf1 include:_spf.google.com ~all\"'),(100,116,1,'10 smtpin.vvv.facebook.com.'),(101,116,2,'157.240.6.35'),(102,116,3,'2a03:2880:f12b:83:face:b00c:0:25de'),(103,116,4,'b.ns.facebook.com.'),(104,116,5,'a.ns.facebook.com. dns.facebook.com. 2695064953 14400 1800 604800 300'),(105,116,6,'\"ghfksmtc0x74q6g76g8nnw3psmx8zkwp\"');
/*!40000 ALTER TABLE `DNS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dominios`
--

DROP TABLE IF EXISTS `dominios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dominios` (
  `id_dominio` int NOT NULL AUTO_INCREMENT,
  `nombre_dominio` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_dominio`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dominios`
--

LOCK TABLES `dominios` WRITE;
/*!40000 ALTER TABLE `dominios` DISABLE KEYS */;
INSERT INTO `dominios` VALUES (115,'google.com',1),(116,'facebook.com',1);
/*!40000 ALTER TABLE `dominios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_logs`
--

DROP TABLE IF EXISTS `system_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_logs` (
  `id_log` int NOT NULL AUTO_INCREMENT,
  `id_dns` int NOT NULL,
  `description` varchar(1000) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id_log`),
  KEY `id_dns` (`id_dns`),
  CONSTRAINT `system_logs_ibfk_1` FOREIGN KEY (`id_dns`) REFERENCES `DNS` (`id_dns`)
) ENGINE=InnoDB AUTO_INCREMENT=212 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_logs`
--

LOCK TABLES `system_logs` WRITE;
/*!40000 ALTER TABLE `system_logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_dns`
--

DROP TABLE IF EXISTS `tipos_dns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_dns` (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_dns`
--

LOCK TABLES `tipos_dns` WRITE;
/*!40000 ALTER TABLE `tipos_dns` DISABLE KEYS */;
INSERT INTO `tipos_dns` VALUES (1,'MX',1),(2,'A',1),(3,'AAAA',1),(4,'NS',1),(5,'SOA',1),(6,'TXT',1);
/*!40000 ALTER TABLE `tipos_dns` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-12 15:35:04
