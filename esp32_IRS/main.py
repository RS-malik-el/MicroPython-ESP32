"""
   * e-mail : rachelsysteme@gmail.com
   * gitHub : https://github.com/RS-malik-el
   * Donation : paypal.me/RachelSysteme
   *
   * @AUTHEUR : RACHEL SYSTEME
   * DATE : 14/09/2022
   *
   * @Board : ESP32
   * Gestion d'intérruption sur l'ESP32
   *
   * L'intérruption peut être utilisé sur tous les pins sauf les pins 6 et 11
"""

from machine import Pin

state = False

# Fonction à exécuter en cas d'intérruption
def gestion_interruption(gpio):
    global state
    state = not state
    led.value(state)
    print("intérruption détecter:", gpio)

led = Pin(22, mode=Pin.OUT)
btn = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)

# création de l'intérruption
btn.irq(trigger=Pin.IRQ_FALLING, handler=gestion_interruption)


# trigger : il définit le mode de déclenchement.
# Il y a 3 conditions différentes :
# ... Pin.IRQ_FALLING: pour déclencher l’interruption chaque fois
#                      que la broche passe de HAUT à BAS;
# ... Pin.IRQ_RISING: pour déclencher l’interruption chaque fois
#                     que la broche passe de LOW à HIGH.
# ... 3: pour déclencher l’interruption dans les deux sens
#        (c’est-à-dire lorsqu’un changement est détecté)
# handler : il s’agit d’une fonction qui sera appelée lorsqu’une interruption
# est détectée, dans ce cas : gestion_interruption().
