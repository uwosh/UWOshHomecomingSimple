## Script (Python) "isSlotTaken"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=slot
##title=
##
signupSheetBrains = context.queryCatalog({'portal_type':'HomecomingSignupSheet'})
signupSheetBrain = signupSheetBrains[0]
signupSheet = signupSheetBrain.getObject()
return getattr(signupSheet, slot).strip()
