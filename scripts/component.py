import bge

class Component(bge.types.KX_PythonComponent):
    def start(self, args):
        self.enabled = args['Enabled']

    def update(self, method):
        if self.enabled:
            method()