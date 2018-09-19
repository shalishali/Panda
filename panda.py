import  re
from urllib import request
class Panda():
    url='https://www.panda.tv/cate/hearthstone'
    linkall = '<div class="video-info">([\s\S]*?)</div>'
    namelink = '</i>([\s\S]*?)</span>'
    numberlink = '<span class="video-number">([\s\S]*?)</span>'
    def __fetch_panda(self):
        r = request.urlopen(Panda.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    #分析
    def __analysis(self,htmls):
        linkhtml = re.findall(Panda.linkall,htmls)
        alls = []
        for html in linkhtml:
            name = re.findall(Panda.namelink, html)
            number = re.findall(Panda.numberlink, html)
            all={'name':name,'number':number}
            alls.append(all)
        return alls
    #提取数据
    def __refine(self,alls):
        l = lambda all:{
            'name':all['name'][0].strip(),
            'number':all['number'][0]
            }
        return map(l,alls)

    #排序
    def __sort(self,alls):
         alls = sorted(alls, key = self.__sort_seed,reverse=True)
         return alls
    def __sort_seed(self,all):
        r = re.findall('\d*', all['number'])
        number = float(r[0])
        if '万' in all['number']:
            number *= 10000
        return number

    #展示
    def __show(self,alls):
         # for all in alls :
             # print(all['name']+'---'+all['number'])
         for rank in range(0, len(alls)):
            print(str(rank+1)
            +'  '+alls[rank]['name']
            +'---'+alls[rank]['number'])

     #入口
    def go(self):
        htmls = self.__fetch_panda()
        alls = self.__analysis(htmls) #值为字典
        alls = list(self.__refine(alls))
        alls = self.__sort(alls)
        self.__show(alls)

panda = Panda()
panda.go()