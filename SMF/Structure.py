__author__ = 'Daniel Bugl'
__copyright__ = "Copyright 2013, Daniel Bugl"
__credits__ = ["Daniel Bugl"]

__license__ = "BSD"
__version__ = "0.1.0"
__maintainer__ = "Daniel Bugl"
__email__ = "daniel.bugl@touchlay.com"
__status__ = "Prototype"


class SMFParameter:
    parameter_type = ""
    parameter_name = ""

    def __init__(self, parameter_type="", parameter_name=""):
        self.parameter_type = parameter_type
        self.parameter_name = parameter_name


class SMFModel:
    model_name = ""
    parameters = []

    def __init__(self, model_name="", parameters=()):
        self.model_name = model_name
        self.parameters = parameters