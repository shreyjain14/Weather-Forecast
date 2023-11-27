import requests

API_KEY = '<API KEY HERE>'


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
