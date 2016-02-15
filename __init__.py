import logging


my_logger = logging.getLogger('uno')

# {{{ Handlers
handler = logging.StreamHandler()

# }}}
# {{{ Formatters
formatter = logging.Formatter(
        '| %(name)-12s | %(levelname)-8s | %(message)s')

# }}}
# {{{ Attach Handlers and Formatters
handler.setFormatter(formatter)
my_logger.addHandler(handler)
# }}}
# {{{ Level Management
my_logger.setLevel(logging.DEBUG)
# }}}
