## Script (Python) "doesTeamHaveSlot"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=team
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
    if team == getattr(signupSheet, name):
      return context.getSlotLabel(name)
return False
