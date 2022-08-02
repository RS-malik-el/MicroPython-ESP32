"""
    * e-mail : rachelsysteme@gmail.com
    * gitHub : https://github.com/RS-malik-el
    * Donation : paypal.me/RachelSysteme
    *
    * @AUTHEUR : RACHEL SYSTEME
    * DATE : 02/08/2022
    *
    * @Board : ESP32
"""
from machine import Pin
from time import sleep_ms

# ---Configuration du pin en mode sortie
led = Pin(22, mode=Pin.OUT)
# led = Pin(22, mode=Pin.OUT, value=1)
# led = Pin(22, mode=Pin.OUT, value=0)

# bouton = Pin(23, mode=Pin.IN)
# bouton = Pin(23, mode=Pin.IN, pull=Pin.PULL_DOWN)
bouton = Pin(23, mode=Pin.IN, pull=Pin.PULL_UP)

# --- Différentes manière de modifier l'état u'une broche
# Pin.on() et Pin.off()
# Pin.high() et Pin.low()
# Pin.value(valeur)
etat = False
while True:
    if not bouton.value():
        etat = not etat
        led.value(etat)
    sleep_ms(100)
