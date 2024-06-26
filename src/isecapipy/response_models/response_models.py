"""The Pydantic Models for the ISEC REST API responses"""

from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel

#  Shared ----------------------------------------------------------


class SuccessCode(BaseModel):
    """The REST API data model for SuccessCode"""

    code: int
    description: str


#  Agents ----------------------------------------------------------


class FrameworkVersion(BaseModel):
    """The REST API data model for FrameworkVersion (from AgentDetial->AgentStatus)"""

    major: int
    minor: int
    build: int
    revision: int
    majorRevision: int
    minorRevision: int


class AgentDetail(BaseModel):
    """The REST API data model for AgentDetail"""

    agentId: str
    assignedPolicyId: str
    dnsName: str
    domain: str
    frameworkVersion: str
    isListening: bool
    lastCheckIn: datetime
    lastKnownIPAddress: str
    links: Dict[str, Dict[str, str]]
    listeningPort: int
    machineName: str
    reportedPolicyId: str
    status: str  # is enum in docs


class AgentStatus(BaseModel):
    """The REST API data model for Agent Status"""

    agentId: str
    frameworkVersion: FrameworkVersion
    installedPackages: List[str]
    lastCheckIn: datetime
    links: Dict[str, Dict[str, str]]
    machineName: str
    reportedOn: datetime
    runningPolicyId: str  # guid
    runningPolicyVersion: int  # this says Uint32 in rest docs but probably fine


#  Agent Deployments -----------------------------------------------


class AgentDeployStatus(BaseModel):
    """The REST API data model for AgentDeployStatus
    Really annoyingly the isec docs use AgentStatus multiple times to mean different responses
    This is called AgentStatus in the agent deployments endpoint doc page, but has been changed
    to avoid clashing. There also seems to be a lot of redundancy in this endpoint..."""

    error: str | Dict[str, str]
    id: Optional[str] = None
    name: str
    percentComplete: int
    status: str
    statusTime: datetime


class AgentDeploymentStatus(BaseModel):
    """The REST API data model for Agent Deployment Status"""

    agentStatuses: List[AgentDeployStatus]
    created: datetime
    # Error: str | Dict[str,str]
    links: Dict[str, Dict[str, str]]
    percentComplete: int
    status: str


#  Agent Tasks -----------------------------------------------------


class AgentPolicyTask(BaseModel):
    """The REST API data model for Agent Policy Task"""

    agentId: str
    links: Dict[str, Dict[str, str]]
    taskId: str
    taskName: str
    taskType: str  # (enum)


class ExecutedTask(BaseModel):
    """The REST API data model for an executed Task"""

    agentId: str
    executingTaskId: str
    links: Dict[str, Dict[str, str]]


class AgentTaskState(BaseModel):
    """The REST API data model for an agent Task's state"""

    canCancel: bool
    commandLine: str
    endTime: datetime
    engineId: str
    hasArgument: bool
    identifier: str
    operationId: str
    startTime: datetime


class QueuedTask(BaseModel):
    """The REST API data model for a Queued Task"""

    agentId: str
    executingTaskId: str
    links: Dict[str, Dict[str, str]]
    taskStatus: AgentTaskState


#  Asset Scan Templates --------------------------------------------


class UsedBy(BaseModel):
    """The REST API data model for Used By - response of asset scan template: used by endpoint

    The response of the API endpoint contains a list of instances of this class."""

    name: str
    usageType: str  # EMUM


class AssetScanWmiOption(BaseModel):
    """The RESP API data model for asset scan WMI options"""

    category: str
    enabled: bool


class AssetScanTemplate(BaseModel):
    """The REST API data model for an asset scan template"""

    configurations: List[AssetScanWmiOption]
    creator: str
    description: str
    id: str
    includeHardwareAndWmiConfigurations: bool
    includeSoftware: bool
    isSystem: bool
    links: Dict[str, Dict[str, str]]
    name: str


class ListAssetScanTemplate(BaseModel):
    """The REST API returns a list of asset scan template objects in this form"""

    count: int
    links: Dict[str, Dict[str, str]]
    value: List[AssetScanTemplate]


#  Cloud Sync ------------------------------------------------------


