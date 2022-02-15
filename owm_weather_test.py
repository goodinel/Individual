from pyowm.owm import OWM

owm = OWM('f1512ea0fb921b85060f18b9fe339000')
weather_manager = owm.weather_manager()
observation = weather_manager.weather_at_place('London, GB')
# weather = owm.weather_at_place('Woodinville, WA')
weather = observation.weather
# print(weather.temperature)
print(weather.status)
# city_id_registry = owm.city_id_registry()

# w = weather.get_weather()
# print(w.get_temperature())
