import argparse

class ArgumentHolder:
    """
    A thin wrapper around argparse.ArgumentParser class to hold argparse-type arguments.
    
    Call parse_args and this just acts like a common or garden argparse.ArgumentParser
    for use in a command line invocation.

    Can be imported into other python code to provide a method for introspection.
    For example, exposing the command line tool through a web form.
    The .args property is an array.
    """

    def __init__(self, description):
        self.args = []
        self.description = description

    def add_argument(self, *args, **kwargs):
        self.args.append((args, kwargs))

    def get_parser(self):
        """Return an ArgumentParser built from the class."""
        parser = argparse.ArgumentParser(description=self.description)
        for x in self.args:
            parser.add_argument(*x[0], **x[1])
        return parser

    def parse_args(self):
        """Act like an ArgumentParser"""
        return self.get_parser().parse_args()