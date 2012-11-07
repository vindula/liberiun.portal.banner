# -*- coding: utf-8 -*-
__author__ = "Liberiun <contato@liberiun.com>"
__docformat__ = "plaintext"
__license__ = "GPL - GNU GENERAL PUBLIC LICENCE"

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from liberiun.portal.banner.config import *
from Products.ATContentTypes.content.link import ATLink
from Products.ATContentTypes.configuration import zconf
from Products.validation import V_REQUIRED
from Products.CMFCore.permissions import View
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *

schema = Schema((

    FileField(
        name='arquivo_flash.swf',
        widget=FileField._properties['widget'](
            label='Arquivo Swf',
            description='Insira um arquivo no formato swf.',
            label_msgid='liberiun.portal.banner_label_arquivo_flash',
            i18n_domain='liberiun.portal.banner',
        ),
        storage=AttributeStorage(),
        required=True,
    ),

    StringField(
        name='altura',
        widget=StringField._properties['widget'](
            label='Altura',
            label_msgid='liberiun.portal.banner_label_altura',
            i18n_domain='liberiun.portal.banner',
        ),
    ),
    
    StringField(
        name='largura',
        widget=StringField._properties['widget'](
            label='Largura',
            label_msgid='liberiun.portal.banner_label_largura',
            i18n_domain='liberiun.portal.banner',
        ),
    ),    

    IntegerField(
        name='tempo',
        widget=IntegerField._properties['widget'](
            label='Tempo de Duração',
            description='Insira número em segundos do tempo de pausa do banner.',            
            label_msgid='liberiun.portal.banner_label_tempo',
            i18n_domain='liberiun.portal.banner',
        ),
        
    ),
    
    StringField(
        name='link_flash',
        default = "http://",        
        widget=StringField._properties['widget'](
            label='Link do Banner',
            label_msgid='liberiun.portal.banner_label_link_flash',
            i18n_domain='liberiun.portal.banner',
        ),
        validators=('isURL',),        
        required=False,
    ),            

),
)

BannerFlash_schema = BaseSchema.copy() + \
    schema.copy()


class BannerFlash(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBannerFlash)

    meta_type = 'BannerFlash'
    _at_rename_after_creation = True

    schema = BannerFlash_schema


    # Metodos

        
registerType(BannerFlash, PROJECTNAME)
