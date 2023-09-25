# -*- coding: utf-8 -*-

from odoo import api, fields, models 


class DevelopersManagementDeveloper(models.Model):
    _name = "developers.management.developer"
    _description = "Model with info about developers"

    name = fields.Char(
        string="Name",
        required=True,
    )
    type = fields.Selection(
        string="Type",
        selection=[
            ("front-end", "Front-end"),
            ("backend", "Backend"),
            ("fullstack", "Fullstack"),
            ("out-stuff", "Out-stuff"),
        ],
        required=True,
    )
    global_identification = fields.Char(
        string="Global Identification",
        compute="_compute_global_identification",
        store=True,
    )
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    birthdate = fields.Date(string="Birthdate")
    dev_company_id = fields.Many2one(
        comodel_name="developers.management.company",
        string="Company",
        required=False,
    )

    _sql_constraints = [
        ("uniq_developer_name", "unique(name)", "Such developer already exists")
    ]

    @api.depends("name", "type")
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = f"{developer.name or ''}-{developer.type or ''}"
