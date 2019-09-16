import urllib.request

import gevent
from gevent import monkey

monkey.patch_all()


def picdown(name, url):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    with open(name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([gevent.spawn(picdown,"c:/devTools/pywhl/1.jpg",
                            "https://rpic.douyucdn.cn/live-cover/roomCover/2019/08/21/4f240e51535eab040f2b6c710d006d07_big.jpg")
                    ,gevent.spawn(picdown,"c:/devTools/pywhl/2.jpg","https://apic.douyucdn.cn/upload/avatar_v3/201905/f1a69d5280cd44b4881c8764fa24151f_big.jpg")])


if __name__ == '__main__':
    main()
