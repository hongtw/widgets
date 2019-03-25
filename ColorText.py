import sys
import colorama
from colorama import Fore, Back, Style
if sys.version_info < (3, 6):
    print("*****\n[WARNING] Please Use Python >= 3.6 (Yours is {0})\n*****".format('.'.join(map(str, sys.version_info[:3]))))
    sys.exit(1)

colorama.init()


def decorator(func):
    def wrapper(*args, **kwargs):
        text = args[0]
        if 'isBg' in kwargs:
            isBg = kwargs['isBg']
        elif len(args) > 1:
            isBg = args[1]
        else:
            isBg = False
        color = func.__name__.upper()

        if isBg:
            return f"{getattr(Back, color) + Fore.BLACK + Style.DIM}{text}{Style.RESET_ALL}"
        else:
            return f"{getattr(Fore, color) + Style.BRIGHT}{text}{Style.RESET_ALL}"
    return wrapper

class Color(object):

    @decorator
    def yellow(text, isBg=False):
        pass

    @decorator
    def green(text, isBg=False):
        pass

    @decorator
    def red(text, isBg=False):
        pass
    
    @decorator
    def cyan(text, isBg=False):
        pass

    @decorator
    def magenta(text, isBg=False):
        pass

    @decorator
    def blue(text, isBg=False):
        pass

    @decorator
    def white(text, isBg=False):
        pass

    def black(text, isBg=False):
        color = 'BLACK'
        if isBg:
            return f"{getattr(Back, color) + Fore.YELLOW + Style.DIM}{text}{Style.RESET_ALL}"
        else:
            return f"{getattr(Fore, color) + Style.BRIGHT}{text}{Style.RESET_ALL}"

if __name__ == "__main__":
    print(Color.yellow('haha'), 'kerker')
    print(Color.yellow('haha', isBg=True), "kerker")

    print(Color.green('haha'), 'kerker')
    print(Color.green('haha', True), "kerker")

    print(Color.red('haha'), 'kerker')
    print(Color.red('haha', True), "kerker")

    print(Color.cyan('haha'), 'kerker')
    print(Color.cyan('haha', True), "kerker")

    print(Color.magenta('haha'), 'kerker')
    print(Color.magenta('haha', True), "kerker")

    print(Color.blue('haha'), 'kerker')
    print(Color.blue('haha', True), "kerker")

    print(Color.white('haha'), 'kerker')
    print(Color.white('haha', True), "kerker")

    print(Color.black('haha'), 'kerker')
    print(Color.black('haha', True), "kerker")