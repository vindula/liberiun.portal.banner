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

    ReferenceField(
        name='link_interno',
        widget=ReferenceBrowserWidget(
            label='Link Interno',
            description="Caso selecionado o link será apontado para o local de sua escolha.",
            label_msgid='LiberiunBanner_label_link_interno',
            i18n_domain='LiberiunBanner',
        ),
        #allowed_types=('Folder',),
        relationship='link_interno',
        multiValued=False,
    ),

    ImageField(
        name='imagem_banner',
        max_size = zconf.ATNewsItem.max_image_dimension,
        sizes= {'large'      :  (768, 768),
                'preview'    :  (400, 400),
                'banner'     :  (545, 115),
                'deolho'     :  (70, 50),
                'mini'       :  (200, 200),
                'thumb'      :  (128, 128),
                'tile'       :  (64, 64),
                'icon'       :  (32, 32),
                'listing'    :  (16, 16),
                'pequin'     :  (468, 60),
                'cipo'       :  (155, 63),
                'ciporodape' :  (162, 46),
                'af'         :  (80, 60),
                'jornalu'    :  (171, 153),
                'cxunidade'  :  (177, 177)
               },

        validators = (('isNonEmptyFile', V_REQUIRED),
                             ('checkNewsImageMaxSize', V_REQUIRED)),
        widget=ImageField._properties['widget'](
            label="Imagem do Banner",
            description="Escolha a imagem do banner.",
            label_msgid='LiberiunBanner_label_imagem_banner',
            i18n_domain='LiberiunBanner',
        ),
        required=1,
        storage=AttributeStorage(),
    ),

    BooleanField('linkTarget',
        default=False,
        widget=BooleanWidget(
            label="Abrir link em nova janela",
            description="Caso selecionado o link será exibido em uma nova janela",
            label_msgid='LiberiunBanner_label_linkTarget',
            i18n_domain='LiberiunBanner',
        ),
        required=False,
    ),


),
)

Banner_schema = BaseSchema.copy() + \
    getattr(ATLink, 'schema', Schema(())).copy() + \
    schema.copy()

# Alteracoes na heranca do tipo ATLink
Banner_schema['description'].schemata='default'
Banner_schema['remoteUrl'].required = False
Banner_schema['remoteUrl'].default = ''
Banner_schema['remoteUrl'].widget.label = 'Link Externo'
Banner_schema['remoteUrl'].widget.description = 'Será ultilizado quando não houver link interno.'


class Banner(ATLink, BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBanner)

    meta_type = 'Banner'
    _at_rename_after_creation = True

    schema = Banner_schema


    # Metodos
    
    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('imagem_banner').tag(self, **kwargs)

    def getTarget(self):
        if self.linkTarget: 
            return '_blank'
        else:
            return ''
            
    def getLink(self):
        """Retorna o interno caso nao haja retorna o externo
        """
        field = self.getField('link_interno')

        if field.get(self) is not None:
            return field.get(self).absolute_url()

        if self.remoteUrl.startswith('http'): 
            return self.remoteUrl
        elif self.remoteUrl is None or self.remoteUrl == '':
            return ''
        else:
            return 'http://' + self.remoteUrl
        
registerType(Banner, PROJECTNAME)
