import machine
import utime
 
analog_value1 = machine.ADC(26)
analog_value2 = machine.ADC(27)
analog_value3 = machine.ADC(28)

while True:
    reading1 = analog_value1.read_u16()
    reading2 = analog_value2.read_u16()
    reading3 = analog_value3.read_u16()
    total = (reading1+reading2+reading3)
    if total < 185000:
        print("Baaang!")
        print("ADC: ",total )
    utime.sleep(0.2)