import logging

logger = logging.getLogger(__name__)

class BaseFile:

    def __init__(self, github_file):
        self.github_file = github_file
        self.file_contents = github_file.decoded_content
        self.objects = None

    def get_objects(self):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError
