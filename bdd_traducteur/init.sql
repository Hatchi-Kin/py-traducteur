-- Adminer 4.8.1 MySQL dump

SET NAMES utf8mb4;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

CREATE TABLE IF NOT EXISTS `prompts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text_in` varchar(250) NOT NULL,
  `text_out` varchar(250) NOT NULL,
  `version` varchar(250) NOT NULL,
  `utilisateur` int NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `execute_time` float NOT NULL DEFAULT 1.0,
  PRIMARY KEY (`id`),
  KEY `utilisateur` (`utilisateur`),
  CONSTRAINT `prompts_ibfk_1` FOREIGN KEY (`utilisateur`) REFERENCES `utilisateurs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `prompts` (`id`, `text_in`, `text_out`, `version`, `utilisateur`, `date`, `execute_time`) VALUES
(1, 'Premièrement, tu ôteras la Goupille sacrée. Puis tu compteras jusqu\'à trois, pas plus, pas moins.', 'First, you\'ll remove the sacred Pin, then you\'ll count to three, no more, no less.', 'fr >> en', 1, '2024-07-13 18:12:02', 7.5),
(2, 'Chevaliers qui dites ni, nous ne sommes que de simples voyageurs qui recherchons un enchanteur qui vit au-delà de ces bois.', 'Knights who say ni, we are merely travelers who seek an enchanter who lives beyond these woods.', 'fr >> en', 1, '2024-07-14 18:12:02', 8.0),
(3, 'C\'est un fameux trois mâts, fin comme un oiseau !', 'It\'s a famous three-masted ship, thin as a bird!', 'fr >> en', 2, '2024-07-15 18:12:02', 8.5);

CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(250) NOT NULL,
  `mdp` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `utilisateurs` (`id`, `login`, `mdp`) VALUES
(1, 'Cleese', 'Sacré Graal!'),
(2, 'Gilliam', 'Flying Circus'),
(3, 'bender', 'rodriguez');

-- 2024-07-10 12:39:49