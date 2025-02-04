# encoding: utf-8

from ckan.common import CKANConfig
from flask import Blueprint
from flask import render_template_string
from ckan.lib.base import render
import ckan.plugins as p

def homepage():
    return render('homepage.html', {})

def about():
    return render('home/about.html', {})

class CurveloThemePlugin(p.SingletonPlugin):
    '''
    An example IBlueprint plugin to demonstrate Flask routing from an
    extension.
    '''
    p.implements(p.IBlueprint)
    p.implements(p.IConfigurer)

    # IConfigurer

    def update_config(self, config: CKANConfig):
        # Add extension templates directory
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource("assets", "ckanext-curvelo")

    def get_blueprint(self):
        '''Return blueprints to be registered by the app.

        This method can return either a Flask Blueprint object or
        a list of Flask Blueprint objects.
        '''

        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = 'templates'
        # Add plugin url rules to Blueprint object
        rules = [
            ('/', 'homepage', homepage),
            ('/sobre', 'sobre', about),
        ]
        for rule in rules:
            blueprint.add_url_rule(*rule)

        return [blueprint]
