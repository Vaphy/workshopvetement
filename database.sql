create database workshop;
create table users (id int NOT NULL AUTO_INCREMENT, login varchar(255), password varchar(255), PRIMARY KEY(id));
create table dressing (id int NOT NULL, user_id int NOT NULL, PRIMARY KEY (id), FOREIGN KEY (user_id) REFERENCES users(id));
create table vetement (id int NOT NULL, dressing_id int NOT NULL, path_photo varchar(255), color varchar(255), type int, url_photo varchar(255), PRIMARY KEY (id), FOREIGN KEY (dressing_id) REFERENCES dressing(id));