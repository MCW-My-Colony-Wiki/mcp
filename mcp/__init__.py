#Load config
from .operate.config import load_config, config
config_data = load_config()

#Self check
from .internal_procedures.self_check import *

#Check update
if config_data['auto_update'] or config_data['check_update']:
	from .internal_procedures.update import check_update
	check_update(config_data['auto_update'])

del load_config, config_data

from .operate.source import *

__all__ = [
	'check_update',
	'config',
	'operate',
	'getpart',
	'getunit'
]
