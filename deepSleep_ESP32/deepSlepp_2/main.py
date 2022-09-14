"""
   * e-mail : rachelsysteme@gmail.com
   * gitHub : https://github.com/RS-malik-el
   * Donation : paypal.me/RachelSysteme
   *
   * @AUTHEUR : RACHEL SYSTEME
   * DATE : 14/09/2022
   *
   * @Board : ESP32
   * Gestion deepsleep externe
"""
from esp32 import wake_on_ext0, WAKEUP_ALL_LOW
from machine import Pin, deepsleep
from time import sleep_ms

led = Pin(22, mode=Pin.OUT)
btn = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)

wake_on_ext0(pin=btn, level=WAKEUP_ALL_LOW)

led.value(1)
sleep_ms(5000) # Attente
deepsleep()
