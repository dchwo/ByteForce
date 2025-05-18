CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sex` enum('male','female','other') DEFAULT 'other',
  `birth_date` date DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` enum('active','inactive') DEFAULT 'active',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
);

INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `role`, `sex`, `birth_date`, `status`)
VALUES

-- Platform Manager
('John', 'Doe', 'pm1@cc.com', 'password', 'platformmanager', 'male', '1995-08-25', 'active'),
('Jane', 'Chan', 'pm2@cc.com', 'password', 'platformmanager', 'female', '1979-01-22', 'active'),

-- Admins
('Alice', 'Tan', 'admin1@cc.com', 'password', 'admin', 'female', '1980-05-12', 'active'),
('Bob', 'Lim',   'admin2@cc.com',   'password', 'admin', 'male', '1975-08-25', 'active'),

-- Cleaners
('Charlie', 'Ng', 'cleaner1@cc.com', 'password', 'cleaner', 'male', '1990-11-03', 'active'),
('Diana', 'Lee',  'cleaner2@cc.com',  'password', 'cleaner', 'female', '1988-04-17', 'inactive'),

-- Homeowners
('Ethan', 'Goh', 'ho1@cc.com', 'password', 'homeowner', 'male', '1992-09-22', 'active'),
('Fiona', 'Tan', 'ho2@cc.com', 'password', 'homeowner', 'female', '1985-01-30', 'active');

CREATE TABLE `service_listings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `service_name` varchar(255) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `description` text,
  `price` decimal(10,2) NOT NULL,
  `total_views` int DEFAULT '0',
  `shortlisted` int DEFAULT '0',
  `status` enum('active','inactive') DEFAULT 'active',
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ;

CREATE TABLE `shortlisted_listings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `listing_id` int NOT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `listing_id` (`listing_id`),
  CONSTRAINT `shortlisted_listings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `shortlisted_listings_ibfk_2` FOREIGN KEY (`listing_id`) REFERENCES `service_listings` (`id`)
);

-- Table for service history tracking
CREATE TABLE `service_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cleaner_id` int NOT NULL,
  `homeowner_id` int NOT NULL,
  `service_listing_id` int,
  `service_type` varchar(100) DEFAULT NULL,
  `service_date` date NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `status` enum('completed','cancelled','pending') DEFAULT 'completed',
  `notes` text,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `cleaner_id` (`cleaner_id`),
  KEY `homeowner_id` (`homeowner_id`),
  KEY `service_listing_id` (`service_listing_id`),
  CONSTRAINT `service_history_ibfk_1` FOREIGN KEY (`cleaner_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `service_history_ibfk_2` FOREIGN KEY (`homeowner_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `service_history_ibfk_3` FOREIGN KEY (`service_listing_id`) REFERENCES `service_listings` (`id`)
);

-- Table for service categories managed by platform manager
CREATE TABLE `service_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `min_price` decimal(10,2) DEFAULT NULL,
  `max_price` decimal(10,2) DEFAULT NULL,
  `status` enum('active','inactive') DEFAULT 'active',
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
);

-- Add a category_id field to service_listings table
ALTER TABLE `service_listings` ADD COLUMN `category_id` int DEFAULT NULL;
ALTER TABLE `service_listings` ADD CONSTRAINT `service_listings_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `service_categories` (`id`);

CREATE TABLE `user_profiles` (
    `id` int NOT NULL AUTO_INCREMENT,
    `user_id` int NOT NULL,
    `role` varchar(100) NOT NULL,
    `description` text,
    `status` enum('active','inactive') DEFAULT 'active',
    `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
    `update_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `user_id`(`user_id`),
    CONSTRAINT `user_profiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
);
