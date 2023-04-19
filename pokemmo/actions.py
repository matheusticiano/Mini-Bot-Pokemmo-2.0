from time import sleep
import pyautogui

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
X_SPOT_EXP = 1144  # Cordenadas spot de exp
Y_SPOT_EXP = 444   # Cordenadas spot de exp
contador = 1  # Numeros de pps do ataque do seu pokemon (começa em 1 para curar seu pokemon em casos que não esteja completo)
contador_setar_spot = 1  # Um contador para fazer com que a função checa_mapa_e_define_spot ocorra apenas um vez


def pesca():  # Função que simula o ato de pescar
    pyautogui.press('3')
    sleep(4)


def checa_seta():  # Função que verifica se a seta está visível e clica nela para lutar com o pokemon / pescar novamente
    while True:
        seta_loc = pyautogui.locateOnScreen('pokemmo/files/seta.PNG', region=REGIAO_SETA, confidence=0.6)
        if seta_loc is not None:
            pyautogui.click(seta_loc.left + seta_loc.width/2, seta_loc.top + seta_loc.height/2)
            sleep(2)
        else:
            break


def atack():  # Função que simula o ataque do personagem
        pyautogui.press('E')
        pyautogui.press('S')
        pyautogui.press('E')
        pyautogui.press('E')


def checa_pokemon_e_contador_payday():  # Função que verifica a presença de um pokemon e atualiza o contador em função disso
    global contador
    while True:
        poke1_loc = pyautogui.locateOnScreen('pokemmo/files/poke_1.PNG', region=(0, 890, 429, 156), confidence=0.8)
        poke2_loc = pyautogui.locateOnScreen('pokemmo/files/poke_2.PNG', region=(0, 890, 429, 156), confidence=0.8)
        poke3_loc = pyautogui.locateOnScreen('pokemmo/files/poke_3.PNG', region=(0, 890, 429, 156), confidence=0.8)
        if contador == 0:  # Se o contador chegar a zero, o personagem se cura no cp, volta para o local de pesca e reseta o contador
            teleport()
            curar()
            voltar_spot_payday()
            contador += 24
        elif poke1_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        elif poke2_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        elif poke3_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        else:  # Se o contador chegar a zero, volta para o local de pesca e reseta o contador
            break


def curar():  # Função que simula a ação de curar no cp
    sleep(4)
    pyautogui.keyDown('e')
    sleep(8)
    pyautogui.keyUp('e')
    sleep(0.2)


def teleport():  # Função que simula a ação de teleporta para o cp
    sleep(8)
    pyautogui.keyDown('5')
    sleep(0.1)
    pyautogui.keyUp('5')


def voltar_spot_payday():  # Função que simula a ação de voltar ao local de pesca
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(2.8)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.7)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.press('1')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(3)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(0.3)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(2)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.2)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(2.4)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(0.1)
    pyautogui.keyUp('d')


def hoen_to_unova():  # Função que simula a ação de viajar de hoen para unova
    sleep(1)
    pyautogui.keyDown('a')
    sleep(0.3)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(0.6)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(2)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(0.6)
    pyautogui.keyUp('w')
    sleep(2)
    pyautogui.keyDown('d')
    sleep(0.8)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(0.8)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('e')
    sleep(0.1)
    pyautogui.keyUp('e')
    sleep(0.2)
    travel()


def kanto_to_unova():  # Função que simula a ação de viajar de kanto para unova
    pyautogui.keyDown('s')
    sleep(0.6)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(1.5)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(1.2)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(2)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(0.3)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(0.3)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(2)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.6)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(0.5)
    pyautogui.keyUp('s')
    sleep(0.2)
    travel()


def sinnoh_to_unova():  # Função que simula a ação de viajar de sinnoh para unova
    sleep(1)
    pyautogui.keyDown('s')
    sleep(0.6)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.6)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(1.8)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(1.6)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(1.5)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(1.6)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('e')
    sleep(0.1)
    pyautogui.keyUp('e')
    sleep(0.2)
    travel()


def travel():  # Função que simula a ação de falar com o npc para viajar
    pyautogui.keyDown('e')
    sleep(0.1)
    pyautogui.keyUp('e')
    sleep(0.2)
    pyautogui.click(957, 766)
    sleep(1)
    pyautogui.keyDown('e')
    sleep(0.1)
    pyautogui.keyUp('e')


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


def abrir_mapa():  # Função que simula a ação de abrir o mapa
    sleep(1)
    pyautogui.press('2')
    sleep(0.5)


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


def sweet_scent():  # Funçãp que simula o uso do sweet scent
    sleep(0.2)
    pyautogui.press('4')


def checa_mapa_e_define_spot_payday():  # Função que simula a ação de conferir em qual região o player está e leva-lo para o spot da farm
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
