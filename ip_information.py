def ip_information(ip):
    import urllib
    import json
    data_dict=json.loads(urllib.request.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=" + ip).read().decode())
    if data_dict['code']==0:
        return data_dict
    else:
        return 'no data'