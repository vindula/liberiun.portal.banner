# -*- coding: utf-8 -*-
try: # New CMF
    from Products.CMFCore.permissions import setDefaultRoles 
except ImportError: # Old CMF
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles


PROJECTNAME = 'liberiun.portal.banner'

try:
    from Products.CMFPlone.migrations import v2_1
except ImportError:
    HAS_PLONE21 = False
else:
    HAS_PLONE21 = True


# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
#ADD_CONTENT_PERMISSIONS = {
#    'VindulaNews': 'vindula.content: Add VindulaNews',
#    'OrganizationalStructure': 'vindula.content: Add OrganizationalStructure',
#    'Unit': 'vindula.content: Add Unit',}


product_globals = globals()


# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from liberiun.portal.banner.AppConfig import *
except ImportError:
    pass