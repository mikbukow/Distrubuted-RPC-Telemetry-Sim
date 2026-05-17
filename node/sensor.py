import random

def read_sensor():
    return {
        "temperature_f": random.randint(40, 80),
        "temperature_c": random.randint(0, 100),
        "humidity": random.randint(0, 50),
        "pressure": random.randint(5, 90)
    }
