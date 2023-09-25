# -*- coding: utf-8 -*-

{
    "name": "Developers Management",
    "version": "16.0",
    "summary": "Module for Managing Developers",
    "description": """
The "Developers Management" module, suited for easing working processes with developers.
     """,
    "author": "Ihor Ramskyi",
    "website": "",
    "license": "",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/developers_management_developer.xml",
        "views/developers_management_company.xml",
        "views/menu.xml",
    ],
    "test": [
        "tests/test_developers_management.py",
    ],
}
