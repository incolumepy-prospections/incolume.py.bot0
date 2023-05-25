import time

import pyautogui


def bot_reservapr(url:str=''):
    """Automação para agendamento de sala com pyautogui."""
    
    url = url or 'https://intranetsispr2.presidencia.gov.br/reservapr/login.php'

    #
    pyautogui.alert("Pronto para iniciar a automação?")
    # pyautogui.PAUSE = .5

    pyautogui.press("winleft")
    pyautogui.write("chromium")
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.write(url)
    pyautogui.press("enter")


if __name__ == "__main__":  # pragma: no cover
    automation1()
