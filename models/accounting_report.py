from openerp import models, fields, api, exceptions, _


class AccountReport(models.TransientModel):
    _inherit = "accounting.report"

    show_percent = fields.Boolean()
    left_and_right = fields.Boolean()

    @api.multi
    def check_report(self):
        res = super(AccountReport, self).check_report()
        self.ensure_one()
        res["data"]["show_percent"] = self.show_percent
        res["data"]["left_and_right"] = self.left_and_right
        return res
