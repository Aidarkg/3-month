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

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
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

UPDATE_BAN_USER = """
update ban_users set ban_count = ban_count + 1 where telegram_id = ?
"""