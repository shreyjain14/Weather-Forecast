import requests

API_KEY = 'c364ea781b44f2d75e4bf5de54414fab'


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    days = 8 * forecast_days
    filtered_data = filtered_data[: days]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place="Delhi", forecast_days=1))
