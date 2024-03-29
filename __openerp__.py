# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Zikzakmedia S.L. (http://zikzakmedia.com) All Rights Reserved.
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Currency Numeric Code",
    "version" : "1.0.1",
    "author" : "Zikzakmedia SL / Enterprise Objects Consulting",
    "website": "http://www.eoconsulting.com.ar",
    "license" : "AGPL-3",
    "category": "Accounting",
    "description": """
    Adds currency numeric codes (Ex, € is 978).
    """,
    'init_xml': [],
    "depends" : ["base"],
    'update_xml': [
        "settings/currency_numeric_data.xml",
        "currency_view.xml"
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
