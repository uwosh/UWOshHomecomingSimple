## Script (Python) "getOpenSlots"
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
openSlots = []
if signupSheet.timeslot1 == '':
    openSlots.append ('timeslot1')
if signupSheet.timeslot2 == '':
    openSlots.append ('timeslot2')
if signupSheet.timeslot3 == '':
    openSlots.append ('timeslot3')
if signupSheet.timeslot4 == '':
    openSlots.append ('timeslot4')
if signupSheet.timeslot5 == '':
    openSlots.append ('timeslot5')
if signupSheet.timeslot6 == '':
    openSlots.append ('timeslot6')
if signupSheet.timeslot7 == '':
    openSlots.append ('timeslot7')
if signupSheet.timeslot8 == '':
    openSlots.append ('timeslot8')
if signupSheet.timeslot9 == '':
    openSlots.append ('timeslot9')
if signupSheet.timeslot10 == '':
    openSlots.append ('timeslot10')
if signupSheet.timeslot11 == '':
    openSlots.append ('timeslot11')
if signupSheet.timeslot12 == '':
    openSlots.append ('timeslot12')
if signupSheet.timeslot13 == '':
    openSlots.append ('timeslot13')
if signupSheet.timeslot14 == '':
    openSlots.append ('timeslot14')
if signupSheet.timeslot15 == '':
    openSlots.append ('timeslot15')
if signupSheet.timeslot16 == '':
    openSlots.append ('timeslot16')
return openSlots
