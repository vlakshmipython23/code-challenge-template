import unittest
import requests


class TestWeatherAPI(unittest.TestCase):
    # Test weather_data endpoint with valid parameters
    def test_weather_data_valid_params(self):
        params = {'station_id': 'USC00110072', 'record_date': '1990-01-01', 'page': 1, 'per_page': 10}
        response = requests.get('http://localhost:5000/api/weather', params=params)
        self.assertEqual(response.status_code, 200)

    # Test weather_data endpoint with no proper parameter / data
    # Since we are not considering invalid parameters, it will still work but there won't be any data
    # hence asserting again empty data for invalid
    def test_weather_data_invalid_params(self):
        params = {'station_id': 'abc', 'record_date': '2021-01-01', 'page': 1, 'per_page': 10}
        response = requests.get('http://localhost:5000/api/weather', params=params)
        self.assertEqual(str(response.json()), "{'data': []}")

    # Test weather_stats endpoint with valid parameters
    def test_weather_stats_valid_params(self):
        params = {'station_id': 'USC00110072', 'record_year': '2010'}
        response = requests.get('http://localhost:5000/api/weather/stats', params=params)
        self.assertEqual(response.status_code, 200)

    # Test weather_stats endpoint with no proper parameter / data
    # Since we are not considering invalid parameters, it will still work but there won't be any data
    # hence asserting again empty data for invalid
    def test_weather_stats_invalid_params(self):
        params = {'station_id': 'abc', 'record_year': '2021'}
        response = requests.get('http://localhost:5000/api/weather/stats', params=params)
        self.assertEqual(str(response.json()), "{'data': []}")


if __name__ == "__main__":
    unittest.main()