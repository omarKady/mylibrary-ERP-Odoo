from odoo import models,fields,api


class MylibraryPublisher(models.Model):
    _name = 'mylibrary.publisher'

    name = fields.Char(required=True)
    publisher_definition = fields.Text()
    mobile_phone = fields.Char()
    books = fields.One2many('mylibrary.book', 'publisher_id')
    country = fields.Char()
    state = fields.Char()
    city = fields.Char()
    street = fields.Char()

    def show_publisher_books(self):
        pub_books = []
        for book in self.books:
            pub_books.append(book.id)

        return {
            'name': 'Publisher Books Action',
            'type': 'ir.actions.act_window',
            'res_model': 'mylibrary.book',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', pub_books)],
        }
