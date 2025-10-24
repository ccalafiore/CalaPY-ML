import datetime
import importlib

__version__ = '1.0.0'

__release_day__ = 23
__release_month_num__ = 10
__release_year__ = 2025


__release_date_object__ = datetime.date(__release_year__, __release_month_num__, __release_day__)
__release_date__ = __release_date_object__.__format__('%d %B %Y')
__release_month_name__ = __release_date_object__.__format__('%B')
del datetime

__author__ = 'Calafiore Carmelo'
__author_email__ = 'carmelo.calafiore@newcastle.ac.uk'
__maintainer_email__ = 'carmelo.calafiore@newcastle.ac.uk'

submodules = ['rl', 'sl']
others = []
__all__ = submodules + others

for sub_module_m in submodules:
    importlib.import_module(name='.' + sub_module_m, package=__package__)
