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
    * Varier la luminosité de la led
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

# Affichage de le fréquence et du cycle pwm
print("Fréquence : ",led.freq())
print("Cycle : ",led.duty())

sleep_ms(5000)# Pause

while True:
    # Incrémentation de l'éclairage
    for x in range(0,101,5):
        x = map(x,0,100,0,1023)
        led.duty(x)
        print("Cycle : ",x)
        sleep_ms(500)
    sleep_ms(2000) # pause
    # Décrémentation de l'éclairage
    for x in range(100,-1,-5):
        x = map(x,100,0,1023,0)
        led.duty(x)
        print("Cycle : ",x)
        sleep_ms(500)
    sleep_ms(2000) # pause
