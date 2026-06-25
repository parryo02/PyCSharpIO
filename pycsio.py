def WriteLine(*args, **kwargs):
    print(*args, **kwargs)
    
def Write(*args, **kwargs):
    kwargs['end'] = ''
    print(*args, **kwargs)
def ReadLine(*args):
    Write(*args, flush=True)
    return input()

def Read(*args):
    Write(*args, flush=True)
    import sys
    if sys.platform.startswith('win'):
        # On Windows, use the msvcrt module [citation:8][citation:10].
        import msvcrt
        # msvcrt.getch() returns bytes, so decode it.
        return msvcrt.getch().decode('utf-8')
    else:
        # On Unix-like systems (Linux, macOS), use termios and tty [citation:3][citation:8].
        import termios
        import tty

        fd = sys.stdin.fileno()
        # Save the current terminal settings.
        old_settings = termios.tcgetattr(fd)
        try:
            # Set the terminal to "raw" mode, which disables line buffering.
            tty.setraw(sys.stdin.fileno())
            # Read exactly one character from stdin.
            ch = sys.stdin.read(1)
        finally:
            # Restore the original terminal settings.
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
