import sys

def choose_handler():
    handler = None

    if 'maya' in sys.executable:
        from handler.maya_handling import MayaHandler
        return MayaHandler()

    elif 'houdini' in sys.executable:
        from handler.houdini_handling import HoudiniHandler
        return HoudiniHandler()

    else: from handler.default_handling import DefaultHandler
    return DefaultHandler()

