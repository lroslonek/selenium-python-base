class L10nException(Exception):

    def __init___(self, ex):
        Exception.__init__(self, "Localisation exception: {0}".format(ex))
        self.ex = ex
