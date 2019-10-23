from odoo import models,fields,api


class LibraryBorrowBy(models.Model):
    _name = 'mylibrary.borrow.by'

    @api.onchange('return_date','due_date')
    def borrow_book(self):
        self.available_books = 'not available'

    @api.onchange('returned')
    def returned_books(self):
        for rec in self:
            if rec.returned == 'returned':
                rec.available_books = 'available'

    student_id = fields.Many2one('mylibrary.student')
    book_id = fields.Many2one('mylibrary.book')
    available_books = fields.Selection([
        ('available', 'Available'),
        ('not available', 'Not Available'),
    ], related='book_id.available',store=True)
    due_date = fields.Date(required=True)
    return_date = fields.Date(required=True)
    returned = fields.Selection([
        ('returned', 'Returned'),
        ('not returned', 'Not Returned'),
    ], default='not returned')
