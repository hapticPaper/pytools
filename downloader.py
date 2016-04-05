import os
import time

import requests


class Stream_Downloader(object):
    def __init__(self):
        self.session = requests.Session()


    def save_as(self, url, destination):
        #USAGE: download = Stream_Downloader()
        #       download.save_as('http://ufpr.dl.sourceforge.net/project/winpython/WinPython_2.7/2.7.10.3/WinPython-64bit-2.7.10.3.exe','WinPython-64bit-2.7.10.3.exe' )

        if os.path.isfile(destination):
            os.remove(destination)
        download = self.session.get(url, stream=True)
        with open(os.path.abspath('~download.chunks'), 'bw+') as f:
            i=0
            t = time.time()
            for chunk in download.iter_content(4096):
                print("\rDownloaded: {0:.3f} Mb in {1:.2f}s - avg:{2:.2f} Mb/s".format((i*4096)/(1024*1024), (time.time()-t), ((i*4096)/(1024*1024))/(time.time()-(t+1))), end="")
                f.write(chunk)
                i+=1
            print(" complete.\nSaved as {PWD}\{dest}".format(PWD=os.path.dirname(os.path.realpath(__file__)), dest=destination))
            f.close()
        os.rename('~download.chunks', destination)
        return

