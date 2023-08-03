from trytond.model import ModelSQL, ModelView, fields 
from datetime import date

from .Util.interest import Interest
from .Util.call_types import CallTypes

class Call(ModelSQL, ModelView):
    'Llamada'
    
    __name__ = 'sale.call'

    date = fields.Date('Date')
    description = fields.Char('Description')

    prospect_trace = fields.Many2One('sale.prospect_trace', 'Prospect trace')

    interest = fields.Selection(Interest.get_interest_levels(), 'Interest')
    call_type = fields.Selection(CallTypes.get_call_types(), 'Call type')

    @classmethod
    def default_date(cls):
        return date.today()