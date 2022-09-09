"""
   * e-mail : rachelsysteme@gmail.com
   * gitHub : https://github.com/RS-malik-el
   * Donation : paypal.me/RachelSysteme
   *
   * @AUTHEUR : RACHEL SYSTEME
   * DATE : 08/09/2022
   *
   * @Board : ESP32
   * Gestion de la led avec les signaux pwm
   * Varier la luminosité de la led grâce à un potentiomètre
"""
# GPIO : ADC2 (0, 2, 4, 12, 13, 14, 15, 25, 26 et 27)
# GPIO : ADC1 (32, 33, 34, 35, 36 et 39)
from machine import Pin
from machine import PWM
from machine import ADC
from time import sleep_ms

# --- Configuration du pin de la led en PWM
led = PWM(Pin(23))
led.freq(1000)
led.duty(500)

# --- Configuration du pin en entrée ADC
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)


while True:
   print(pot.read())
   led.duty(pot.read())
   sleep_ms(100)

# --- Plage de tension
# ADC.ATTN_0DB    : plage de 1,2 V
# ADC.ATTN_2_5DB  : plage de 1,5 V
# ADC.ATTN_6DB    : plage de 2,0 V
# ADC.ATTN_11DB   : plage de 3,3 V

# --- Resolution de la plage du signal
# ADC.WIDTH_9BIT  : plage 0 à 511
# ADC.WIDTH_10BIT : plage 0 à 1023
# ADC.WIDTH_11BIT : plage 0 à 2047
# ADC.WIDTH_12BIT : plage 0 à 4095
