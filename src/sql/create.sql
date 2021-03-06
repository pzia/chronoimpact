BEGIN TRANSACTION;
CREATE TABLE "groups" ( `id_group`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name`	TEXT, `date_start`	TEXT, `date_end`	TEXT );
CREATE TABLE `impacts` ( `id_impact`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `id_location`	INTEGER NOT NULL, `id_project`	INTEGER NOT NULL, `type`	TEXT DEFAULT "loss", `real`	INTEGER DEFAULT 0, `felt`	INTEGER DEFAULT 0 );
CREATE TABLE `locations` ( `id_location`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name`	INTEGER );
CREATE TABLE "projects" ( `id_project`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name`	TEXT, `id_group`	INTEGER NOT NULL, `date_impact`	TEXT );
DELETE FROM "sqlite_sequence";
COMMIT;
