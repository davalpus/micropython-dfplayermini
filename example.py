from dfplayermini import Player
import machine

from time import sleep
import sys


music = Player(pin_TX=17, pin_RX=16)
led_onboard = machine.Pin(25, machine.Pin.OUT)
TactSw  = machine.Pin(16, machine.Pin.PULL_DOWN)
RelaySw  = machine.Pin(17, machine.Pin.OUT)


music.module_reset()
sleep(3)

music.volume(10)
led_onboard.value(1)
sleep(0.5)
led_onboard.value(0)
sleep(0.5)
led_onboard.value(1)
sleep(0.5)
led_onboard.value(0)
sleep(0.5)
led_onboard.value(1)
sleep(0.5)
led_onboard.value(0)
sleep(0.5)

print("START")
oldValue = TactSw.value()

while (True):
    if TactSw.value() != oldValue:
        if TactSw.value() == 1:
            led_onboard.value(1)
            music.play('next')
            RelaySw.value(1)
        else:
            led_onboard.value(0)
            music.stop()
            RelaySw.value(0)
        oldValue = TactSw.value()
        sleep(0.5)
    sleep(0.5)
sys.exit()