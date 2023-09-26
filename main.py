import pyautogui
import time
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# COMANDO ENTRA NO SITE #
time.sleep(0.5)
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(link)
pyautogui.press('enter')
# COMANDO ENTRA NO SITE #

# FAZ O LOGIN #
time.sleep(3)
pyautogui.click(x=555, y=360)
pyautogui.write('emaildeteste@gmail.com')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('senha123')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
# FAZ O LOGIN #

import pandas
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    time.sleep(1)
    pyautogui.click(x=569, y=246, clicks=2)

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha,'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))

    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.scroll(50000)
