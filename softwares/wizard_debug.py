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


def connect() -> bool:
    """Connect to the debugpy debugger.

    Returns:
        bool: Returns True if the connection to the debugpy debugger is \
            successful, False otherwise.

    Raises:
        ModuleNotFoundError: If the debugpy module is not found.
        ConnectionRefusedError: If the connection to the debugpy debugger \
            is refused.
    """
    try:
        import debugpy
    except ModuleNotFoundError as e:
        return False

    try:
        host = os.environ.get("WIZARD_DEBUGPY_HOST", "127.0.0.1")
        port = int(os.environ.get("WIZARD_DEBUGPY_PORT", "5679"))

        debugpy.connect((host, port))

        debugpy.wait_for_client()
    except ConnectionRefusedError as e:
        return False

    return True
