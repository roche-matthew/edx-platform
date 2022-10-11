"""
This module contains various configuration settings via
waffle switches for the teams app.
"""

from edx_toggles.toggles import WaffleFlag

# .. toggle_name: learner_home_mfe.enabled
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to enable to redirect user to learner home mfe
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2022-10-11
# .. toggle_tickets: AU-879
ENABLE_LEARNER_HOME_MFE = WaffleFlag(
    'learner_home_mfe.enabled',
    __name__,
)
