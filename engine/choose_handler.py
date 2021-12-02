import sys

def choose_handler():
    handler = None

    if 'maya' in sys.executable:
        from engine.maya_handling import MayaEngine
        return MayaEngine()

    elif 'houdini' in sys.executable:
        from engine.houdini_handling import HoudiniEngine
        return HoudiniEngine()
