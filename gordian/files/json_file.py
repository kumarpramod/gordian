from . import BaseFile
import json

class JsonFile(BaseFile):

    def __init__(self, github_file):
        super().__init__(github_file)

    def get_objects(self):
        if not self.objects:
            self.objects = json.loads(self.file_contents)
        return self.objects

    def dump(self):
        return json.dumps(self.get_objects(), indent=4)
