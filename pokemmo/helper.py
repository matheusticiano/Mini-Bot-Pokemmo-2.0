from time import sleep

import pyautogui
from actions import atack, curar, teleport, voltar_spot_payday, kanto_to_unova, hoen_to_unova, sinnoh_to_unova, abrir_mapa

# Define algumas constantes que serão usadas ao longo do programa
X_SETA = 1363  # Cordenadas da seta
Y_SETA = 196  # Cordenadas da seta
REGIAO_SETA = (1341, 176, 43, 40)   # Região que a seta da mensagem aparece
REGIAO_MAPA_KANTO = (676, 298, 569, 467)   # Região mapa de kanto
REGIAO_MAPA_SINNOH = (579, 251, 753, 535)  # Região mapa de sinnoh
REGIAO_MAPA_HOEN = (576, 281, 768, 512)  # Região mapa de hoen
REGIAO_MAPA_UNOVA = (575, 277, 759, 536)  # Região mapa de unova
X_SPOT_PAYDAY = 801  # Cordenadas do spot
Y_SPOT_PAYDAY = 451  # Cordenadas do spot
X_HOEN = 803  # Cordenadas do porto de hoen
Y_HOEN = 628  # Cordenadas do porto de hoen
X_KANTO = 1044  # Cordenadas do porto de kanto
Y_KANTO = 626  # Cordenadas do porto de kanto
X_SINNOH = 1042  # Cordenadas do porto de sinnoh
Y_SINNOH = 750  # Cordenadas do porto de sinnoh
# Numeros de pps do ataque do seu pokemon (começa em 1 para caso curar seu pokemon em casos que não esteja completo)
contador = 1
# Um contador para fazer com que a função checa_mapa_e_define_spot ocorra apenas um vez
contador_setar_spot = 1
X_SPOT_EXP = 1144
Y_SPOT_EXP = 444


def set_spot_payday():  # Função que simula a ação de salvar o teleport e ir para spot do local
    sleep(0.5)
    pyautogui.moveTo(X_SPOT_PAYDAY, Y_SPOT_PAYDAY)
    sleep(0.2)
    pyautogui.click(X_SPOT_PAYDAY, Y_SPOT_PAYDAY)
    sleep(0.5)
    pyautogui.click(X_SPOT_PAYDAY, Y_SPOT_PAYDAY)
    sleep(5)
    pyautogui.keyDown('w')
    sleep(4)
    pyautogui.keyUp('w')
    sleep(0.2)
    curar()
    voltar_spot_payday()


# Função que simula a ação de conferir em qual região o player está e leva-lo para o spot da farm
def checa_mapa_e_define_spot_payday():
    global contador_setar_spot
    if contador_setar_spot == 1:
        pyautogui.press('2')
        sleep(1)
        while True:
            sinnoh_loc = pyautogui.locateOnScreen(
                'pokemmo/files/sinnoh_map.PNG', region=REGIAO_MAPA_SINNOH, confidence=0.6)
            kanto_loc = pyautogui.locateOnScreen(
                'pokemmo/files/kanto_map.PNG', region=REGIAO_MAPA_KANTO, confidence=0.6)
            hoen_loc = pyautogui.locateOnScreen(
                'pokemmo/files/hoen_map.PNG', region=REGIAO_MAPA_HOEN, confidence=0.6)
            unova_loc = pyautogui.locateOnScreen(
                'pokemmo/files/unova_map.PNG', region=REGIAO_MAPA_UNOVA, confidence=0.6)

            if kanto_loc is not None:
                sleep(0.2)
                pyautogui.click(X_KANTO, Y_KANTO)
                sleep(6)
                kanto_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_payday()
                contador_setar_spot -= 1
                break
            elif hoen_loc is not None:
                sleep(0.2)
                pyautogui.click(X_HOEN, Y_HOEN)
                sleep(5)
                hoen_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_payday()
                contador_setar_spot -= 1
                break
            elif unova_loc is not None:
                sleep(0.2)
                set_spot_payday()
                contador_setar_spot -= 1
                break
            elif sinnoh_loc is not None:
                sleep(0.2)
                pyautogui.click(X_SINNOH, Y_SINNOH)
                sleep(5)
                sinnoh_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_payday()
                contador_setar_spot -= 1
                break
            else:
                break


def voltar_spot_exp():
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(2.5)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.press('1')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(3)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(0.05)
    pyautogui.keyUp('w')
    sleep(0.2)


def set_spot_exp():  # Função que simula a ação de salvar o teleport e ir para spot do local
    sleep(0.5)
    pyautogui.moveTo(X_SPOT_EXP, Y_SPOT_EXP)
    sleep(0.2)
    pyautogui.click(X_SPOT_EXP, Y_SPOT_EXP)
    sleep(0.5)
    pyautogui.click(X_SPOT_EXP, Y_SPOT_EXP)
    sleep(5)
    pyautogui.keyDown('w')
    sleep(4)
    pyautogui.keyUp('w')
    sleep(0.2)
    curar()
    voltar_spot_exp()


def sweet_scent():
    sleep(0.2)
    pyautogui.press('4')


def checa_mapa_e_define_spot_exp():  # Função que simula a ação de conferir em qual região o player está e leva-lo para o spot da farm
    global contador_setar_spot
    if contador_setar_spot == 1:
        pyautogui.press('2')
        sleep(1)
        while True:
            sinnoh_loc = pyautogui.locateOnScreen('pokemmo/files/sinnoh_map.PNG', region=REGIAO_MAPA_SINNOH, confidence=0.6)
            kanto_loc = pyautogui.locateOnScreen('pokemmo/files/kanto_map.PNG', region=REGIAO_MAPA_KANTO, confidence=0.6)
            hoen_loc = pyautogui.locateOnScreen('pokemmo/files/hoen_map.PNG', region=REGIAO_MAPA_HOEN, confidence=0.6)
            unova_loc = pyautogui.locateOnScreen('pokemmo/files/unova_map.PNG', region=REGIAO_MAPA_UNOVA, confidence=0.6)

            if kanto_loc is not None:
                sleep(0.2)
                pyautogui.click(X_KANTO, Y_KANTO)
                sleep(6)
                kanto_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_exp()
                contador_setar_spot -= 1
                break
            elif hoen_loc is not None:
                sleep(0.2)
                pyautogui.click(X_HOEN, Y_HOEN)
                sleep(5)
                hoen_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_exp()
                contador_setar_spot -= 1
                break
            elif unova_loc is not None:
                sleep(0.2)
                set_spot_exp()
                contador_setar_spot -= 1
                break
            elif sinnoh_loc is not None:
                sleep(0.2)
                pyautogui.click(X_SINNOH, Y_SINNOH)
                sleep(5)
                sinnoh_to_unova()
                sleep(3)
                abrir_mapa()
                set_spot_exp()
                contador_setar_spot -= 1
                break
            else:
                break


def checa_pokemon_e_contador_exp():  # Função que verifica a presença de um pokemon e atualiza o contador em função disso
    global contador
    while True:
        battle = pyautogui.locateOnScreen('pokemmo/files/battle.PNG', minSearchTime=3, region=(1519, 565, 54, 20), confidence=0.6)
        if contador == 0:  # Se o contador chegar a zero, o personagem se cura no cp, volta para o local de pesca e reseta o contador
            teleport()
            curar()
            voltar_spot_exp()
            contador += 4
        elif battle is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            sleep(3)
            atack()
            sleep(8)
            contador -= 1
        else:
            break


sleep(1)
while True:
    checa_mapa_e_define_spot_exp()
    sweet_scent()
    sleep(20)
    checa_pokemon_e_contador_exp()
