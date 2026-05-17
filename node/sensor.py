import random
import time
import smbus2
import bme280

#TODO: check if sensor connected, if not use random numbers
# def read_sensor():
#     return {
#         "temperature_f": random.randint(40, 80),
#         "temperature_c": random.randint(0, 100),
#         "humidity": random.randint(0, 50),
#         "pressure": random.randint(5, 90)
#     }

# BME280 sensor address 
address = 0x77

# Create I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)


def convert_celsius(celsius):
    return (celsius * 9/5) + 32

def read_sensor():
    data = bme280.sample(bus, address, calibration_params)
    temperature_c = data.temperature
    humidity = data.humidity
    pressure = data.pressure
    temperature_f = convert_celsius(temperature_c)

    return {
        "temperature_f": temperature_f,
        "temperature_c": temperature_c,
        "humidity": humidity,
        "pressure": pressure
    }
