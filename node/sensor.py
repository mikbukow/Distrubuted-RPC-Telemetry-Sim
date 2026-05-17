import random
import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280


#TODO: check if sensor connected, if not use random numbers
# def read_sensor():
#     return {
#         "temperature_f": random.randint(40, 80),
#         "temperature_c": random.randint(0, 100),
#         "humidity": random.randint(0, 50),
#         "pressure": random.randint(5, 90)
#     }


# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

def convert_celsius(celsius):
    return (celsius * 9/5) + 32

def read_sensor():
    temperature_c = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure
    temperature_f = convert_celsius(temperature_c)

    return {
        "temperature_f": temperature_f,
        "temperature_c": temperature_c,
        "humidity": humidity,
        "pressure": pressure
    }


print(read_sensor)




