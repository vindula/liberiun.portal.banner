## Script (Python) "verificaTarget"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=item
##title=
##

if item.getLinkTarget == True:
    target='_blank'
else:
    target=''

return target