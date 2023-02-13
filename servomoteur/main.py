"""
    * e-mail : rachelsysteme@gmail.com
    * gitHub : https://github.com/RS-malik-el
    * Donation : paypal.me/RachelSysteme
    *
    * @AUTEUR : RACHEL SYSTEME / Openprogramming
    * DATE : 08/02/2023
    *
    * @Board : ESP32
    * Gestion des signaux pwm pour controler l'angle du servomoteur
"""
from machine import Pin,PWM
from time import sleep_ms

CYCLE_MIN = int((2.5*1023)//100) # 500us/20_000us  = 2.5%  (25)
CYCLE_MAX = int((12.5*1023)//100)  # 2500us/20_000us = 12.5% (127)
PAUSE = 2_000 # Temps de pense

# Fonction permettant d'effectuer des changements d'echelle comme sur l'arduino
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min)*(out_max - out_min)//(in_max - in_min)+out_min


# Fonction permettant de determiner la valeur du cycle pwm correspond a l'angle
def pwmForAngle(angle):
    try:
        assert angle >= 0 and angle <= 180
        return map(angle,0,180,CYCLE_MIN, CYCLE_MAX)
    except AssertionError:
        print("Angle invalide")
        return CYCLE_MIN


# ---Configuration du pin en mode sortie pwm
servo = PWM(Pin(23),freq=50, duty=CYCLE_MIN)

# Affichage de le frequence et du cycle pwm
print("Frequence : ",servo.freq())
print("Cycle : ",servo.duty())

sleep_ms(PAUSE)# Pause

while True:
    # Incrementation de l'angle
    for angle in range(0,181):
        signal = pwmForAngle(angle)
        servo.duty(signal)
        print("Cycle : ",signal)
        sleep_ms(20)

    sleep_ms(PAUSE) # pause

    # Decrementation de l'angle
    for angle in range(180,-1,-1):
        signal = pwmForAngle(angle)
        servo.duty(signal)
        print("Cycle : ",signal)
        sleep_ms(20)

    sleep_ms(PAUSE) # pause
