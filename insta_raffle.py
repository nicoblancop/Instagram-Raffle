import pyautogui as gui
import time
import pyperclip as pc
import random


friends = ['leomessi', 'nicoblancop', 'messismo_', 'cristiano']

raffle = 'https://www.instagram.com/p/CVBnPYRjDnL/'

safari_icon_loc = (175,865)

# class siempre en mayuscula

class Sorteo(object):
    def __init__(self, link, gente, espera, freq, safari):
        self.link = link
        self.gente = gente
        self.espera = espera
        self.freq = freq
        self.safari = safari
    def abrirSafari(self):
        # Esta funcion abre safari
        gui.moveTo(self.safari)
        gui.click()
        time.sleep(5)
        gui.hotkey('command', 't')  
    def abrirInsta(self):
        # Esta funcion abre el sorteo de ig
        pc.copy(self.link)
        gui.moveTo(743,50, duration=1)
        gui.click()
        gui.hotkey('command', 'v')
        gui.hotkey('enter')
    def etiquetar(self):
        # Esta funcion etiqueta a friends como jime
        gui.moveTo(889,768, duration=1)
        gui.click()
        dobolu= random.choice(self.gente)
        pc.copy(dobolu)
        gui.hotkey('alt', '2')
        gui.hotkey('command', 'v')
        gui.moveTo(1105,767, duration=0.5)
        gui.click()
    def cerrarSafari(self):
        # La funcion cierra safari
        gui.hotkey('command', 'w')
    def esperar(self):
        # La funcion espera 15"
        time.sleep(self.espera)
    def intervalo(self):
        # espera el intervalo entre personas en minutos
        time.sleep(self.freq*60)


def handler():
    # Me maneja la ejecucion del sorteo

    veces = 100
    sorteo1 = Sorteo(raffle, friends, 15, 1, safari_icon_loc)

    counter1 = 0
    while counter1 != veces:
        sorteo1.abrirSafari()
        sorteo1.esperar()
        sorteo1.abrirInsta()
        sorteo1.esperar()
        sorteo1.etiquetar()
        sorteo1.esperar()
        sorteo1.etiquetar()
        sorteo1.esperar()
        sorteo1.etiquetar()
        sorteo1.cerrarSafari()     
        sorteo1.intervalo()

def main():
    handler()

main()