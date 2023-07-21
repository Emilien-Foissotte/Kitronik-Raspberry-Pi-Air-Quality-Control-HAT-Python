import time

from KitronikAirQualityControlHAT import KitronikBME688, KitronikOLED, KitronikZIPLEDs, KitronikBuzzer

# Initialise the BME688 sensor
bme688 = KitronikBME688()
# Initialise the OLED display
oled = KitronikOLED()
# Calculate the baseline values for the BME688 sensor
bme688.calcBaselines(oled) # Takes OLED as input to show progress

while True:
    # Update the sensor values
    bme688.measureData()
    oled.clear()
    # Read and output the sensor values to the OLED display
    oled.displayText("Temperature:" + str(bme688.readTemperature()), 1)
    oled.displayText("Pressure:" + str(bme688.readPressure()), 2)
    oled.displayText("Humidity:"+  str(bme688.readHumidity()), 3)
    oled.show()
    time.sleep(5)
    bme688.measureData()
    oled.clear()
    oled.displayText("eCO2:" + str(bme688.readeCO2()), 4)
    oled.displayText("Air Quality %:" + str(bme688.getAirQualityPercent()), 5)
    oled.displayText("Air Quality Score:" + str(bme688.getAirQualityScore()), 6)
    oled.show()

