{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Your name',
    'category': 'Theme/Creative',
    'assets': {
        'web.assets_frontend': [
            '/theme_tutorial/static/scss/style.scss',
            '/theme_tutorial/static/scss/primary_variables.scss',
            '/theme_tutorial/static/src/js/tutorial_editor.js',
            'theme_tutorial/static/src/scss/bootstrap_overridden.scss',
        ],
    },

    'depends': ['website'],
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],
}