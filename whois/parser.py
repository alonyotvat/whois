from . import parsers


class Parser:
    '''
    '''
    def __init__(self):
        pass

    def parse(self, raw_whois):
        '''
        '''
        parsed_data = parsers.parser.Parser.parse(raw_whois)

        if parsed_data:
            return parsed_data

        return None