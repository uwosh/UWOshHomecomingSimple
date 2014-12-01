# -*- coding: utf-8 -*-
#
# File: HomecomingSignupSheet.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """T. Kim Nguyen <nguyen@uwosh.edu> <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.UWOshHomecomingSimple.config import *

##code-section module-header #fill in your manual code here
from Products.CMFCore.utils import getToolByName
from zLOG import LOG, INFO, ERROR, WARNING
from Products.Archetypes.Registry import registerWidget

class URLWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro' : "urlstring",
        'size' : '30',
        'maxlength' : '255',
        'blurrable' : True,
        })

    security = ClassSecurityInfo()
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringWidget(
            label_msgid="label_title",
            i18n_domain="plone",
            visible={'view':'invisible'},
            label='Title',
        ),
        searchable=1,
        view="Manage portal",
        required=1,
        write_permission="Manage portal",
        accessor="Title"
    ),

    StringField(
        name='timeslot1',
        widget=URLWidget(
            label="Mon. Oct. 1 4:00-4:15 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot1',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot1"
    ),

    StringField(
        name='timeslot2',
        widget=URLWidget(
            label="Mon. Oct. 1 4:15-4:30 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot2',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot2"
    ),

    StringField(
        name='timeslot3',
        widget=URLWidget(
            label="Mon. Oct. 1 4:30-4:45 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot3',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot3"
    ),

    StringField(
        name='timeslot4',
        widget=URLWidget(
            label="Mon. Oct. 1 4:45-5:00 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot4',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot4"
    ),

    StringField(
        name='timeslot5',
        widget=URLWidget(
            label="Mon. Oct. 1 5:00-5:15 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot5',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot5"
    ),

    StringField(
        name='timeslot6',
        widget=URLWidget(
            label="Mon. Oct. 1 5:15-5:30 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot6',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot6"
    ),

    StringField(
        name='timeslot7',
        widget=URLWidget(
            label="Mon. Oct. 1 5:30-5:45 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot7',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot7"
    ),

    StringField(
        name='timeslot8',
        widget=URLWidget(
            label="Mon. Oct. 1 5:45-6:00 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot8',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot8"
    ),

    StringField(
        name='timeslot9',
        widget=URLWidget(
            label="Tues. Oct. 2 6:00-6:15 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot9',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot9"
    ),

    StringField(
        name='timeslot10',
        widget=URLWidget(
            label="Tues. Oct. 2 6:15-6:30 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot10',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot10"
    ),

    StringField(
        name='timeslot11',
        widget=URLWidget(
            label="Tues. Oct. 2 6:30-6:45 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot11',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot11"
    ),

    StringField(
        name='timeslot12',
        widget=URLWidget(
            label="Tues. Oct. 2 6:45-7:00 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot12',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot12"
    ),

    StringField(
        name='timeslot13',
        widget=URLWidget(
            label="Tues. Oct. 2 7:00-7:15 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot13',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot13"
    ),

    StringField(
        name='timeslot14',
        widget=URLWidget(
            label="Tues. Oct. 2 7:15-7:30 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot14',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot14"
    ),

    StringField(
        name='timeslot15',
        widget=URLWidget(
            label="Tues. Oct. 2 7:30-7:45 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot15',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot15"
    ),

    StringField(
        name='timeslot16',
        widget=URLWidget(
            label="Tues. Oct. 2 7:45-8:00 p.m.",
            label_msgid='UWOshHomecomingSimple_label_timeslot16',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('disallowValueModification',),
        searchable=1,
        edit_accessor="getRawTimeslot16"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

HomecomingSignupSheet_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class HomecomingSignupSheet(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Homecoming Signup Sheet'

    meta_type = 'HomecomingSignupSheet'
    portal_type = 'HomecomingSignupSheet'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'HomecomingSignupSheet.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Homecoming Signup Sheet"
    typeDescMsgId = 'description_edit_homecomingsignupsheet'

    _at_rename_after_creation = True

    schema = HomecomingSignupSheet_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def _getTeamNames (self):
#         catalog = getToolByName (self, 'portal_catalog')
#         query = {}
#         query["Type"] = "HomecomingTeam"
#         teams = catalog.searchResults (**query)
        teams = self.queryCatalog ({'portal_type':'HomecomingTeam'})
        teamNames = []
        for t in teams:
            o = t.getObject()
            #LOG ("setTimeslot", INFO, "Examining object %s" % str(o))
            if o:
                teamNames.append (o.title)
        #LOG ("setTimeslotNN", INFO, "Catalog query returned teams %s" % teamNames)
        return teamNames

    def setTimeslot1 (self, value):
        if getattr(self, 'timeslot1', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot1 = value
        else:
            raise ValueError, "timeslot1: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot2 (self, value):
        if getattr(self, 'timeslot2', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot2 = value
        else:
            raise ValueError, "timeslot2: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot3 (self, value):
        if getattr(self, 'timeslot3', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot3 = value
        else:
            raise ValueError, "timeslot3: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot4 (self, value):
        if getattr(self, 'timeslot4', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot4 = value
        else:
            raise ValueError, "timeslot4: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot5 (self, value):
        if getattr(self, 'timeslot5', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot5 = value
        else:
            raise ValueError, "timeslot5: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot6 (self, value):
        if getattr(self, 'timeslot6', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot6 = value
        else:
            raise ValueError, "timeslot6: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot7 (self, value):
        if getattr(self, 'timeslot7', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot7 = value
        else:
            raise ValueError, "timeslot7: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot8 (self, value):
        if getattr(self, 'timeslot8', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot8 = value
        else:
            raise ValueError, "timeslot8: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot9 (self, value):
        if getattr(self, 'timeslot9', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot9 = value
        else:
            raise ValueError, "timeslot9: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot10 (self, value):
        if getattr(self, 'timeslot10', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot10 = value
        else:
            raise ValueError, "timeslot10: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot11 (self, value):
        if getattr(self, 'timeslot11', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot11 = value
        else:
            raise ValueError, "timeslot11: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot12 (self, value):
        if getattr(self, 'timeslot12', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot12 = value
        else:
            raise ValueError, "timeslot12: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot13 (self, value):
        if getattr(self, 'timeslot13', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot13 = value
        else:
            raise ValueError, "timeslot13: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot14 (self, value):
        if getattr(self, 'timeslot14', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot14 = value
        else:
            raise ValueError, "timeslot14: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot15 (self, value):
        if getattr(self, 'timeslot15', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot15 = value
        else:
            raise ValueError, "timeslot15: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def setTimeslot16 (self, value):
        if getattr(self, 'timeslot16', None) == ''and value == '':
            return
        teamNames = self._getTeamNames()
        if value == '' or value in teamNames:
            self.timeslot16 = value
        else:
            raise ValueError, "timeslot16: '%s' is not the name of an existing homecoming team. Please use your browser's Back button then choose one of %s." % (value, str(teamNames))

    def _getTeamURL (self, teamName):
        if teamName == '':
            return ''
        teamNotFound = '<i>team %s not found</i>' % teamName
        teamBrains = self.queryCatalog ({'portal_type':'HomecomingTeam', 'Title':teamName})
        if not teamBrains or len(teamBrains) == 0:
            return teamNotFound
        teamBrain = teamBrains[0]
        team = teamBrain.getObject()
        if not team:
            return teamNotFound
        teamURL = team.absolute_url()
        return '<a href="%s">%s</a>' % (teamURL, teamName)

    def getTimeslot1 (self):
        return self._getTeamURL(self.getRawTimeslot1());

    def getRawTimeslot1 (self):
        try:
            return self.timeslot1
        except AttributeError:
            return ''

    def getTimeslot2 (self):
        return self._getTeamURL(self.getRawTimeslot2());

    def getRawTimeslot2 (self):
        try:
            return self.timeslot2
        except AttributeError:
            return ''

    def getTimeslot3 (self):
        return self._getTeamURL(self.getRawTimeslot3());

    def getRawTimeslot3 (self):
        try:
            return self.timeslot3
        except AttributeError:
            return ''

    def getTimeslot4 (self):
        return self._getTeamURL(self.getRawTimeslot4());

    def getRawTimeslot4 (self):
        try:
            return self.timeslot4
        except AttributeError:
            return ''

    def getTimeslot5 (self):
        return self._getTeamURL(self.getRawTimeslot5());

    def getRawTimeslot5 (self):
        try:
            return self.timeslot5
        except AttributeError:
            return ''

    def getTimeslot6 (self):
        return self._getTeamURL(self.getRawTimeslot6());

    def getRawTimeslot6 (self):
        try:
            return self.timeslot6
        except AttributeError:
            return ''

    def getTimeslot7 (self):
        return self._getTeamURL(self.getRawTimeslot7());

    def getRawTimeslot7 (self):
        try:
            return self.timeslot7
        except AttributeError:
            return ''

    def getTimeslot8 (self):
        return self._getTeamURL(self.getRawTimeslot8());

    def getRawTimeslot8 (self):
        try:
            return self.timeslot8
        except AttributeError:
            return ''

    def getTimeslot9 (self):
        return self._getTeamURL(self.getRawTimeslot9());

    def getRawTimeslot9 (self):
        try:
            return self.timeslot9
        except AttributeError:
            return ''

    def getTimeslot10 (self):
        return self._getTeamURL(self.getRawTimeslot10());

    def getRawTimeslot10 (self):
        try:
            return self.timeslot10
        except AttributeError:
            return ''

    def getTimeslot11 (self):
        return self._getTeamURL(self.getRawTimeslot11());

    def getRawTimeslot11 (self):
        try:
            return self.timeslot11
        except AttributeError:
            return ''

    def getTimeslot12 (self):
        return self._getTeamURL(self.getRawTimeslot12());

    def getRawTimeslot12 (self):
        try:
            return self.timeslot12
        except AttributeError:
            return ''

    def getTimeslot13 (self):
        return self._getTeamURL(self.getRawTimeslot13());

    def getRawTimeslot13 (self):
        try:
            return self.timeslot13
        except AttributeError:
            return ''

    def getTimeslot14 (self):
        return self._getTeamURL(self.getRawTimeslot14());

    def getRawTimeslot14 (self):
        try:
            return self.timeslot14
        except AttributeError:
            return ''

    def getTimeslot15 (self):
        return self._getTeamURL(self.getRawTimeslot15());

    def getRawTimeslot15 (self):
        try:
            return self.timeslot15
        except AttributeError:
            return ''

    def getTimeslot16 (self):
        return self._getTeamURL(self.getRawTimeslot16());

    def getRawTimeslot16 (self):
        try:
            return self.timeslot16
        except AttributeError:
            return ''



registerType(HomecomingSignupSheet, PROJECTNAME)
# end of class HomecomingSignupSheet

##code-section module-footer #fill in your manual code here
registerWidget(URLWidget,
               title='URLString',
               description=('Renders a HTML text input box which '
                            'accepts a single line of text and display a link'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##/code-section module-footer
