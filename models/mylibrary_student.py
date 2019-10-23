from odoo import models,fields,api
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class MylibraryStudent(models.Model):
    _name = 'mylibrary.student'

    name = fields.Char(required=True)

    @api.depends('date_of_birth')
    def calc_age(self):
        for record in self:
            if record.date_of_birth:
                d1 = date.today()
                d2 = datetime.strptime(record.date_of_birth, "%Y-%m-%d").date()
                record.age = relativedelta(d1,d2).years

    age = fields.Integer(compute=calc_age, store=True)
    date_of_birth = fields.Date()
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ])
    mobile_phone = fields.Char()
    mylibrary_borrower_ids = fields.One2many('mylibrary.borrow.by', 'student_id')
    state = fields.Char()
    city = fields.Char()
    street = fields.Char()
