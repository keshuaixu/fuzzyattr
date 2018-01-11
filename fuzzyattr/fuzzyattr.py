from fuzzywuzzy import process
import logging


def fuzzyattr(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, item):
            try:
                return getattr(self.wrapped, item)
            except AttributeError:
                available_attributes = dir(self.wrapped)
                closest_attribute = process.extractOne(item, available_attributes)
                logging.warning(
                    'fuzzy attribute: You accessed \'{}\' but you probably meant \'{}\'.'.format(item, closest_attribute[0]))
                return getattr(self.wrapped, closest_attribute[0])

    return Wrapper
