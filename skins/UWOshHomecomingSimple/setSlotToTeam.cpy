## Controller Python Script "setSlotToTeam"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example form action code

# Get a value from the REQUEST
#n = context.REQUEST.get('n')

# do something with the value here
# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
from Products.Archetypes.utils import addStatusMessage

request = context.REQUEST
RESPONSE =  request.RESPONSE
#print "request is", request
#print "response is", RESPONSE

teamNameNotFound = '__no_team_to_assign__'
teamName = request.get('teamToAssign', teamNameNotFound)
#print "teamToAssign is", teamName

slotNotFound = '__no_slot_to_assign__'
desiredSlot = request.get('slotSelection', slotNotFound)
#print "desiredSlot is", desiredSlot

signupSheetBrains = context.queryCatalog({'portal_type':'HomecomingSignupSheet'})
signupSheetBrain = signupSheetBrains[0]
signupSheet = signupSheetBrain.getObject()

if teamName <> teamNameNotFound:
    state.setError ('teamToAssign', 'You do not have a primary team to assign to a time slot.')

if desiredSlot <> slotNotFound:
    state.setError ('teamToAssign', 'You did not select a time slot.')

noSuchSlot = '__no_such_slot__'
if getattr(signupSheet, desiredSlot, noSuchSlot) == noSuchSlot:
    state.setError ('desiredSlot', "There is no time slot named '%s'." % desiredSlot)

for field in signupSheet.Schema().viewableFields (signupSheet):
    fieldName = field.getName()
    if fieldName == desiredSlot:
        mutator = field.getMutator(signupSheet)
        mutator (teamName)
        desiredSlotLabel = field.widget.label

portal_status_message = "Assigned team '%s' to slot '%s' ok." % (teamName, desiredSlotLabel)
addStatusMessage(context.REQUEST, portal_status_message)

redirect_to = context.portal_url.getPortalObject().absolute_url()+'/homecoming-signup-sheet'
state.setNextAction ('redirect_to:string:' + redirect_to)

#return printed



# (Optional) set the default next action (this can be overridden
# in the script's actions tab in the ZMI).
#state.setNextAction('redirect_to:string:http://www.plone.org')

# Always make sure to return the ControllerState object
return state
