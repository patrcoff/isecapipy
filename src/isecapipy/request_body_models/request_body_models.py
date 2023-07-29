"""The Pydantic Models for the ISEC REST API request bodies (JSON)"""

from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel, Optional

# AGENTS ------------------------------------------------------------


class Agents(BaseModel):
    """The REST API request body model for AGENTS
    Applies to DELETE and PUT requests"""

    policyId: Optional[str]
    checkIn: Optional[bool]


# AGENT DEPLOYMENTS -------------------------------------------------


class AgentDeployment(BaseModel):
    """The REST API request body model for Agent deployments
    Applies to POST requests"""

    assignedGroup: Optional[str]
    connectionMethod: Optional[str]  # ENUM
    credentialId: Optional[str]
    endpointNames: Optional[str]  # I assume this is actually a list...
    machineGroupIds: Optional[List[int]]
    policyId: str
    sshServerValidationMode: Optional[
        str
    ]  # Enum -  Blocked or SkipServerAuthentication
    useMachineCredentialId: Optional[bool]


# AGENT TASKS -------------------------------------------------------

# N/A

# Asset Scan Templates ----------------------------------------------

# N/A

# Cloud Sync --------------------------------------------------------


class CloudSync(BaseModel):
    """The REST API request body model for Cloud syncs.
    Applies to POST requests"""

    additionalProperties: Optional[Dict[str, str]]
    consoleId: str
    initialActivationCount: int
    notOnOrAfter: datetime
    policyId: str


# Configuration -----------------------------------------------------

# N/A

# Credentials -------------------------------------------------------


class CredentialsShare(BaseModel):
    """The REST API request body for credentials - share body
    Applies to DELETE, POST and PUT"""

    propogateUsagePolicy: Optional[str]  # ENUM - Throw, Overwrite
    propogateUsages: bool
    shareWithService: bool
    usernames: List[str]


class SessionKey(BaseModel):
    """The REST API request body parametr for SessionKey
    Used by the Password model in Credential requests"""

    algorithmIdentifier: str  # e.g. AES
    encryptedKey: str  # base64 RSA-encrypted session key ??
    iv: str  # base64-encoded, unencrypted initialization vecotr...
    # I will need to do some further research to figure out how to use this...


class Password(BaseModel):
    """The REST API request body for Passwords"""

    cipherText: str
    clearText: str
    protectionMode: Optional[str]  # ENUM - None(default), Local DPApi, SessionKey
    sessionKey: SessionKey


class Credentials(BaseModel):
    """The REST API request body for credentials
    Applies to POST, PUT"""

    name: str
    password: Password


# Distribution Servers and IP Ranges ---------------------------------

# N/A

# Linux Patch Deployment Configuration -------------------------------


class LinuxPatchDerploymentOptions(BaseModel):
    """The REST API request body for linux deployment options
    Used in main request body of endpoint"""

    deploymentFilterType: str  # Enum
    patchGroupIds: List[int]
    shouldDeployOnlyExplicitVersion: bool
    shouldPostDeployReboot: bool

    # The above is the same as ResponseModels.LinuxPatchDeploymentOptions
    # Duplicating in case later circular imports occurred from importing
    # the response models here


class LinuxDeployConfig(BaseModel):
    """The REST API request body for linux deployment configs.
    Used by POST, PUT"""

    description: Optional[str]
    options: Optional[LinuxPatchDerploymentOptions]
    name: str
    path: str


#  Linux Patch Groups  -------------------------------------------------


class LinuxPatches(BaseModel):
    """The REST API request body for linux patches"""

    errorPolicy: Optional[str]  #  ENUM Throw, Omit
    patchIds: List[str]  # GUIDS of the patches...


class LinuxCVEs(BaseModel):
    """The REST API request body for linux CVEs"""

    cves: List[str]  # cve ids, not names
    errorPolicy: Optional[str]  # ENUM- Throw, Omit


class LinuxPatchGroup(BaseModel):
    """The REST API  for Linux patch groups"""

    name: str
    path: Optional[str]


# Linux Patch Metadata --------------------------------------------------

# N/A

# Linux Patch Scan Configuration ----------------------------------------


class LinuxPatchScanFilter(BaseModel):
    """The REST API request body for linux patch scan filters"""

    patchGroupIds: List[int]  # ids of patch groups
    patchTypeSeverities: str  # ENUM - None(0)
    # SecurityUnassigned(1)
    # SecurityCritical(2)
    # SecurityImportant(4)
    # SecurityModerate(8)
    # SecurityLow(16)
    # BugFix(32)
    # Enhancement(64)
    # It is not clear from Ivanti docs if this is the text or number
    # Will need confirmed during models testing


class LinuxPatchScanConfig:
    """The REST API request body for Linux patch scan configs
    Applies to Post, PUT"""

    description: Optional[str]
    filter: Optional[LinuxPatchScanFilter]  # required for PUT
    name: str
    path: Optional[str]
