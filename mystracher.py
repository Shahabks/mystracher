# -*- coding: utf-8 -*-
""" ATD module
helper classes and methods for playing with After The Deadline service
See http://www.afterthedeadline.com/api.slp for the API documentation.

Usage example:
setDefaultKey('your AfterTheDeadline API key')
errs = checkDocument('your text')
for error in errs:
    print "string: %s" % error.string
    print "description: %s" % error.description
    for suggestion in error.suggestions:
        print "suggestion: %s" % suggestion

Build on work done by Miguel Ventura
License: MIT
"""
import http.client
import urllib.request, urllib.parse, urllib.error
from xml.etree import ElementTree

_key = None

def setDefaultKey(key):
    global _key
    _key = key
    
def checkDocument(text, key=None):
    """Invoke checkDocument service with provided text and optional key.
    If no key is provided, a default key is used.

    Returns list of Error objects.

    See http://www.afterthedeadline.com/api.slp for more info."""
    
    global _key
    if key is None:
        if _key is None:
            raise Exception('Please provide key as argument or set it using setDefaultKey() first')
        key = _key
    
    params = urllib.parse.urlencode({
        'key': key,
        'data': text,
    })
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'User-Agent':' python-ATD',
    }
    #pdb.set_trace()
    service = http.client.HTTPConnection("service.afterthedeadline.com")
    service.request("POST", "/checkDocument", body=params, headers=headers)
    response = service.getresponse()
    if response.status != http.client.OK:
        service.close()
        raise Exception('Unexpected response code from AtD service %d' % response.status)
    response_text = response.read()
    #print(params)
    #print(response_text)
    e = ElementTree.fromstring(response_text)
    service.close()
    errs = e.findall('message')
    if len(errs) > 0:
        raise Exception('Server returned an error: %s' % errs[0].text)
    return [Error(err) for err in e.findall('error')]

class Error:
    """ AtD Error Object
    These are to be returned in a list by checkText()
    Available properties are: string, description, precontext, type, url
    and suggestions.

    Look at http://www.afterthedeadline.com/api.slp for more information."""
    def __init__(self, e):
        self.string = e.find('string').text
        self.description = e.find('description').text
        self.precontext = e.find('precontext').text
        self.type = e.find('type').text
        if not e.find('url') is None:
            self.url = e.find('url').text
        else:
            self.url = ""
        if not e.find('suggestions') is None:
            self.suggestions = [o.text for o in e.find('suggestions').findall('option')]
        else:
            self.suggestions = []
    def __str__(self):
        return "%s (%s)" % (self.string, self.description)

def stats(data, key=None):
    """Invoke stats service with provided text and optional key.
    If no key is provided, a default key is used.

    Returns list of Metric objects.

    See http://www.afterthedeadline.com/api.slp for more info."""
    
    global _key
    if key is None:
        if _key is None:
            raise Exception('Please provide key as argument or set it using setDefaultKey() first')
        key = _key

    params = urllib.parse.urlencode({
        'key': key,
        'data': data,
    })
    service = http.client.HTTPConnection("service.afterthedeadline.com")
    service.request("POST", "/stats", params)
    response = service.getresponse()
    if response.status != http.client.OK:
        service.close()
        raise Exception('Unexpected response code from AtD service %d' % response.status)
    e = ElementTree.fromstring(response.read())
    service.close()
    return [Metric(metric) for metric in e.findall('metric')]

class Metric:
    """ AtD Metric Object
    These are to be returned in a list by stats()
    Available properties are: type, key and value.

    Look at http://www.afterthedeadline.com/api.slp for more information."""
    def __init__(self, e):
        self.type = e.find('type').text
        self.key = e.find('key').text
        self.value = int(e.find('value').text)

    def __str__(self):
        return "%s(%s:%d)" % (self.type, self.key, self.value)
    
    @staticmethod
    def filterByType(metrics, t):
        """Filter a list leaving only Metric objects whose type matches 't'"""
        return [m for m in metrics if m.type == t]
    @staticmethod
    def filterByKey(metrics, k):
        """Filter a list leaving only Metric objects whose key matches 'k'"""
        return [m for m in metrics if m.key == k]

def mystracher():
    textt=str(input("Enter the text here:     "))

    setDefaultKey('mygra2019#shs')
    errs=checkDocument(textt)
    pointt=-1
    tott=1
    for error in errs:
        print("string:  ", error.string)
        print("description  ", error.description)
        print("type   ", error.type)
        print("precontext  ", error.precontext)
        print("------------")
        tott=tott+1
        if error.type=="spelling":
            pointt=pointt-1
        for suggestion in error.suggestions:
            print("suggestion:  ", suggestion)
            print("===============")
        
    for m in errs:
        print(str(m))
    print("===============")
    print("Score    :", (-pointt)/tott)
 
