## Script (Python) "retornaLinkCerto"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain
##title=
##

link_interno = context.portal_catalog.getIndexDataForRID(brain.getRID())['getBanner_link_interno']
link_externo = brain.getRemoteUrl


if link_interno:
    return {'link':link_interno, 'target':False}

if link_externo:
    if 'http://' not in link_externo:
        link_externo = 'http://%s'%link_externo
    return {'link':link_externo, 'target':True}
  
return {'link':context.portal_url(), 'target':False}
