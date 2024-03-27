-- Create the database
CREATE DATABASE IF NOT EXISTS task_tracker;

-- Use the database
USE task_tracker;

-- Create table Categories
CREATE TABLE IF NOT EXISTS Categories (
  CategoryID int(11) NOT NULL AUTO_INCREMENT,
  CategoryName varchar(255) NOT NULL,
  PRIMARY KEY (CategoryID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Insert data into table Categories
INSERT INTO Categories (CategoryID, CategoryName) VALUES
(1, 'Work'),
(2, 'Personal'),
(3, 'Shopping');

-- Create table TaskCategory
CREATE TABLE IF NOT EXISTS TaskCategory (
  TaskID int(11) NOT NULL DEFAULT '0',
  CategoryID int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (TaskID,CategoryID),
  KEY CategoryID (CategoryID),
  CONSTRAINT TaskCategory_ibfk_1 FOREIGN KEY (TaskID) REFERENCES Tasks (TaskID),
  CONSTRAINT TaskCategory_ibfk_2 FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Insert data into table TaskCategory
INSERT INTO TaskCategory (TaskID, CategoryID) VALUES
(1, 1),
(3, 2),
(2, 3);

-- Create table Tasks
CREATE TABLE IF NOT EXISTS Tasks (
  TaskID int(11) NOT NULL AUTO_INCREMENT,
  TaskTitle varchar(255) NOT NULL,
  TaskDescription text NOT NULL,
  Priority enum('low','medium','high') NOT NULL,
  Reminder datetime DEFAULT NULL,
  CategoryID int(11) DEFAULT NULL,
  PRIMARY KEY (TaskID),
  KEY CategoryID (CategoryID),
  CONSTRAINT Tasks_ibfk_1 FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Insert data into table Tasks
INSERT INTO Tasks (TaskID, TaskTitle, TaskDescription, Priority, Reminder, CategoryID) VALUES
(1, 'Complete Project Proposal', 'Finish writing the project proposal and submit it before the deadline.', 'high', '2024-03-28 15:00:00', 1),
(2, 'Buy groceries', 'Purchase fruits, vegetables, and dairy products from the supermarket.', 'medium', NULL, 3),
(3, 'Call Mom', 'Check in with Mom to see how she is doing and catch up on recent events.', 'low', NULL, 2);
