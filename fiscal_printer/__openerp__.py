#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Eduardo Ochoa    <eduardo.ochoa@clusterbrands.com.ve>
#                               <elos3000@gmail.com>
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
{
    'name' : "Fiscal Printer",
    'category' : "Test",
    'version' : "1.0",
    'depends':['l10n_ve_fiscal_requirements'],
    'author' : "Me",
    'description' : """Fiscal Printer""",
    'init_xml': [
        'data/http_helper_data.xml'
     ],
    'data' : [        
        'view/pos_fiscal_printer_view.xml',
        'view/pos_fiscal_printer_action_menu.xml',
    ],
}
