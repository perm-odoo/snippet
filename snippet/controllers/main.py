from odoo import http
import json

class Employee(http.Controller):
    @http.route("/website/departments", type='json', auth="public")
    def getEmployees(self, dept_id):
        Department = http.request.env['hr.department']
        
        if int(dept_id) != -1:
            department = Department.search([('id', '=', dept_id)], limit=1)
            if department:
                department_data = [{
                    'id': department.id,
                    'name': department.name,
                    'manager_name': department.manager_id.name if department.manager_id else '',
                    'employees': [{'id': member.id, 'name': member.name} for member in department.member_ids]
                }]
                
                return department_data
            else:
                return []
        else:
            departments = Department.search([])
            department_data = [{
                'id': department.id,
                'name': department.name,
                'manager_name': department.manager_id.name if department.manager_id else '',
                'employees': [{'id': member.id, 'name': member.name} for member in department.member_ids]
            } for department in departments]
            return department_data