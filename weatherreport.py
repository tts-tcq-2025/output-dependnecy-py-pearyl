

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def heavyRainStub():
    return {
        'temperatureInC': 30,
        'precipitation': 80,  # High precipitation
        'humidity': 90,
        'windSpeedKMPH': 10   # Low wind
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        else: 
            if readings['windSpeedKMPH'] > 50:
                weather = "Alert, Stormy with heavy rain"
            else:
                weather = "Rainy Day"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("storm" in weather.lower())


def testHighPrecipitation():
    weather = report(heavyRainStub)
    assert("rainy" in weather.lower()); # Will fail if bug exists


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
