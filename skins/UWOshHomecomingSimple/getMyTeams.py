## Script (Python) "getMyTeams"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
portal=context.portal_url.getPortalObject()
pm=portal.portal_membership
member=pm.getAuthenticatedMember()
email = member.getProperty('email')
fullname = member.getProperty('fullname')
if fullname == '':
  fullname = '__no_fullname_found__'
if email == '':
  email = '__no_email_found__'
teams = context.queryCatalog({'portal_type':'HomecomingTeam'})
myTeams = []
for team in teams:
  teamObject = team.getObject()
  if fullname == getattr(teamObject, 'membername1', None) or email == getattr(teamObject, 'memberemail1', None) or fullname == getattr(teamObject, 'membername2', None) or email == getattr(teamObject, 'memberemail2', None) or  fullname == getattr(teamObject, 'membername3', None) or email == getattr(teamObject, 'memberemail3', None) or fullname == getattr(teamObject, 'membername4', None) or email == getattr(teamObject, 'memberemail4', None):
    teamName = getattr(teamObject, 'title', None)
    if teamName:
      myTeams.append(teamName)
return myTeams
