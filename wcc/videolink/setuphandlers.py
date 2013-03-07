from collective.grok import gs
from wcc.videolink import MessageFactory as _

@gs.importstep(
    name=u'wcc.videolink', 
    title=_('wcc.videolink import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.videolink.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
