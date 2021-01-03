import machine
import utime
import vl53l0x

# declare pins
SDA_PIN = const(4)
SCL_PIN = const(5)

# define software I2C bus (needed for ESP8266).
# alternatively hardware I2C bus (ESP32 only) can be used by passing 0 or 1 to
# constructor, i.e.: i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
# any input pins can be defined for the i2c interface
i2c = machine.I2C(-1, scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN), freq=100000)

# create snesor object
sensor = vl53l0x.VL53L0X(i2c)

sensor.start()

print("* VL43L0X Distance *")

while True:
    # read sensor value
    distance = sensor.read()

    # print readings to console
    # {} is used in conjunction with format() for substitution.
    # .1f       - format to 1 decimal places.
    print("Distance: {:.1f} mm".format(distance), end='\r')
    
    utime.sleep_ms(500)
