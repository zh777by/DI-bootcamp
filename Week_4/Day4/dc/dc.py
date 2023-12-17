import sqlite3
import random
from restcountries import RestCountryApiV2 as rc

def create_connection():
    conn = sqlite3.connect('countries.db')
    return conn

def create_countries_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            name TEXT PRIMARY KEY,
            capital TEXT,
            population INTEGER,
            area REAL,
            region TEXT,
            subregion TEXT
        )
    ''')
    conn.commit()

def insert_country(conn, country):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO countries (name, capital, population, area, region, subregion)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (country.name, country.capital, country.population, country.area, country.region, country.subregion))
    conn.commit()

def write_random_countries_to_database(conn, num_countries=10):
    all_countries = rc.get_all()
    random_countries = random.sample(all_countries, min(num_countries, len(all_countries)))

    for country in random_countries:
        insert_country(conn, country)

def main():
    conn = create_connection()
    create_countries_table(conn)
    write_random_countries_to_database(conn, num_countries=10)
    conn.close()

if __name__ == "__main__":
    main()

