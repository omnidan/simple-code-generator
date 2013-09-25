from SMF import SMFParser


class TestSMFParser:
    def test_name(self):
        assert self.result.model_name == "School"

    def test_parameter_string_type(self):
        assert self.result.parameters[0].parameter_type == "string"

    def test_parameter_string_name(self):
        assert self.result.parameters[0].parameter_name == "location"

    def test_parameter_int_type(self):
        assert self.result.parameters[1].parameter_type == "int"

    def test_parameter_int_name(self):
        assert self.result.parameters[1].parameter_name == "pupils_count"

    def __init__(self):
        self.parser = SMFParser(r"""
model School:
    string location
    int pupils_count
    int teacher_count
        """)
        self.result = self.parser.getResult()