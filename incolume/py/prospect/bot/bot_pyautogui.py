# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import time

import pyautogui


def automation1():
    """Automação para agendamento de sala com pyautogui."""

    #
    pyautogui.alert('Pronto para iniciar a automação?')
    # pyautogui.PAUSE = .5

    pyautogui.press('winleft')
    pyautogui.write('chromium')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write(r'https://keep.google.com')
    pyautogui.press('enter')


if __name__ == '__main__':    # pragma: no cover
    automation1()
