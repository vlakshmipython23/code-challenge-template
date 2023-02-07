# Importing required packages
import sqlite3
import os
from pathlib import Path

# initialize project root directory, database directory
root_dir = str(Path(__file__).parent.parent)
db_folder_path = root_dir + "\\database"
db_file_path = root_dir + "\\database\\weather.db"


# create an empty weather.db in the database folder
def create_database():
    # if database folder does not existing then create the database folder
    if not os.path.isdir(db_folder_path):
        os.mkdir(db_folder_path)

    # create an empty weather.db file ( overwrite if exists)
    with open(db_file_path, 'w') as fp:
        pass
    print(f"Database weather.db created in [{db_folder_path}]")


# function to create the db schema
#       weather_data and weather_stats tables are
#       created in \database\weather.db
def create_db_schema():
    # connecting to Sqlite database file
    conn = sqlite3.connect(db_file_path, check_same_thread=False)

    # query to create the weather_data table
    weather_data_query = """CREATE TABLE weather_data (
      Station_ID char(11),
      Record_Date date,
      Min_Temp decimal(5,1),
      Max_Temp decimal(5,1),
      Precipitation decimal(5,1)
    );"""

    # query to create the weather_stats table
    weather_stats_query = """CREATE TABLE weather_stats (
        Station_ID char(11),
        Record_Year int,
        Avg_MinTemp decimal(5,1),
        Avg_MaxTemp decimal(5,1),
        Total_Precipitation decimal(10,1)
    );"""

    # execute the query using the sqlite connection for
    #       creating the tables - weather_data and weather_stats
    conn.execute(weather_data_query)
    print("weather data table created")
    conn.execute(weather_stats_query)
    print("weather stats table created")

    # commit and close the connection for the changes to be committed in the database
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Call the create_database function to create the weather.db file
    create_database()
    # Call the create_db_schema function
    #       to create the database schema for weather tables
    create_db_schema()

