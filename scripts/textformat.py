try:
    from clint.textui import colored
    from colorama import Fore, Back, Style
    from pyfiglet import Figlet
except:
    print("pacotes visuais do menu não instalados")


def welcome(text):
    try:
        result = Figlet()
        return colored.cyan(result.renderText(text))
    except:
        return text