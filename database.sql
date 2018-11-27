create database workshop;
create table users (id int AUTO_INCREMENT, login varchar(255), password varchar(255), PRIMARY KEY(id));
create table dressing (id int AUTO_INCREMENT, user_id int NOT NULL, PRIMARY KEY (id), FOREIGN KEY (user_id) REFERENCES users(id));
create table vetement (id int AUTO_INCREMENT, dressing_id int NOT NULL, nom_vetement varchar(255), path_photo varchar(255), color varchar(255), type int, url_photo varchar(255), PRIMARY KEY (id), FOREIGN KEY (dressing_id) REFERENCES dressing(id));


insert into users (login, password) values ('yoann.abherve@gmail.com', 'CDB30A1AAA630DF7D20D799C142CE7F8130E68058341C0E118EB786029F37D7D');
insert into users (login, password) values ('coucou@yahoo.com', '110812F67FA1E1F0117F6F3D70241C1A42A7B07711A93C2477CC516D9042F9DB');
insert into dressing (user_id) values ('1');
insert into dressing (user_id) values ('2');
insert into vetement (dressing_id, nom_vetement, color, type) values ('1', 'pull bleu', '#0000FF', '0');
insert into vetement (dressing_id, nom_vetement, color, type) values ('2', 'pantalon rouge', '#FF0000', '1');
insert into vetement (dressing_id, nom_vetement, color, type) values ('2', 'chaussure jaune', '#FFFF00', '2');



-- select * from users;


-- drop table vetement;
-- drop table dressing;
-- drop table users;


