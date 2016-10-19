class PrintColor():
    STYLE = {
        'fore':
        {
            'black'    : 30,
            'red'      : 31,
            'green'    : 32,
            'yellow'   : 33,
            'blue'     : 34,
            'purple'   : 35,
            'cyan'     : 36,
            'white'    : 37,
        },
        'back' :
        {
            'black'     : 40,
            'red'       : 41,
            'green'     : 42,
            'yellow'    : 43,
            'blue'      : 44,
            'purple'    : 45,
            'cyan'      : 46,
            'white'     : 47,
        },
        'mode' :
        {
            'normal'    : 0,
            'bold'      : 1,
            'underline' : 4,
            'blink'     : 5,
            'invert'    : 7,
            'hide'      : 8,
        },
        'default' :
        {
            'end' : 0,
        },
    }
    def __init__(self, mode='normal', fore='white', back='black'):
        mode = PrintColor.STYLE['mode'].get(mode, 'e')
        fore = PrintColor.STYLE['fore'].get(fore, 'e')
        back = PrintColor.STYLE['back'].get(back, 'e')
        if (mode=='e' or fore=='e' or back=='e'):
            raise ValueError('wrong parameter!')
        self.style = '\033[%sm' % ';'.join([str(x) for x in [mode, fore, back] if x])
        self.end = '\033[%sm' % PrintColor.STYLE['default']['end']
    def __call__(self, string):
        return '%s%s%s' % (self.style, string, self.end)

print(PrintColor('bold','red','cyan')('haha'))
