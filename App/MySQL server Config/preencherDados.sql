-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema iot_server
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema iot_server
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `iot_server` DEFAULT CHARACTER SET utf8 ;
USE `iot_server` ;

-- -----------------------------------------------------
-- Table `iot_server`.`MensurementUnit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iot_server`.`MensurementUnit` (
  `UnitID` INT NOT NULL AUTO_INCREMENT,
  `symbol` VARCHAR(45) NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`UnitID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iot_server`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iot_server`.`user` (
  `userID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iot_server`.`SensorDevice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iot_server`.`SensorDevice` (
  `SensorDeviceID` INT NOT NULL AUTO_INCREMENT,
  `Akey` VARCHAR(45) NOT NULL,
  `label` VARCHAR(45) NOT NULL,
  `user_userID` INT NOT NULL,
  `description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`SensorDeviceID`, `user_userID`),
  INDEX `fk_SensorDevice_user1_idx` (`user_userID` ASC) VISIBLE,
  CONSTRAINT `fk_SensorDevice_user1`
    FOREIGN KEY (`user_userID`)
    REFERENCES `iot_server`.`user` (`userID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iot_server`.`DeviceStream`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iot_server`.`DeviceStream` (
  `DataStreamID` INT NOT NULL AUTO_INCREMENT,
  `SensorDeviceID` INT NOT NULL,
  `Akey` VARCHAR(45) NOT NULL,
  `label` VARCHAR(45) NOT NULL,
  `MensurementUnitID` INT NOT NULL,
  `anabled` TINYINT(1) ZEROFILL NOT NULL,
  `mensurementCount` INT NOT NULL,
  PRIMARY KEY (`DataStreamID`, `SensorDeviceID`, `MensurementUnitID`),
  INDEX `fk_DataStream_SensorDevice1_idx` (`SensorDeviceID` ASC) VISIBLE,
  INDEX `fk_DataStream_MensurementUnit1_idx` (`MensurementUnitID` ASC) VISIBLE,
  CONSTRAINT `fk_DataStream_SensorDevice1`
    FOREIGN KEY (`SensorDeviceID`)
    REFERENCES `iot_server`.`SensorDevice` (`SensorDeviceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DataStream_MensurementUnit1`
    FOREIGN KEY (`MensurementUnitID`)
    REFERENCES `iot_server`.`MensurementUnit` (`UnitID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iot_server`.`StreamData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iot_server`.`StreamData` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `DataStreamID` INT NOT NULL,
  `TimeStamp` DATETIME NOT NULL,
  `MensurementUnitID` INT NOT NULL,
  `value` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ID`, `DataStreamID`, `MensurementUnitID`),
  INDEX `fk_SensorData_MensurementUnit1_idx` (`MensurementUnitID` ASC) VISIBLE,
  INDEX `fk_SensorData_DataStream1_idx` (`DataStreamID` ASC) VISIBLE,
  CONSTRAINT `fk_SensorData_MensurementUnit1`
    FOREIGN KEY (`MensurementUnitID`)
    REFERENCES `iot_server`.`MensurementUnit` (`UnitID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SensorData_DataStream1`
    FOREIGN KEY (`DataStreamID`)
    REFERENCES `iot_server`.`DeviceStream` (`DataStreamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
-- --------------------------------- --
-- Adcionando informaçõe nas tableas --
-- --------------------------------- --
INSERT INTO user(name, email) VALUES
    ('Yiaver', 'yiaverS@gmail.com'),
    ('Gabriel', 'gabriel770@gmail.com'),
    ('Dacio', 'dacio123@gmail.com'),
    ('Isaac', 'isaac188@gmail.com'),
    ('Luiz', 'luizmatadordeporco@gmail.com'),
    ('jorge', 'giorgimDoPneu@gmail.com'),
    ('Beatriz', 'beatrizz@gmail.com'),
    ('Maria', 'maria@gmail.com'),
    ('João', 'joao@gmail.com'),
    ('Pedro', 'pedro@gmail.com');
    
INSERT INTO mensurementunit(symbol,description) VALUES ('ºC','Celsius'), ('mg/m³','Megagram per cubic metre'),('hPa','hectopasca'), ('%','Percent'), ('lux','Lux');