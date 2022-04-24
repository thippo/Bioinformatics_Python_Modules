import time
import curses
import urllib
import urllib.request

class ConvertibleBond():
    
    def __init__(self, p_code, p_name, p_maturity, p_maturity_price):
        self.code = p_code
        self.name = p_name
        self.maturity = p_maturity
        self.maturity_price = p_maturity_price
        
    def _get_now_date(self):
        return time.strftime("%Y-%m-%d", time.localtime()) 

    def day_to_maturity(self):
        day1 = time.strptime(self.maturity, '%Y-%m-%d')
        day2 = time.strptime(self._get_now_date(), '%Y-%m-%d')
        day_num = (int(time.mktime(day1)) - int(time.mktime(day2))) / (24 * 60 * 60)
        return abs(int(day_num))

    def get_current_price(self):
        return float(urllib.request.urlopen("http://hq.sinajs.cn/list="+self.code).read().decode("gbk","ignore").split(",")[3])

    def YTM(self, current_price=""):
        if current_price:
            return str(round(((self.maturity_price/current_price)**(1/self.day_to_maturity())-1)*365*100, 2))+"%"
        else:
            return str(round(((self.maturity_price/self.get_current_price())**(1/self.day_to_maturity())-1)*365*100, 2))+"%"

    def YTM2pot5(self):
        return str(round(self.maturity_price/((0.025/365+1)**self.day_to_maturity()), 2))

    def YTM5(self):
        return str(round(self.maturity_price/((0.05/365+1)**self.day_to_maturity()), 2))

    def __str__(self):
    	return "haha"



if __name__ == '__main__':
    convertiblebond_list = [
        ["sz128114","正邦转债","2026-06-17",110.00],
        ["sh113596","城地转债","2026-07-28",108.00],
        ["sz128062","亚药转债","2025-04-02",115.00],
        ["sh110072","广汇转债","2026-08-18",110.00],
        ["sh113595","花王转债","2026-07-21",116.00],
        ["sh113589","天创转债","2026-06-24",110.00],
        ["sz127019","国城转债","2026-07-15",110.00],
        ["sh110059","浦发转债","2025-10-28",110.00],
        ["sz128124","科华转债","2026-07-28",106.00],
        ["sh113578","全筑转债","2026-04-20",113.00],
        ["sh113569","科达转债","2026-03-09",115.00],
        ["sh113042","上银转债","2027-01-25",112.00],
        ["sz128100","搜特转债","2026-03-12",112.00],
        ["sh113584","家悦转债","2026-06-05",110.00],
        ["sz127034","绿茵转债","2027-04-30",113.00],
        ["sz123128","首华转债","2027-11-01",110.00],
        ["sh113584","家悦转债","2026-06-05",110.00],
    ]
    
    convertiblebond_code_list = ",".join([x[0] for x in convertiblebond_list])

    for i in convertiblebond_list:
        locals()["cb_"+i[0]] = ConvertibleBond(*i)
    '''
    stdscr = curses.initscr()
    while 1:
        head = "{:>8s}{:>8s}{:>10s}{:>6s}{:>7s}{:>8s}{:>7s}".format("名称","代码","到期日","剩余天数","到期赎回价","现价","到期收益率")
        stdscr.addstr(0, 0, head)
        convertiblebond_currentprice_list = [float(x.split(",")[3]) for x in urllib.request.urlopen("http://hq.sinajs.cn/list="+convertiblebond_code_list).read().decode("gbk","ignore").rstrip().split(";") if x]
        for i in range(len(convertiblebond_list)):
            lin_name = convertiblebond_list[i][1]
            lin_code = convertiblebond_list[i][0]
            lin_maturity = convertiblebond_list[i][2]
            lin_mprice = convertiblebond_list[i][3]
            lin_days = locals()["cb_"+convertiblebond_list[i][0]].day_to_maturity()
            lin_cprice = convertiblebond_currentprice_list[i]
            lin_ytm = locals()["cb_"+convertiblebond_list[i][0]].YTM(convertiblebond_currentprice_list[i])
            stdscr.addstr(i+1, 0, "{:>6s}{:>10s}{:>13s}{:>10s}{:>12s}{:>10s}{:>12s}".format(lin_name,lin_code,lin_maturity,str(lin_days),str(lin_mprice),str(lin_cprice),lin_ytm))
        stdscr.addstr(len(convertiblebond_list)+1, 0, "")
        stdscr.refresh()
        time.sleep(5)
    '''
    while 1:
        print()
        print("——————————————————————————————————————————————————————")
        linshi = "{}{}{}   {}   {}{}{} {}{}  {}  {} {} {}".format("|","序号","|","名称","|","剩余天数","|","赎回价","|","YTM5%","|","YTM2.5%","|")
        print(linshi)
        print("——————————————————————————————————————————————————————")
        for i,j in enumerate(convertiblebond_list):
            linshi = "{}{:>3s} {} {} {} {:>4s}{} {} {:<4s} {}  {:<6s} {}  {:<6s} {}".format("|",str(i),"|",j[1],"|",str(locals()["cb_"+convertiblebond_list[i][0]].day_to_maturity()),"天","|",str(convertiblebond_list[i][3]),"|",locals()["cb_"+convertiblebond_list[i][0]].YTM5(),"|",locals()["cb_"+convertiblebond_list[i][0]].YTM2pot5(),"|")
            print(linshi)
            print("——————————————————————————————————————————————————————")
        print()
        index1 = int(input("请输入序号:"))
        print()
        linshi = "{}{} {}".format("您选择的是:",convertiblebond_list[index1][1],"请输入现价:")
        index2 = float(input(linshi))
        if index2:
            linshi = "{}{}".format("YTM:",str(locals()["cb_"+convertiblebond_list[index1][0]].YTM(index2)))
            print(linshi)
            input()

    #print(cb_sh110072.YTM(97.19))