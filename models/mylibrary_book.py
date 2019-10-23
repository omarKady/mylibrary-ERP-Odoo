from odoo import models,fields,api


class LibraryBook(models.Model):
    _name = 'mylibrary.book'

    name = fields.Char()
    available = fields.Selection([
        ('available','Available'),
        ('not available','Not Available'),
    ],default='available')
    description = fields.Text('Book Description')
    publication_date = fields.Date()
    author = fields.Char()
    type = fields.Selection([
        ('science','Science'),
        ('history','History'),
        ('philosophy','Philosophy'),
        ('psychology','psychology'),
        ('medicine','Medicine'),
        ('geography','Geography'),
        ('civilization','Civilization'),
        ('literature','Literature'),
    ])
    price = fields.Float()
    pages = fields.Integer()
    publisher_id = fields.Many2one('mylibrary.publisher', string='Publisher')
    publisher_def = fields.Text(related='publisher_id.publisher_definition', store=True, readonly=True)
    borrower_ids = fields.One2many('mylibrary.borrow.by', 'book_id')

