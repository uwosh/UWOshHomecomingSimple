## Script (Python) "getAllSlots"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
signupSheetBrains = context.queryCatalog({'portal_type':'HomecomingSignupSheet'})
signupSheetBrain = signupSheetBrains[0]
signupSheet = signupSheetBrain.getObject()
allSlots = []
schema = signupSheet.Schema().viewableFields(signupSheet)
for field in schema:
  name = field.getName()
  if name.find("timeslot") <> -1:
    allSlots.append(name)
return allSlots
