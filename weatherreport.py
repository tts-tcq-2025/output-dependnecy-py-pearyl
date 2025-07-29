

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
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
    assert("rain" in weather.lower())


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(sensorStub)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert("rainy" in weather.lower()); # Will fail if bug exists


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
