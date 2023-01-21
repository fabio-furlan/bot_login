import pyautogui

pyautogui.PAUSE = 2

# abrir a ferramenta
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

# preencher o login
pyautogui.click(x=500, y=186)
pyautogui.write("Fabio")

# preencher a senha
pyautogui.click(x=511, y=225)
pyautogui.write("senha")

# clicar em fazer login
pyautogui.click(x=491, y=347)

import time

time.sleep(3)
pyautogui.position()
