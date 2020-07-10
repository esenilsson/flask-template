create table bearfood.users (id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), email varchar(50));


create table bearfood.ingredients (id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), kcal int);


create table bearfood.meals (id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), ingredient_id int, gram int);


create table bearfood.tour_meals (id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), meal_id int, meal_day_no int, meal_no int, tour_id int);


create table bearfood.tour (id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), user_id int);




# connect
mariadb --host 192.168.4.23 -P 33306 --user root -p;

# Insert
r = requests.post('http://127.0.0.1:5000/api/add_user/', json={"email": "katy.ho@outlook.com", "name": "Katy"})


r = requests.post('http://127.0.0.1:5000/api/add_user/', json={"name": "YY", "kcal": 20})



# add ingredients
insert into ingredients (name, kcal) values ('Snabb nudlar',359);
insert into ingredients (name, kcal) values ('kikärtor',360);
insert into ingredients (name, kcal) values ('Quinoa',360);
insert into ingredients (name, kcal) values ('Havre',370);
insert into ingredients (name, kcal) values ('Quinoa',380);
insert into ingredients (name, kcal) values ('Hårdost',398);
insert into ingredients (name, kcal) values ('sojabönor',400);
insert into ingredients (name, kcal) values ('Ölkorv',450);
insert into ingredients (name, kcal) values ('Golden curry',462);
insert into ingredients (name, kcal) values ('Edamame bönor',544);
insert into ingredients (name, kcal) values ('mandel',550);
insert into ingredients (name, kcal) values ('Choklad',566);
insert into ingredients (name, kcal) values ('mörk choklad',566);
insert into ingredients (name, kcal) values ('Kakaonibs',572);
insert into ingredients (name, kcal) values ('Rostad lök',580);
insert into ingredients (name, kcal) values ('Cashew',580);
insert into ingredients (name, kcal) values ('Jordnötter',620);
insert into ingredients (name, kcal) values ('Jordnötter',620);
insert into ingredients (name, kcal) values ('Kokos',621);
insert into ingredients (name, kcal) values ('solrosfrön',638);
insert into ingredients (name, kcal) values ('Valnötter',654);
insert into ingredients (name, kcal) values ('Olivolja',884);


inser into ingrients (name, kcal) values (XX, YY);