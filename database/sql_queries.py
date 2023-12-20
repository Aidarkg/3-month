CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

CREATE_PROFILE_TABLE = """
create table if not exists profile_users
(
id integer primary key,
telegram_id integer,
nickname char(50),
biography text,
age integer,
height integer,
weight integer,
gender char(50),
photo text,
unique (telegram_id)
)
"""


INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""

INSERT_PROFILE_USERS = """
insert or ignore into profile_users values (?,?,?,?,?,?,?,?,?)
"""


CREATE_BAN_USER_TABLE = """
create table if not exists ban_users
(
id integer primary key,
telegram_id integer,
ban_count integer,
unique (telegram_id)
)
"""

INSERT_BAN_USER = """
insert into ban_users values (?,?,?)
"""

SELECT_BAN_USER = """
select * from ban_users where telegram_id = ?
"""

SELECT_PROFILE_USER = """
select * from profile_users where telegram_id = ?
"""

UPDATE_BAN_USER = """
update ban_users set ban_count = ban_count + 1 where telegram_id = ?
"""

DELETE_BAN_USER = """
delete from ban_users where telegram_id = ?
"""