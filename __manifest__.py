{
    'name': 'mylibrary',
    'summary': 'Library Management System',
    'description': 'special system for library to make librarian work easy',
    'author': 'Omar Ahmed',
    'depends':['base'],
    'data': [
        'views/mylibrary_book_view.xml',
        'data/book_data.xml',
        'reports/report.xml',
        'reports/book_report_template.xml',
        'reports/publisher_report_template.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
    ],
}