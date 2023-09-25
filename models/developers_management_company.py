# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class DevelopersManagementCompany(models.Model):
    _name = "developers.management.company"
    _description = "Companies to which developers are assigned"

    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address")
    developer_ids = fields.One2many(
        comodel_name="developers.management.developer",
        inverse_name="dev_company_id",
        string="Developers",
    )