class AgentActivationKey(BaseModel):
    """The REST API data model for cloud sync agent activation keys"""

    activationCountRemaining: int
    activationKey: str
    additionalProperties: Dict[str, str]
    consoleId: str
    consoleName: str
    consoleVersion: str
    createdBy: str
    initialActivationCount: int
    links: Dict[str, Dict[str, str]]
    notBefore: datetime
    notOnOrAfter: datetime
    policyId: str
    policyName: str


class ListAgentActivationKey(BaseModel):
    """The REST API returns a list of agent activation keys in this form"""

    # cannot repro in lab atm - need to register with cloud
    # likely contains count and links
    count: Optional[int] = None
    links: Optional[Dict[str, Dict[str, str]]] = None
    value: List[AgentActivationKey]


class ConsoleInformation(BaseModel):
    """The REST API data model for console information as returned by cloud sync API endpoint"""

    id: str
    links: Dict[str, Dict[str, str]]
    name: str
    version: str


class PolicyInformation(BaseModel):
    """The REST API data model for policy information as returned by cloud sync policies endpoint"""

    id: str
    links: Dict[str, Dict[str, str]]
    name: str


#  Configuration ---------------------------------------------------


class ConsoleVersions(BaseModel):
    """The REST API data model for console versions as returned by configuration api endpoint"""

    latestApiVersion: str
    productName: str
    productVersion: str


#  Credentials -----------------------------------------------------


class SessionCredential(BaseModel):
    """The REST API data model for the session credential endpoint response"""

    created: bool


class UserCredential(BaseModel):
    """The REST API data modelf for the credentials endpoint - user credentials"""

    id: str
    links: Dict[str, Dict[str, str]]
    name: str
    ownerName: str
    sharedWith: List[str]
    sharedWithService: bool
    username: str


class ServiceCredential(BaseModel):
    """The REST API data modelf for the credentials endpoint - service credentials"""

    id: str
    links: Dict[str, Dict[str, str]]
    name: str
    username: str

    # the Ivanti docs don't seem to show where this model is returned from
    # so will need to be confirmed in testing


class UserCredentialShares(BaseModel):
    """The REST API data model for the credentials endpoint - user credential shares"""

    propogateUsagePolicy: str  # ENUM
    propogateUsages: bool
    usernames: List[str]


# Distribution Servers and IP Ranges --------------------------------


class DistributionServers(BaseModel):
    """The REST API data model for Distribution servers"""

    autoSync: bool
    clientHttpPort: int
    clientPath: str  # URI
    clientSsl: bool
    clientType: str  # Enum(FileShare, AnonymousHttp, AuthenticatedHttp)
    id: int
    links: Dict[str, Dict[str, str]]
    name: str
    synchronizePath: str  # URI


class IPRange(BaseModel):
    """The REST API data model for IP ranges"""

    id: int
    links: Dict[str, Dict[str, str]]
    lowerBound: str  # ip address
    primaryServerId: int
    secondaryServerId: int
    upperBound: str  # ip address


# Linux Patch Deployment Configuration -------------------------------


class LinuxPatchDeploymentOptions(BaseModel):
    """The REST API data model for linux deployment options"""

    deploymentFilterType: str  # Enum
    patchGroupIds: List[int]
    shouldDeployOnlyExplicitVersion: bool
    shouldPostDeployReboot: bool


class LinuxPatchDeploymentConfiguration(BaseModel):
    """The REST API data model for linux deployment configs"""

    createdBy: str
    description: str
    id: str
    isSystem: bool
    links: Dict[str, Dict[str, str]]
    name: str
    options: LinuxPatchDeploymentOptions
    path: str


class LinuxPatchDeployUsedBy(BaseModel):
    """The REST API data model for linus deploy configs - used by"""

    name: str
    usageType: str  # Enum


# Linux Patch Groups -------------------------------------------------


class LinuxPatchGroup(BaseModel):
    """The REST API data model for linux patch groups"""

    id: str
    links: Dict[str, Dict[str, str]]
    name: str
    path: str  # path


class LinuxPatchLinks(BaseModel):
    """The REST API data model for Linux patch links"""

    links: Dict[str, Dict[str, str]]
    patchId: str


