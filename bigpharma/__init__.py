"""
bigpharma - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'bigpharma.schema'
    flow_module   = 'bigpharma.flow'
    javascripts   = [
        'js/bigpharma/routes.js',
        'js/opal/controllers/discharge.js',
        'js/bigpharma/controllers/cdr.js',
        'js/bigpharma/controllers/add_patient.js',
        'js/bigpharma/services/formulations.js',
        'js/bigpharma/services/patients.js'
    ]
