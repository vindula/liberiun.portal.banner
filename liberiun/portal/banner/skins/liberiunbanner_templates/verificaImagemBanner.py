## Script (Python) "verifica_logado"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain
##title=
##

return context.portal_catalog.getIndexDataForRID(brain.getRID())['TemImagemNoBanner']
