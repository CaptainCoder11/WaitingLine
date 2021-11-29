CREATE TABLE [IF NOT EXISTS] `user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password_hash` VARCHAR(72) NOT NULL,
  `profile_picture` BLOB,
  `role` ENUM('OWNER','EMPLOYEE','REGULAR') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `id_UNIQUE` (`id`)
);


CREATE TABLE [IF NOT EXISTS] ``('')