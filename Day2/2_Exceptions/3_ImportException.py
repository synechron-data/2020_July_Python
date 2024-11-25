# try:
#     import pqrs
#     print(pqrs)
# except ImportError:
#     print("Noting Imported")


try:
    import msvcrt       # Microsoft Visual C++ Runtime (MSVCRT)

    def getkey():
        return msvcrt.getch()

except:
    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

print("Press any key to exit.....")
getkey()