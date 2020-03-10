"""
Creates initial tables required by the app.
"""
from database import db


def create_search_history():
    """Create history table.

    :return: None
    """
    db.run_query('''CREATE TABLE IF NOT EXISTS songs
                 (ID SERIAL PRIMARY KEY,
                 source varchar(64),
                 url 
                 user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                 keyword  TEXT  NOT NULL,
                 updated_on TIMESTAMP NOT NULL default CURRENT_TIMESTAMP,
                 CONSTRAINT user_keyword_constraint UNIQUE(user_id, keyword)
                 );
        ''')


if __name__ == '__main__':
    create_song_table()
