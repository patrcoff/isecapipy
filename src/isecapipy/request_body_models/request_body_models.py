"""The Pydantic Models for the ISEC REST API request bodies (JSON)"""

from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel

# AGENTS ------------------------------------------------------------


class Agents(BaseModel):
    """The REST API request body model for AGENTS
    Applies to DELETE and PUT requests"""

    policyId: Optional[str] = None
    checkIn: Optional[bool] = None


# AGENT DEPLOYMENTS -------------------------------------------------


class AgentDeployment(BaseModel):
    """The REST API request body model for Agent deployments
    Applies to POST requests"""

    assignedGroup: Optional[str] = None
    connectionMethod: Optional[str] = None  # ENUM
    credentialId: Optional[str] = None
    endpointNames: Optional[str] = None  # I assume this is actually a list...
    machineGroupIds: Optional[List[int]] = None
    policyId: str
    sshServerValidationMode: Optional[
        str
    ] = None  # Enum -  Blocked or SkipServerAuthentication
    useMachineCredentialId: Optional[bool] = None


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

    propogateUsagePolicy: Optional[str] = None  # ENUM - Throw, Overwrite
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
    protectionMode: Optional[
        str
    ] = None  # ENUM - None(default), Local DPApi, SessionKey
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

    description: Optional[str] = None
    options: Optional[LinuxPatchDerploymentOptions] = None
    name: str
    path: str


#  Linux Patch Groups  -------------------------------------------------


class LinuxPatches(BaseModel):
    """The REST API request body for linux patches"""

    errorPolicy: Optional[str] = None  #  ENUM Throw, Omit
    patchIds: List[str] = None  # GUIDS of the patches...


class LinuxCVEs(BaseModel):
    """The REST API request body for linux CVEs"""

    cves: List[str]  # cve ids, not names
    errorPolicy: Optional[str] = None  # ENUM- Throw, Omit


class LinuxPatchGroup(BaseModel):
    """The REST API  for Linux patch groups"""

    name: str
    path: Optional[str] = None


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

    description: Optional[str] = None
    filter: Optional[LinuxPatchScanFilter] = None  # required for PUT
    name: str
    path: Optional[str] = None


# Machine Groups --------------------------------------------------------


# Machines --------------------------------------------------------------


class DiscoveryFilterType(BaseModel):
    """The ENUM for the DiscoveryFilterType"""

    machineName: int = None
    domain: int = None
    ipRange: int = None
    ipAddress: int = None
    machineFile: int = None
    domainFile: int = None
    ipRangeFile: int = None
    ipAddressFile: int = None
    organizationalUnit: int = None
    nestedGroup: int = None
    virtualServerWilcard: int = None


class VMDiscoveryFilterType(DiscoveryFilterType):
    """The ENUM for the DiscoveryFilterType
    Used in the Machines model"""

    virtualServerCenterHostedOfflineSystem: int = None
    offlineDirectory: Optional[int] = None
    offlineImage: Optional[int] = None


class DiscoveryFilter(BaseModel):
    """The REST API request body for discovery filters
    Used in the Machines model"""

    adminCredentialId: Optional[str] = None
    category: DiscoveryFilterType
    containerCredentialId: Optional[str] = None
    includeChildOU: Optional[bool] = None
    isExcluded: Optional[bool] = None
    name: str
    notes: Optional[str] = None
    sshServerValidationMode: Optional[
        str
    ] = None  # ENUM - Blocked, SkipServerAuthentication


class ServerFilterTypes(BaseModel):
    """The ENUM for the ServerFilterTypes
    Used in the Machines model"""

    workstation: int = None
    server: int = None
    sqlServer: int = None
    domainController: int = None
    iisServer: int = None


class MachineGroup(BaseModel):
    """The REST API request body for machines
    Applies to DELETE, PUT"""

    connectionMethod: Optional[str] = None  # ENUM
    credentialId: Optional[str] = None
    description: Optional[str] = None
    discoveryFilters: DiscoveryFilter
    errorPolicy: Optional[str] = None  # ENUM - Throw, Omit
    name: str
    path: Optional[str] = None
    serverFilterTypes: Optional[ServerFilterTypes] = None
    virtualMachineDiscoveryFilters: Optional[VMDiscoveryFilterType] = None
