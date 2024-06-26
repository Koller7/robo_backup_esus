import pyautogui
import time

# Arrasta o mouse e clica no icone do aplicativo do backup a esquerda

pyautogui.moveTo(361,1004)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

# clica no backup no canto superior esquerdo

pyautogui.moveTo(382,468)
time.sleep(1)
pyautogui.click()
time.sleep(1)

# inicia o backup

pyautogui.moveTo(666,603)
time.sleep(1)
pyautogui.click()

# confirma o backup

time.sleep(1800)
pyautogui.moveTo(643,520)
time.sleep(1)
pyautogui.click()
time.sleep(1)

# minimiza o sistema do backup

pyautogui.moveTo(833,258)
time.sleep(1)
pyautogui.click()





