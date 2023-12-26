import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.create_table_reference_users)

        try:
            self.connection.execute(sql_queries.add_column_table_telegram_users)
        except sqlite3.Error:
            pass

        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None)
        )
        self.connection.commit()

    def sql_insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER,
            (tg_id,)
        )
        self.connection.commit()

    def sql_delete_user(self, tg_id):
        self.cursor.execute(
            sql_queries.DELETE_BAN_USER,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_profile_user(self, tg_id, nickname, bio, age, height, weight, gender, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_USERS,
            (None, tg_id, nickname, bio, age, height, weight, gender, photo)
        )
        self.connection.commit()

    def sql_select_profile_user(self, tg_id):
        self.cursor.execute(
            sql_queries.SELECT_PROFILE_USER,
            (tg_id,)
        )
        user_data = self.cursor.fetchone()

        if user_data:
            return {
                "id": user_data[0],
                "telegram_id": user_data[1],
                "nickname": user_data[2],
                "biography": user_data[3],
                "age": user_data[4],
                "height": user_data[5],
                "weight": user_data[6],
                "gender": user_data[7],
                "photo": user_data[8]
            }
        else:
            return None

    def sql_select_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "height": row[5],
            "weight": row[6],
            "gender": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY,
            (tg_id, tg_id, tg_id,)
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_insert_dislike(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker,)
        )
        self.connection.commit()

    def get_referral_link(self, user_id):
        self.cursor.execute(sql_queries.select_reference_user,
                            (user_id,)
                            )
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_referral_list(self, user_id):
        self.cursor.execute(
            """
            SELECT owner_telegram_id
            FROM reference_users
            WHERE reference_telegram_id = ?
            """,
            (user_id,)
        )
        referred_users = self.cursor.fetchall()
        if referred_users:
            referred_users_ids = [user[0] for user in referred_users]
            query = f"""
            SELECT telegram_id, username
            FROM telegram_users
            WHERE telegram_id IN ({','.join('?' * len(referred_users_ids))})
            """
            self.cursor.execute(query, referred_users_ids)
            referred_users_data = self.cursor.fetchall()
            return referred_users_data
        else:
            return []
