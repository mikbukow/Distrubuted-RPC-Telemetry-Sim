import random

def read_sensor():
    return {
        "temperature": random.randint(40, 80),
        "cpu_usage": random.randint(0, 100)
    }
