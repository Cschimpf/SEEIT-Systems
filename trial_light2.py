import RPi.GPIO as GPIO
import time
import requests

def gpioSetup(sensor_index):
	for gpio in sensor_index:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpio, GPIO.IN)

def readSensor(sensor_index, server_address):
	while True:
		sensor_list = []
		for index in sensor_index:
			sensor= GPIO.input(index)
			sensor_list.append(sensor)
			print(sensor)

		req = requests.post(server_address, data={'sensor_status' : sensor_list}) #[sensor1, sensor2, sensor3]
                print("the status code is: ", req.status_code)
		time.sleep(2)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)

gpios = [17, 10]

url = "http://10.0.0.16:80"
gpioSetup(gpios)
readSensor(gpios, url)

#while True:
	#print(GPIO.input(17))
	#time.sleep(2)
