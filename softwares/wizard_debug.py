# coding: utf-8
# Author: Mael PERON
# Contact: maelperon.cg@gmail.com

import os
import logging


logger = logging.getLogger(__name__)


def is_debugging() -> bool:
    """Fetch the debugging environment variable status.

    Returns:
        bool: Returns True if the debugging environment variable is \
            set to "1", False otherwise.
    """

    return os.environ.get("WIZARD_DEBUGPY", "0") == "1"
