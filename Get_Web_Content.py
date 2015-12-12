#writen by thippo
#python version 3.4.3

def get_web_content(url):
'''
url的格式必须是http://xxxxxx.xxxx.xxxxx/

'''
    import urllib.request
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    content = opener.open(url).read()
    content = content.decode(errors='ignore')
    return content