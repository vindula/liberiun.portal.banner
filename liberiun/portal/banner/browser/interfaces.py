from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer bound to a Skin
       Selection in portal_skins.
       If you need to register a viewlet only for the "IntranetCaixa"
       skin, this is the interface that must be used for the layer attribute
       in IntranetCaixa/browser/configure.zcml.
    """
    
from zope.interface import Interface

class IBanner(Interface):
    """Interface de view do Banner
    """
    
    def get_flash_banners(self):
        """Retorna os objetos to tipo banner em determinado local"""


