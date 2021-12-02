class DefaultHandler():
    implements = ['Save', 'Open', 'Reference']

    def open(self, path):
        print("open!")

    def save(self):
        print("save!")

    def reference(self, path):
        print("reference!")
