import machine
import utime
import vl53l0x

# declare pins
SDA_PIN = const(4)
SCL_PIN = const(5)

# setup sensor
i2c = machine.I2C(-1, scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN), freq=100000)
sensor = vl53l0x.VL53L0X(i2c)

sensor.start()

while True:
    distance = sensor.read()
    print("Distance: {:.1f} mm".format(distance), end='\r')
    utime.sleep_ms(500)
