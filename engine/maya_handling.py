import maya.cmds as cmds

class MayaEngine():
    implements = ['save', 'open', 'reference']

    def open(self, path):
        cmds.file(path, open=True, f=True)

    def save(self):
        cmds.file(save=True)

    def reference(self, path):
        cmds.file(path, reference=True)
