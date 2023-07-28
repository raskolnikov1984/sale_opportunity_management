# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields 

class ProspectTracker(ModelSQL, ModelView):
    'Seguimiento de un prospecto'
    
    __name__ = 'sale.prospect_tracker'

    prospect = fields.Many2One('sale.prospect', 'Prospect')
    prospect_name = fields.Char('Name')
    prospect_tel = fields.Integer('Tel')
    prospect_city = fields.Char('City') 

    calls = fields.One2Many('sale.call', 'prospect_tracker', "Calls")

    @fields.depends('prospect')
    def on_change_prospect(self):
        if self.prospect:
            self.prospect_name = self.prospect.name
            self.prospect_tel = self.prospect.tel
            self.prospect_city = self.prospect.city
