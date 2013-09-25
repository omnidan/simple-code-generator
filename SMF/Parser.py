from __future__ import print_function
__author__ = 'Daniel Bugl'
__copyright__ = "Copyright 2013, Daniel Bugl"
__credits__ = ["Daniel Bugl"]

__license__ = "BSD"
__version__ = "0.1.0"
__maintainer__ = "Daniel Bugl"
__email__ = "daniel.bugl@touchlay.com"
__status__ = "Prototype"

from .Structure import *
import re


class SMFParser:
    def __parseDocument(self, smf):
        """ Parse an SMF document and return the content buffer """
        content_buffer = []  # buffer for the content lines
        # run through all lines
        for line in [line for line in smf.split('\n') if True]:
            content_buffer.append(line)
        return content_buffer

    # noinspection PyUnusedLocal
    def __matchSMF(self, line):
        """ Some regex magic to parse SMF commands """
        pass

    def __parse(self, smf):
        model_name = ""
        parse_buffer = []
        in_parameter_list = False
        for line in smf:
            # firstly, strip the line to remove whitespace
            line = line.strip()
            # check if the line is empty
            if line != "":
                # now check if comment
                if line[0] == '#':
                    # this is a comment, ignore
                    pass
                else:
                    parts = line.split(' ')
                    in_model_name = False
                    in_parameter = False
                    current_parameter = None
                    for part in parts:
                        part = part.strip()
                        if part != "":
                            if not in_parameter_list:
                                # parsing the model name
                                if in_model_name:
                                    model_name = part
                                    if model_name[-1] == ":":
                                        model_name = model_name[:-1]
                                    if model_name[-1] == "{":
                                        model_name = model_name[:-1]
                                    in_model_name = False
                                    in_parameter_list = True

                                # parsing the model syntax type
                                if not in_model_name and (part == "model" or part == "class" or part == "struct"):
                                    self.__model_type = part
                                    in_model_name = True
                            # parsing parameters
                            else:
                                # parsing parameter type
                                if not in_parameter:
                                    current_parameter = SMFParameter(part)
                                    in_parameter = True

                                # parsing parameter name
                                else:
                                    current_parameter.parameter_name = part
                                    if current_parameter.parameter_name[-1] == ";":
                                        current_parameter.parameter_name = current_parameter.parameter_name[:-1]
                    if current_parameter is not None:
                        parse_buffer.append(current_parameter)
        return model_name, parse_buffer

    def getResult(self):
        return self.__ld

    def __init__(self, smf, obj=None):
        self.__model_type = ""

        # parse document into content buffer
        content = self.__parseDocument(smf)

        # parse buffers into objects
        if obj is None:
            obj = SMFModel()
        self.__ld = obj
        self.__ld.model_name, self.__ld.parameters = self.__parse(content)