from odoo import http
import json

class Employee(http.Controller):
    @http.route("/website/departments", type='json', auth="public")
    def getEmployees(self, **kwargs):
        Department = http.request.env['hr.department']
        departments = Department.search([])
        
        department_data = [{
            'id': department.id,
            'name': department.name,
            'manager_name': department.manager_id.name if department.manager_id else '',
            'employees': [{'id': member.id, 'name': member.name} for member in department.member_ids]
        } for department in departments]
        
        return department_data
