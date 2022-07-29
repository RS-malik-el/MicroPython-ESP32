"""
    * e-mail : rachelsysteme@gmail.com
    * gitHub : https://github.com/RS-malik-el
    * Donation : paypal.me/RachelSysteme
    *
    * @AUTHEUR : RACHEL SYSTEME
    * DATE : 28/07/2022
    *
    * @Board : ESP32
"""
from machine import Pin
from time import sleep_ms

# Définition du pin comme une sortie
pin_led = Pin(2, mode=Pin.OUT)

while True:
    pin_led.on()  # Allume de la led
    sleep_ms(500) # Pause
    pin_led.off() # Extincion de la led
    sleep_ms(500) # Pause

# Différentes manières de mettre un programme en pause
# time.sleep(temps en seconde)
# time.sleep_ms(temps en millis seconde)
# time.sleep_us(temps en micro seconde)
