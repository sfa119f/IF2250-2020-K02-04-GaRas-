-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: rpl
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `kurir`
--

DROP TABLE IF EXISTS `kurir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kurir` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) DEFAULT NULL,
  `harga` int DEFAULT NULL,
  `alamat` varchar(300) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kurir`
--

LOCK TABLES `kurir` WRITE;
/*!40000 ALTER TABLE `kurir` DISABLE KEYS */;
INSERT INTO `kurir` VALUES (1,'jne',10000,'Jalan A No.5 Bandung','Foto/kurir/jne.png'),(2,'jnt',9500,'Jalan B No.4 Bandung','Foto/kurir/jnt.png'),(3,'tiki',11000,'Jalan C No.3 Bandung','Foto/kurir/tiki.png'),(4,'sicepat',12000,'Jalan D No.6 Bandung','Foto/kurir/sicepat.png');
/*!40000 ALTER TABLE `kurir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pengguna`
--

DROP TABLE IF EXISTS `pengguna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pengguna` (
  `nama` varchar(50) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `jenis_kelamin` char(1) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `nomor_gawai` varchar(12) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `peranan` varchar(10) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pengguna`
--

LOCK TABLES `pengguna` WRITE;
/*!40000 ALTER TABLE `pengguna` DISABLE KEYS */;
INSERT INTO `pengguna` VALUES ('Aang','1995-08-18','P','aang@gmail.com','081223757474','Jalan H No.4','pembeli','aang','pass','Foto/pengguna/aang.png'),('Katara','1994-05-20','W','katara@gmail.com','081212797914','Jalan H No.5','pembeli','katara','word','Foto/pengguna/katara.png'),('Sokka','1990-01-01','P','sokka@gmail.com','081123657377','Jalan Z No.2','pembeli','sokka','1234','Foto/pengguna/sokka.png'),('Toph','1991-11-29','P','toph@gmail.com','082223444474','Jalan G No.5','penjual','toph','password','Foto/pengguna/toph.png');
/*!40000 ALTER TABLE `pengguna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produk`
--

DROP TABLE IF EXISTS `produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produk` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) DEFAULT NULL,
  `harga` int DEFAULT NULL,
  `stok` int DEFAULT NULL,
  `berat` float DEFAULT NULL,
  `spek` varchar(300) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `kategori` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produk`
--

LOCK TABLES `produk` WRITE;
/*!40000 ALTER TABLE `produk` DISABLE KEYS */;
INSERT INTO `produk` VALUES (1,'tongkat lipat',30000,100,0.8,'tongkat untuk tuna netra dan bisa dilipat','Foto/produk/tongkat.png','tuna netra'),(2,'alquran braille',200000,30,0.5,'alquran braille untuk tuna netra','Foto/produk/alquran.png','tuna netra'),(3,'kacamata hitam',150000,50,0.2,'kacamata hitam untuk tuna netra','Foto/produk/kacamata.png','tuna netra'),(4,'alat tulis tunanetra',10000,150,0.3,'alat tulis tunanetra untuk tuna netra','Foto/produk/alat tulis.png','tuna netra'),(5,'alat bantu belajar tunanetra',50000,10,0.2,'media belajar matematika','Foto/produk/alat belajar.jpg','tuna netra'),(6,'alat bantu dengar',70000,25,0.1,'alat bantu pendengaran','Foto/produk/alat dengar.png','tuna rungu'),(7,'masker transparan',15000,80,0.05,'masker transparan untuk tuna rungu','Foto/produk/masker.jpg','tuna rungu'),(8,'buku bahasa isyarat',35000,250,0.5,'buku untuk belajar bahasa isyarat','Foto/produk/buku.jpg','tuna wicara'),(9,'translator',1000000,10,0.4,'alat penerjemah bahasa isyarat','Foto/produk/translator.jpg','tuna wicara'),(10,'kursi roda',350000,60,5,'kursi roda untuk tuna daksa','Foto/produk/kursi roda.png','tuna daksa'),(11,'kaki palsu',75000,70,2,'alat bantu jalan','Foto/produk/kaki palsu.png','tuna daksa'),(12,'orthotic',95000,45,0.4,'alat bantu untuk tuna daksa','Foto/produk/orthotic.png','tuna daksa'),(13,'splint',105000,35,0.4,'alat bantu untuk tuna daksa','Foto/produk/splint.png','tuna daksa'),(14,'alat peraga',105000,35,0.3,'alat peraga untuk tuna grahita','Foto/produk/alat peraga.jpg','tuna grahita');
/*!40000 ALTER TABLE `produk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-11 16:18:45
