from . import BaseFile
import yaml

class YamlFile(BaseFile):

    def __init__(self, github_file):
        super().__init__(github_file)
        yaml.add_representer(type(None), represent_none)

    def get_objects(self):
        if not self.objects:
            self.objects = list(yaml.safe_load_all(self.file_contents))
        return self.objects

    def dump(self):
        return yaml.dump_all(self.get_objects(), default_flow_style=False, explicit_start=True)

def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')
