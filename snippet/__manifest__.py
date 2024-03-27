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
    ],
    'assets': {
       'web.assets_frontend': [
           'snippet/static/src/snippets/s_employee/000.xml',
           'snippet/static/src/snippets/s_employee/000.js',
       ],
    },
    'application': True,
    'installable': True,
}
