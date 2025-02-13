# Execute a command within an SQLlite database

import sqlite3
import os
import pathlib

def sql_connect(database):
    """Will try to connect to a given sqlite database"""
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None