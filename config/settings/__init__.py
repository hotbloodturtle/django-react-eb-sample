import os

SERVER_MODE = os.getenv('SERVER_MODE', 'LOCAL')
if SERVER_MODE == 'PROD':
    from .prod import *
else:
    from .local import *
