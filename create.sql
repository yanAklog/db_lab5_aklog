CREATE TABLE Genre
(
  genre_type VARCHAR(50) NOT NULL,
  PRIMARY KEY (genre_type)
);

CREATE TABLE Category
(
  category_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (category_name)
);

CREATE TABLE App
(
  app_name VARCHAR(250) NOT NULL,
  app_size INT,
  app_price NUMERIC(8, 2),
  app_content_rating VARCHAR(50) NOT NULL,
  category_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (app_name),
  FOREIGN KEY (category_name) REFERENCES Category(category_name)
);

CREATE TABLE App_Genre
(
  app_name VARCHAR(250) NOT NULL,
  genre_type VARCHAR(50) NOT NULL,
  PRIMARY KEY (app_name, genre_type),
  FOREIGN KEY (app_name) REFERENCES App(app_name),
  FOREIGN KEY (genre_type) REFERENCES Genre(genre_type)
);


