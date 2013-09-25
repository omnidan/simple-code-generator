from test_Parser import TestSMFParser


class TestSMFParserC(TestSMFParser):
    def __init__(self):
        self.document = r"""
struct School {
    string location;
    int pupils_count;
    int teacher_count;
};
        """
        super(TestSMFParserC, self).__init__()