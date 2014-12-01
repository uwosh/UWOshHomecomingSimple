## Script (Python) "getTeamMembers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=teamName
##title=
##
results = []
teamBrains = context.queryCatalog ({'portal_type':'HomecomingTeam', 'Title':teamName})
teamBrain = teamBrains[0]
teamObject = teamBrain.getObject()
fields = teamObject.Schema().viewableFields(teamObject)
memberFieldNames=[]
for field in fields:
    if field.getName().find('membername') <> -1:
        memberFieldNames.append(field.getName())
for memberFieldName in memberFieldNames:
    memberEmailFieldName = memberFieldName.replace('name','email')
    memberShirtSizeFieldName = memberFieldName.replace('name','shirt')
    fullname = getattr(teamObject, memberFieldName, None)
    email = getattr(teamObject, memberEmailFieldName, None)
    shirtsize = getattr(teamObject, memberShirtSizeFieldName, None)
    if fullname or email:
#         results.append('fullname')
#         results.append(fullname)
#         results.append('email')

#         results.append(email)
        results.append({'fullname':fullname, 'email':email, 'shirtsize':shirtsize})
return results
