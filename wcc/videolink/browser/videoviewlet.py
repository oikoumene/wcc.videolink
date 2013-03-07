from five import grok
from plone.app.layout.viewlets.interfaces import IBelowContentTitle
from wcc.videolink.interfaces import IVideoLinkEnabled
import urlparse

grok.templatedir('templates')

class VideoViewlet(grok.Viewlet):
    grok.name('wcc.videolink.videoviewlet')
    grok.template('videoviewlet')
    grok.context(IVideoLinkEnabled)
    grok.require('zope2.View')
    grok.viewletmanager(IBelowContentTitle)

    def embedlink(self):
        if not self.context.video_url:
            return ''
        q = urlparse.parse_qs(urlparse.urlparse(self.context.video_url).query)
        if q.get('v',None):
            return 'http://www.youtube.com/embed/%s' %  q['v'][0]
        return ''

