def sorted_dict(dic, key=True, reverse=False):
    if key:
        return sorted(dic.items(), key=lambda d:d[0], reverse = reverse)
    else:
        return sorted(dic.items(), key=lambda d:d[1], reverse = reverse)
