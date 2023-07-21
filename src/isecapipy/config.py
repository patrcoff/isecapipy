"""Module configuration definitions"""

import os

class Config():
    """A class to generate a config object.
    Used to define connections to ISEC console and other defaults of module usage.
    """

    def __init__(self) -> None:

        self.fqdn = None
        self.fqdn_is_set = False
        self.set_fqdn()

    def set_fqdn(self,override=None):
        """Set the FQDN
        
        Optionally takes string argument override
        Defaults to env var FQDN"""

        if override.isinstance(str):
            self.fqdn = override
        else:
            try:
                self.fqdn = os.environ['FQDN']
                self.fqdn_is_set = True
            except KeyError:

                self.fqdn_is_set = False

    def set_auth(self,override=None):
        """Method to set REST API authentication

        Optionally accepts override dict of {'type','username', 'password'}
        Defaults to use of env vars 'ISEC'AUTH_TYPE' 'ISEC_USER' 'ISEC_PASSWORD'
        """
