import twint


class TwitterParams:
    term_to_search = None
    user_to_exclude = None

    def __init__(self, term_to_search, user_to_exclude):
        self.term_to_search = term_to_search
        self.user_to_exclude = user_to_exclude

    def get_config(self):
        c = twint.Config()
        c.Search = self.term_to_search
        c.Pandas = True
        return c
