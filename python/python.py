# ----------------------------
# Hava Durumu Tahmin Uygulaması
# Creator=  Tuba
#  Kullanıcıdan şehir alır rastgele bir hava durumu verir
# ----------------------------


import random  

def get_weather_forecast(city_name):
    
    # Options
    weather_options = [
        "Güneşli ☀️",
        "Yağmurlu 🌧️",
        "Bulutlu ☁️",
        "Karlı ❄️",
        "Fırtınalı 🌩️",
        "Rüzgarlı 🌬️"
    ]
    
    #
    selected_weather = random.choice(weather_options)
    
 
    return f"{city_name} için hava durumu: {selected_weather}"

def main():
    
    print("🌍 Hava Durumu Tahmin Uygulamasına Hoşgeldiniz!")
    
    
    city = input("Lütfen bir şehir girin: ")
    
   
    forecast = get_weather_forecast(city)
    
    
    print(forecast)


if __name__ == "__main__":
    main()
