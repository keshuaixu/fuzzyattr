from fuzzywuzzy import process
import logging


def fuzzyattr(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, item):
            available_attributes = self.wrapped.__dict__.keys()
            closest_attribute = process.extractOne(item, available_attributes)
            logging.warning(
                'fuzzy attribute: You accessed \'{}\' but you probably meant \'{}\'.'.format(item, closest_attribute))
            return self.wrapped.__dict__[closest_attribute]
