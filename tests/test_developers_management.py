# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from psycopg2.errors import UniqueViolation

class TestDevelopersManagement(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Developer = self.env["developers.management.developer"]
        self.Company = self.env["developers.management.company"]

    def test_1_create_developer(self):
        developer_data = {
            "name": "Ihor Ramskyi",
            "type": "backend",
            "phone": "0123465789",
            "email": "noreply@gmail.com",
        }
        developer = self.Developer.create(developer_data)
        self.assertTrue(developer)
        self.assertEqual(developer.global_identification, "Ihor Ramskyi-backend")

    def test_2_same_name_developer(self):
        developer_data = {
            "name": "Nevil Longbottom",
            "type": "front-end",
            "phone": "0123465789",
            "email": "noreply@gmail.com",
        }
        developer = self.Developer.create(developer_data)
        self.assertTrue(developer)
        try:
            developer2 = self.Developer.create(developer_data)
        except UniqueViolation:
            pass

    def test_3_create_company(self):
        company_data = {
            "name": "Generic Company",
            "address": "Generic Street",
        }
        company = self.Company.create(company_data)
        self.assertTrue(company)

    def test_4_link_developer_to_company(self):
        developer_data = {
            "name": "Good Fella",
            "type": "out-stuff",
            "phone": "9876543210",
            "email": "gmail@goodfella.com",
        }
        developer = self.Developer.create(developer_data)

        company_data = {
            "name": "Nice Company",
            "address": "Very Nice Street",
        }
        company = self.Company.create(company_data)

        developer.write({"dev_company_id": company.id})
        self.assertEqual(developer.dev_company_id, company)
        self.assertEqual(len(company.developer_ids), 1)
        self.assertIn(developer, company.developer_ids)
