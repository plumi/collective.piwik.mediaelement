from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.piwik.core.interfaces import IPiwikSettings

class PiwikVideoViewlet(ViewletBase):
    """ Piwik Video Viewlet
    """
    def update(self):
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IPiwikSettings)

