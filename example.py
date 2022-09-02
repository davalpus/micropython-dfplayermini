from dfplayermini import Player

from time import sleep
import sys


music = Player(pin_TX=17, pin_RX=16)

sleep(1)
music.volume(10)
sleep(1)
music.play('next')
sleep(10)

music.play('next')
sleep(30)

sys.exit()