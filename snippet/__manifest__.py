{
    'name': 'Employee Snippet',
    'summary': 'Employee Snippet',
    'depends': [
        'base',
        'website',
        'hr',
    ],
    'data' : [
        'views/snippet.xml',
        'views/options.xml',

    ],
    'assets': {
       'web.assets_frontend': [
           'snippet/static/src/snippets/s_employee/000.xml',
           'snippet/static/src/snippets/s_employee/000.js',
           'snippet/static/src/snippets/s_employee/000.scss',
       ],
       'website.assets_wysiwyg' :[
            'snippet/static/src/snippets/s_employee/options.js',
        ]
    },
    'application': True,
    'installable': True,
}
