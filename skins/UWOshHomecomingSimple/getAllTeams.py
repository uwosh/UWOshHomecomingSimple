## Script (Python) "getAllTeams"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
teamBrains=context.queryCatalog({'portal_type':'HomecomingTeam'})
teamNames=[]
for teamBrain in teamBrains:
  team = teamBrain.getObject()
  teamName = getattr(team, 'title', None)
  if team and teamName:
    teamNames.append(teamName)
return teamNames
