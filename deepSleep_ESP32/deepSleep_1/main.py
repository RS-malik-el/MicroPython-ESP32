"""
   * e-mail : rachelsysteme@gmail.com
   * gitHub : https://github.com/RS-malik-el
   * Donation : paypal.me/RachelSysteme
   *
   * @AUTHEUR : RACHEL SYSTEME
   * DATE : 14/09/2022
   *
   * @Board : ESP32
   * Gestion deepsleep interne
"""

from machine import Pin, deepsleep
from time import sleep_ms

led = Pin(22, mode=Pin.OUT)
led.value(1)
sleep_ms(5000) # Attente
deepsleep(5000)
