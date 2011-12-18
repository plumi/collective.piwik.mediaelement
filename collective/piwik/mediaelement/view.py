from Products.Five.browser  import BrowserView
import urllib2, simplejson
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.piwik.core.interfaces import IPiwikSettings
import logging

log = logging.getLogger('collective.piwik.mediaelement')

class CountView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.plays = 0
        self.unique = 0
        self.downloads = 0
        self.unique = 0        

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json')
        if self.request.URL.endswith('downcount'):
            result = self.getDownloadCount()
        else:
            result = self.getPlayCount()
        return simplejson.dumps(result)

    def getPlayCount(self):
        """ Return video play count and unique visits from Piwik 
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPiwikSettings)

        self.plays = 0
        self.unique = 0
        
        #for urls with slash(es) on the end
        self.page_url = self.context.absolute_url().strip('/')        

        url = settings.piwik_server +\
            '?module=API&method=Actions.getOutlink&idSite=' +\
            settings.piwik_siteid +\
            '&outlinkUrl=' +\
            self.page_url +\
            '&period=year&date=last100&format=json&token_auth=' +\
            settings.piwik_key
        try: 
            piwik_data = simplejson.load(urllib2.urlopen(url))
        except Exception, e: # might be a URLError, timeout etc
            log.error("exception %s !"  % e)
            piwik_data = {}

        if piwik_data.get('result') == 'error':
            log.error("error loading piwik data: %s" % piwik_data)
            piwik_data = {} # error on the communication.maybe wrong token?

        for year in piwik_data:
            for entry in piwik_data[year]:
                self.plays += int(entry['nb_hits'])
                self.unique += int(entry['nb_visits'])

        return(self.plays, self.unique)

    def getDownloadCount(self):
        """ Return the number of downloads from Piwik 
        """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPiwikSettings)

        self.downloads = 0
        self.unique = 0
        
        #for urls with slash(es) on the end
        self.page_url = self.context.absolute_url().strip('/')

        url = settings.piwik_server +\
            '?module=API&method=Actions.getDownload&idSite=' +\
            settings.piwik_siteid +\
            '&downloadUrl=' +\
            self.page_url +\
            '&period=year&date=last100&format=json&token_auth=' +\
            settings.piwik_key
        try: 
            piwik_data = simplejson.load(urllib2.urlopen(url))
        except Exception, e: # might be a URLError, timeout etc
            piwik_data = {}

        if piwik_data.get('result') == 'error':
            piwik_data = {} # error on the communication.maybe wrong token?

        for year in piwik_data:
            for entry in piwik_data[year]:
                self.downloads += int(entry['nb_hits'])
                self.unique += int(entry['nb_visits'])

        return(self.downloads, self.unique)
