from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner,aq_parent
from zope.interface import implements
from liberiun.portal.banner.browser.interfaces import IBanner
from plone.memoize.instance import memoize
from zope.app.component.hooks import getSite

class Banner(BrowserView):
    """View especifica do produto Banner"""
            
    def get_flash_banners(self):
        """Retorna os objetos to tipo banner em determinado local"""
        
        urltool = getSite().portal_url
        caminho = urltool.getPortalPath()+'/jornal-da-caixa/banners-do-jornal';
        ctool = getSite().portal_catalog
        items = ctool(portal_type='BannerFlash', 
                      review_state='published',
                      path=caminho)        
        return items