class LinuxPatchGroupUsedBy(BaseModel):
    """The REST API data model for Linux patch groups - used by"""

    name: str
    usageType: str  # Enum


# Linux Patch Metadata -----------------------------------------------


class LinuxPatchMetadata(BaseModel):
    """The REST API data model for Linux patch metadata"""

    cves: List[str]
    distribution: str  # Enum? Maybe a separate class not specified in Ivanti docs - needs tested
    issuedDate: datetime
    links: Dict[str, Dict[str, str]]
    name: str
    notifications: str
    packages: str
    # above is likely an undocumented data class - needs tested.
    # Architecture, name, packageUpdated, packageVersion, productId
    patchId: str
    patchTypeSeverity: str  # Enum
    platformEditions: str
    replacedBy: str
    requiresReboot: bool
    revisedDate: datetime


# Linux Patch Scan Configuration ------------------------------------


class LinuxPathScanFilter(BaseModel):
    """The REST API data model for Linux patch scan filter"""

    patchGroupIds: List[int]
    patchTypeSeverities: str  # Enum - None(0)
    # Enum - SecurityUnassigned(1)
    # Enum - SecurityCritical(2)
    # Enum - SecurityImportant(4)
    # Enum - SecurityModerate(8)
    # Enum - SecurityLow(16)
    # Enum - BugFix(32)
    # Enum - Enhancement(64)


class LinuxPatchScanConfiguration(BaseModel):
    """The REST API data model for Linux patch scan configuration"""

    createdBy: str
    description: str
    filter: LinuxPathScanFilter
    id: str
    isSystem: bool
    links: Dict[str, Dict[str, str]]
    name: str
    path: str


class LinuxPatchScanConfigUsedBy(BaseModel):
    """The REST API data model for Linux patch scan - used by"""

    name: str
    usageType: str  # Enum


# Machine Groups ----------------------------------------------------


class DiscoveryFilterType(BaseModel):
    """The REST API data model for discovery filter types"""

    machineName: int
    domain: int
    IpAddress: int
    IpRange: int
    machineFile: int
    domainFile: int
    IpRangeFile: int
    IpAddressFile: int
    organizationalUnit: int
    nestedGroup: int
    virtualServerWildcard: int


class DiscoveryFilters(BaseModel):
    """The REST API data model for discovery filters"""

    adminCredentialId: str
    category: DiscoveryFilterType
    containerCredentialId: str
    id: int
    IncludeChildOU: bool
    isExcluded: bool
    links: Dict[str, Dict[str, str]]
    name: str
    nestedGroupId: int
    notes: str


class VirtDiscoveryFilterType(DiscoveryFilterType):
    virtualServerCenterHostedOfflineSystem: int
    offlineDirectory: Optional[int]
    offlineImage: Optional[int]


class VirtualMachineDiscoveryFilter(BaseModel):
    """The REST API data model for virtual machine discovery filters"""

    adminCredentialId: str
    category: VirtDiscoveryFilterType
    id: int
    InventoryPath: str
    links: Dict[str, Dict[str, str]]
    note: str
    serverName: str


class ServerFilterTypes(BaseModel):
    workstation: int
    server: int
    sqlServer: int
    domainController: int
    printServer: int
    iisServer: int


class MachineGroup(BaseModel):
    connectionMethod: str  # Enum
    creator: str
    credentialId: str
    description: str
    discoveryFilters: List[DiscoveryFilters]
    id: str
    isBuiltIn: bool
    isReadOnly: bool
    links: Dict[str, Dict[str, str]]
    name: str
    path: str
    serverFilterTypes: List[ServerFilterTypes]
    virtualMachineDiscoveryFilters: List[VirtualMachineDiscoveryFilter]


# NOT IMPLIMENTED OR NEEDS TESTING (ISEC DOCS INCOMPLETE)


class NotImplementedModel:
    """A placeholder for models not yet implemented"""

    def __init__(self, *args, **kwargs) -> None:
        message = (
            f"You passed args and kwargs\n{args}\n{kwargs}"
            / "into a model which isn't implimented yet"
        )

        raise TypeError(message)
