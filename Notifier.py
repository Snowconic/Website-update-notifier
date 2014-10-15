import urllib2, webbrowser
from time import sleep
from datetime import datetime, date, time

def pTime():
    return datetime.now().strftime("%H:%M:%S") + " --- "

class Notify(object):
    def __init__(self, url):
        self.url = url
        self.data = ""

    def checkPage(self):
        req = urllib2.Request(self.url, None)
        u = urllib2.urlopen(req)
        newdata = u.read()
        print pTime(), "Checking --- " + self.url
        if self.data != newdata:
            print pTime(), self.url + " --- Has been updated"
            self.openPage(self.url)
            self.data = newdata
        else:
            print pTime(), "URL: " + self.url + " --- Stale"

    def openPage(self, url):
        webbrowser.open(url)

def Main():
    urlList = raw_input("Please enter URLs to check, separated by a comma: ")
    urlList = urlList.split(",")
    objList = []
    for i in range(0, len(urlList)):
        objList.append(Notify("http://" + urlList[i]))
    while(True):
        for i in objList:
            i.checkPage()
            print ""
        sleep(60)
        
if __name__ == "__main__":
    Main()
