import hou

class HoudiniHandler():
    implements = ['save', 'open', 'merge']

    def open(self, path):
        hou.hipFile.load(path, suppress_save_prompt=False, ignore_load_warnings=False)

    def save(self):
        hou.hipFile.save(file_name=None, save_to_recent_files=True)

    def reference(self, path):
        hou.hipFile.merge(path, node_pattern="*", overwrite_on_conflict=False, ignore_load_warnings=False)
