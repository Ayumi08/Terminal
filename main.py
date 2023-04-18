import colorama
import os
import readchar

from settings import *

colorama.init(autoreset=True,)

os.system('cls')
print(
    'Microsoft Windows [Version 10.0.19044.2846]\n(c) Microsoft Corporation. All rights reserved.\n\n')

try:
    os.chdir(f'C:/Users/{USERNAME}')
except FileNotFoundError:
    print(colorama.Fore.RED + colorama.Style.BRIGHT +
          'Critical Error!' + colorama.Fore.WHITE + '\n\nFileNotFoundError: [WinError 2] The system cannot find the path specified: C:/Users/{USERNAME}\n\nAre you sure you typed your USERNAME correctly?')


working_dir = os.getcwd()

print(working_dir+'>')
