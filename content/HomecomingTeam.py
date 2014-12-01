# -*- coding: utf-8 -*-
#
# File: HomecomingTeam.py
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
            label="Team Name",
            visible={'view':'invisible'},
        ),
        required=1,
        accessor="Title",
        searchable=1
    ),

    StringField(
        name='membername1',
        widget=StringWidget(
            label="Member 1 Name",
            label_msgid='UWOshHomecomingSimple_label_membername1',
            i18n_domain='UWOshHomecomingSimple',
        ),
        searchable=1,
        default_method="setDefaultMemberName1"
    ),

    StringField(
        name='memberemail1',
        widget=URLWidget(
            label="Member 1 Email",
            label_msgid='UWOshHomecomingSimple_label_memberemail1',
            i18n_domain='UWOshHomecomingSimple',
        ),
        edit_accessor="getRawMemberEmail1",
        default_method="setDefaultMemberEmail1",
        searchable=1,
        validators=('isEmail', 'isEmailUWOsh')
    ),

    StringField(
        name='membershirt1',
        widget=SelectionWidget(
            label="Member 1 T-Shirt Size",
            label_msgid='UWOshHomecomingSimple_label_membershirt1',
            i18n_domain='UWOshHomecomingSimple',
        ),
        enforceVocabulary=1,
        vocabulary=['--choose one--','S','M','L','XL','XXL'],
        searchable=1
    ),

    StringField(
        name='membername2',
        widget=StringWidget(
            label="Member 2 Name",
            label_msgid='UWOshHomecomingSimple_label_membername2',
            i18n_domain='UWOshHomecomingSimple',
        ),
        searchable=1
    ),

    StringField(
        name='memberemail2',
        widget=URLWidget(
            label="Member 2 Email",
            label_msgid='UWOshHomecomingSimple_label_memberemail2',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('isEmail', 'isEmailUWOsh'),
        searchable=1,
        edit_accessor="getRawMemberEmail2"
    ),

    StringField(
        name='membershirt2',
        widget=SelectionWidget(
            label="Member 2 T-Shirt Size",
            label_msgid='UWOshHomecomingSimple_label_membershirt2',
            i18n_domain='UWOshHomecomingSimple',
        ),
        enforceVocabulary=1,
        vocabulary=['--choose one--','S','M','L','XL','XXL'],
        searchable=1
    ),

    StringField(
        name='membername3',
        widget=StringWidget(
            label="Member 3 Name",
            label_msgid='UWOshHomecomingSimple_label_membername3',
            i18n_domain='UWOshHomecomingSimple',
        ),
        searchable=1
    ),

    StringField(
        name='memberemail3',
        widget=URLWidget(
            label="Member 3 Email",
            label_msgid='UWOshHomecomingSimple_label_memberemail3',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('isEmail', 'isEmailUWOsh'),
        searchable=1,
        edit_accessor="getRawMemberEmail3"
    ),

    StringField(
        name='membershirt3',
        widget=SelectionWidget(
            label="Member 3 T-Shirt Size",
            label_msgid='UWOshHomecomingSimple_label_membershirt3',
            i18n_domain='UWOshHomecomingSimple',
        ),
        enforceVocabulary=1,
        vocabulary=['--choose one--','S','M','L','XL','XXL'],
        searchable=1
    ),

    StringField(
        name='membername4',
        widget=StringWidget(
            label="Member 4 Name",
            label_msgid='UWOshHomecomingSimple_label_membername4',
            i18n_domain='UWOshHomecomingSimple',
        ),
        searchable=1
    ),

    StringField(
        name='memberemail4',
        widget=URLWidget(
            label="Member 4 Email",
            label_msgid='UWOshHomecomingSimple_label_memberemail4',
            i18n_domain='UWOshHomecomingSimple',
        ),
        validators=('isEmail', 'isEmailUWOsh'),
        searchable=1,
        edit_accessor="getRawMemberEmail4"
    ),

    StringField(
        name='membershirt4',
        widget=SelectionWidget(
            label="Member 4 T-Shirt Size",
            label_msgid='UWOshHomecomingSimple_label_membershirt4',
            i18n_domain='UWOshHomecomingSimple',
        ),
        enforceVocabulary=1,
        vocabulary=['--choose one--','S','M','L','XL','XXL'],
        searchable=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

HomecomingTeam_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class HomecomingTeam(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Homecoming Team'

    meta_type = 'HomecomingTeam'
    portal_type = 'HomecomingTeam'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'HomecomingTeam.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Homecoming Team"
    typeDescMsgId = 'description_edit_homecomingteam'

    _at_rename_after_creation = True

    schema = HomecomingTeam_schema

    ##code-section class-header #fill in your manual code here
    actions =  (
        
       {'action': "string:${object_url}/base_view",
        'category': "object",
        'id': 'view',
        'name': 'view',
        #'permissions': (permissions.View,),
        'condition': ''
       },
       
       )

    ##/code-section class-header

    # Methods

    # Manually created methods

    def setDefaultMemberName1(self):
        pm = getToolByName (self, "portal_membership")
        m = pm.getAuthenticatedMember()
        return m.getProperty('fullname', "")

    def setDefaultMemberEmail1(self):
        pm = getToolByName (self, "portal_membership")
        m = pm.getAuthenticatedMember()
        return m.getProperty('email', "")

    def getMemberemail1 (self):
        return '<a href="mailto:' + self.memberemail1 + '">' + self.memberemail1 + '</a>'

    def getMemberemail2 (self):
        return '<a href="mailto:' + self.memberemail2 + '">' + self.memberemail2 + '</a>'

    def getMemberemail3 (self):
        return '<a href="mailto:' + self.memberemail3 + '">' + self.memberemail3 + '</a>'

    def getMemberemail4 (self):
        return '<a href="mailto:' + self.memberemail4 + '">' + self.memberemail4 + '</a>'

    def getRawMemberEmail1 (self):
        return self.memberemail1

    def getRawMemberEmail2 (self):
        return self.memberemail2

    def getRawMemberEmail3 (self):
        return self.memberemail3

    def getRawMemberEmail4 (self):
        return self.memberemail4



registerType(HomecomingTeam, PROJECTNAME)
# end of class HomecomingTeam

##code-section module-footer #fill in your manual code here
registerWidget(URLWidget,
               title='URLString',
               description=('Renders a HTML text input box which '
                            'accepts a single line of text and display a link'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##/code-section module-footer



