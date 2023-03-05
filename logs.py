import colorama, threading
__lock__ = threading.Lock()
colorama.init()
def log(message, color=None):
    if color:
        print(color + message + colorama.Style.RESET_ALL)
    else:
        print(message)


def error(message):
    log(message, colorama.Fore.RED)
def success(message):
    log(message, colorama.Fore.GREEN)
def info(message):
    log(message, colorama.Fore.BLUE)
def warning(message):
    log(message, colorama.Fore.YELLOW)
def details(message):
    log("  >"+message, colorama.Fore.CYAN)

def print(message):
    __lock__.acquire()
    print(message+colorama.Style.RESET_ALL + "")
    __lock__.release()