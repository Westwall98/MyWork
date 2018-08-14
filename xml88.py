# -*- coding:utf-8 -*-

import xml.sax
from datetime import datetime

class ForecastHandler(xml.sax.ContentHandler):
    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == 'results':
            self.result = {}
        elif tag == 'yweather:location':
            self.result['city'] = attrs['city']
        elif tag == 'yweather:condition':
            self.result['forecast'] = attrs['temp']
        elif tag == 'yweather:forecast':
            ft = {
                'date':datetime.strptime(attrs['date'],'%d %b %Y').strftime('%Y-%m-%d'),
                'highest':int(attrs['high']),
                'lowest':int(attrs['low'])
            }
            [self.result['forecast']].append(ft)
            print(ft)

    def endElement(self,name):
        if name == 'results':
            print(self.result)
        self.CurrentData = ""

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = ForecastHandler()
    parser.setContentHandler(Handler)
    parser.parse("forecast.xml")