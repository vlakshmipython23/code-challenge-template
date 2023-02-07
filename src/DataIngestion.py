# Importing required packages
import sqlite3
import os
from pathlib import Path
import time


# function to import the weather data from data_dir to db_file
#   iterate through all the files in the data_dir folder and
#   read data in each file, split the data line by tabs separate
#   insert those data into the weather.db in weather_data table
def ingest_weather_data(db_file, data_dir):
    # open the sqlite connection object using the db_file
    conn = sqlite3.connect(db_file)
    # open the cursor object for query execution purpose
    c = conn.cursor()

    filecount = 0
    for filename in os.listdir(data_dir):
        # assuming file name as the station id
        station_id = filename.split(".")[0]
        filecount += 1

        # just for internal reference - can be deleted
        print(f"\nFile Number: {filecount} is {station_id}.txt")

        # open the file in the read mode for reach the data
        with open(os.path.join(data_dir, filename), "r") as f:
            # get all the lines in the list
            lines = f.readlines()

            # iterate through each line (row) in the lines list
            for line in lines:
                # split the data using TAB and store in the respective variables
                date, max_temp, min_temp, precipitation = line.strip().split("\t")

                # prepare the insert statement for inserting the data
                insert_data = "INSERT INTO weather_data "
                insert_data += "(Record_Date, Max_Temp, Min_Temp, Precipitation, "
                insert_data += "Station_ID) VALUES('" + date[0:4] + "-" + date[4:6]
                insert_data += "-" + date[-2:] + "',"
                insert_data += max_temp.strip() + "," + min_temp.strip() + ","
                insert_data += precipitation.strip() + ",'" + station_id + "');"
                # execute the above insert query
                c.execute(insert_data)

            # just an internal reference for number of records inserted
            #   in the table for  that file
            print(f"Number of records imported from [{filename}] is {len(lines)}")
    print("\nIngestion of weather data completed.")
    # commit the transactions done and close the connection
    conn.commit()
    conn.close()


def ingest_weather_stats(db_file):
    # creation connection and cursor objects
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # prepare the insert statement for aggregating the stats data
    #   from weather data table using aggregation for min_temp,
    #   max_temp, precipitation
    stats_data = "INSERT INTO weather_stats SELECT Station_ID, "
    stats_data += "strftime('%Y',Record_Date) , avg(Min_Temp), avg(Max_Temp), "
    # converting the precipitation from millimeter to centimeter
    stats_data += "sum(precipitation/10) from weather_data "
    stats_data += "where Min_Temp != -9999 and  Max_Temp != -9999 and Precipitation != -9999 "
    stats_data += "group by Station_ID, strftime('%Y',Record_Date);"

    # execute the above insert statement
    c.execute(stats_data)
    print("\nIngestion of weather stats completed.")

    # commit the transaction and close the connection object
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # initialize the project root path, database file path,
    #       import folder path
    root_dir_path = str(Path(__file__).parent.parent)
    db_file_path = root_dir_path + "\\database\\weather.db"
    data_import_path = root_dir_path + "\\wx_data"

    # initialize the start time
    start_time = time.time()
    # call the function to import the weather data from files available
    #       in data_import_path
    ingest_weather_data(db_file_path, data_import_path)
    # print the overall duration for importing all the data
    print(f"Total duration of importing the weather data is {time.time() - start_time} seconds.")

    # initialize the start time
    start_time = time.time()
    # call the function to generate the weather stats from weather data
    #       by passing the db_file_path for weather db
    ingest_weather_stats(db_file_path)
    # print the overall duration for generating the weather stats data
    print(f"Total duration of creating the weather stats is {time.time() - start_time} seconds.")
