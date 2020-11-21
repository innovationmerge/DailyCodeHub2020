CREATE TABLE `users` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(150) NULL COLLATE 'latin1_swedish_ci',
	`password` VARCHAR(150) NULL COLLATE 'latin1_swedish_ci',
	`fullname` VARCHAR(150) NULL COLLATE 'latin1_swedish_ci',
	PRIMARY KEY (`id`) USING BTREE,
	UNIQUE INDEX `username` (`username`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=223
;
