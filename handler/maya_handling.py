import maya.cmds as cmds

class MayaHandler():
    implements = ['Save', 'Open', 'Reference']

    def open(self, path):
        cmds.file(path, open=True, f=True)

    def save(self):
        cmds.file(save=True)

    def reference(self, path):
        cmds.file(path, reference=True)
