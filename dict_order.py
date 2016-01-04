def dict_order(d,type='key',d_reverse=False):
    '''
    type:
        'key'(defaut)
        'value'
        'key_len'
        'value_len'
    '''

    assert isinstance(d,dict), 'parameter d must be dict type!'
    assert type in ('key','value','key_len','value_len'), 'parameter type must be key/value/key_len/value_len!'

    from collections import OrderedDict

    if d_reverse:
        if 'key'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: t[0] ,reverse=True))
        elif 'value'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: t[1] ,reverse=True))
        elif 'key_len'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: len(t[0]) ,reverse=True))
        elif 'value_len'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: len(t[1]) ,reverse=True))
    else:
        if 'key'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
        elif 'value'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: t[1]))
        elif 'key_len'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
        elif 'value_len'==type:
            return OrderedDict(sorted(d.items(), key=lambda t: len(t[1])))