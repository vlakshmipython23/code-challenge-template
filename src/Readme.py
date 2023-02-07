'''

*** This is just a readme file for ***
*** understanding and executing the program ***

Order of execution:
-------------------
1. Run CreateWeatherDB.py
    a. create the database folder in the project root directory if it does not exist
    b. Creates an empty 'weather.db' in 'database' folder (overtwrites if exist)
    a. Creates the table definition of weather_data table
    b. Creates the table definition of weather_stats table
2. Run DataIngestion.py
    a. Helps in reading the txt file in the ws_data folder and
        import them into weather_data table
    b. Helps in inserting the stats data in weather_stats table
        that does not have invalid data -9999 in MinTemp and MaxTemp and Precipitation
3. Run weather_api.py (core weather api open the api in browser with parameters)
    a. This is the core api with two routes 1) api/weather 2) api/weather_stats
    b. In the root of the api, I have provided some links for easy navigation
        or quick testing (kindly ignore - it is just a helper)
    c. api/weather is the api end point for providing the weather data as a while
        or based on the station id and/or record date
        also pagination is considered and if not pass as parameters, default
        values are considered
    d. api/weather_stats is the api end point for providing the weather data as a while
        or based on the station id and/or record year
4.  Run unittest_weather
    This has 4 test methods to check valida and invalid parameters for
        weather data and weather stats endpoints
    This could be expanded with more unit tests as well

Other Assumptions:
    1. Assume project folder is the root folder
    2. An empty weather.db will be created in 'database' folder
    3. Folder 'ws_data' has all the txt files for data import
    4. Assuming flask and sqlite packages are installed for the above code to work

'''