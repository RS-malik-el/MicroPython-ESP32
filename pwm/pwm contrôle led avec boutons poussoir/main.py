"""
    * e-mail : rachelsysteme@gmail.com
    * gitHub : https://github.com/RS-malik-el
    * Donation : paypal.me/RachelSysteme
    *
    * @AUTHEUR : RACHEL SYSTEME
    * DATE : 26/08/2022
    *
    * @Board : ESP32
    * Gestion de la led avec les signaux pwm
    * Varier la luminosité de la led avec des boutons poussoir
"""
from machine import Pin,PWM
from time import sleep_ms

# Fonction permettant d'éffectuer des changements d'échelle comme sur l'arduino
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min)*(out_max - out_min)//(in_max - in_min)+out_min

# ---Configuration du pin en mode sortie pwm
led = PWM(Pin(21, mode=Pin.OUT))
led.freq(1000)
led.duty(1023)

# ---Configuration des pins comme entrée digital
boutonUp   = Pin(22, mode=Pin.IN, pull=Pin.PULL_UP)
boutonDown = Pin(23, mode=Pin.IN, pull=Pin.PULL_UP)

# ---Intensité de la lumière de 0 à 100
intensite = 100

while True:
    if not boutonUp.value():
        if intensite < 100:
            intensite += 5
            val = map(intensite,0,100,0,1023)
            led.duty(val)
            print("Intensité de la ded = ",intensite,"%")
            print("Cycle = ",val)

    if not boutonDown.value():
        if intensite > 0:
            intensite -= 5
            val = map(intensite,0,100,0,1023)
            led.duty(val)
            print("intensité de la ded = ",intensite,"%")
            print("Cycle = ",val)

    sleep_ms(100) # pause
