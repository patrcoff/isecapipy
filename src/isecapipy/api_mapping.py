"""This is a placeholder module docstring"""

from pydantic import BaseModel, Opt
from datetime import datetime
from typing import Deque, List, Optional, Tuple, Dict

def placeholder():
    """This is a placeholder function to test importing structure"""

class Links(BaseModel):
    value: Dict[str, Dict[str, str]]

class AgentDetail(BaseModel):
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
    machineNme: str
    reportedPolicyId: str
    status: str  # is enum in docs

class AgentStatus(BaseModel):
    agentId: str
    frameworkVersion: str
    installedPackages: List[str]
    lastCheckIn: datetime
    links: Dict[str, Dict[str, str]]
    machineName: str
    reportedOn: datetime
    runningPolicyId: str  # guid
    runningPolicyVersion: int  # this says Uint32 in rest docs but probably fine

class SuccessCode(BaseModel):
    code: int
    description: str

#  Really annoyingly the isec docs use AgentStatus multiple times to mean different responses
#  This is called AgentStatus in the agent deployments endpoint doc page, but have changed to
#  avoid clashing. There also seems to be a lot of redundancy in this endpoint...
class AgentDeployStatus(BaseModel):
    error: str
    id: str
    name: str
    percentComplete: int
    status: str
    statusTime: datetime

class AgentDeploymentStatus(BaseModel):
    agentStatuses: AgentDeployStatus
    created: datetime
    Error: str
    links: Links
    percentComplete: int
    Status: str

class AgentPolicyTask(BaseModel):
    agentId: str
    links: Dict[str, Dict[str, str]]
    taskId: str
    taskName: str
    taskType: str  # (enum)

class ExecutedTask(BaseModel):
    agentId: str
    executingTaskId: str
    links: Dict[str, Dict[str, str]]

class AgentTaskState(BaseModel):
    canCancel: bool
    commandLine: str
    endTime: datetime
    engineId: str
    hasArgument: bool
    identifier: str
    operationId: str
    startTime: datetime

class QueuedTask(BaseModel):
    agentId: str
    executingTaskId: str
    links: Dict[str, Dict[str, str]]
    taskStatus: AgentTaskState




uris = {
    'AGENTS': {
        'base_url': {
            'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents'
            },
        'get': {
            'agents': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents',
                'params': [
                    {
                        'count': {
                            'type': int,
                            'default': 100
                        }
                    },
                    {
                        'listening': {
                            'type': bool,
                            'default': True
                        }
                    },
                    {
                        'name': {
                            'type': str,
                            'default': None
                        },
                        'Start': {
                            'type': int,
                            'default': None
                        }
                    }
                ],
                'return': AgentDetail # this needs expanded into a return data class
            },
            'agent': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}',
                'params': None,
                'return': AgentDetail # this needs expanded into a return data class
            },
            'status': {
                'href': 
                    'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}/status',
                'params': None,
                'return': AgentStatus # this needs expanded into a return data class
            }
        },
        'put': {
            'agent_policy': {
                'href': 
                    'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}/policy',
                'params': None,
                'request_body': {
                    'policyId': str,
                    'checkin': bool
                },
                'return': SuccessCode
            }
        },
        'delete': {
            'agent': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}',
                'params': None,
                'request_body': {
                    'policyId': str,
                    'checkin': bool
                },
                'return': SuccessCode
            }
        },
        'post': None
    },

    'Agent Deployments': {
        'base_url': {
            'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment'
        },
        'get': {
            'deployment': {
                'href': 
                    'https://<consoleFQDN:port>/st/console/api/v1.0/agents/'\
                    'deployment/{agentdeployment ID}',
                'params': None,
                'request_body': None,
                'response': AgentDeploymentStatus
            }
        },
        'post': {
            'deployment': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment',
                'params': None,
                'request_body': {
                    'assignedGroup': {
                        'required': False,
                        'type': str
                        },
                    'connectionMethod': {
                        'required': False,
                        'type': str  
                        # this is an Enum in the REST API docs so will likely add that later
                        },
                    'credentialId': {
                        'required': False,
                        'type': str
                        },
                    'endPointNames': {
                        'required': False,
                        'type': str
                        },
                    'machineGroupIds': {
                        'required': False,
                        'type': (list, int)  # a list of ints
                        },
                    'policyId': {
                        'required': True,
                        },
                    'sshServerValidationMode': {'required': False},
                    'useMachineCredentialId': {'required': False}
                },
                'response': SuccessCode  # links to operations in header of response...
            }
        }
    },
    'Agent Tasks': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks'},
        'get': {
            'tasks': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/tasks',
                'params': None,
                'request_body': None,
                'response': AgentPolicyTask
                },
            'executedTask': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/queuedTask',
                'params': None,
                'request_body': None,
                'response': ExecutedTask
                },
            'queuedTask': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/queuedTask/{queuedTaskId}',
                'params': None,
                'request_body': None,
                'response': QueuedTask
                }
            },
        'post': {
            'checkin': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/checkin',
                'params': None,
                'request_body': None,
                'response': SuccessCode
                },
            'taskById': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/tasks/{taskId}',
                'params': None,
                'request_body': None,
                'response': ExecutedTask
                }
            },
        'delete': {
            'task': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/queuedTask/{queuedTaskId}',
                'params': None,
                'request_body': None,
                'response': SuccessCode
                }
            },
        'put': None
    },
    'Asset Scan Templates': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/asset/scantemplates'}
    },
    'Cloud Sync': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/cloudsync'}
    },
    'Configuration': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/configuration'}
    },
    'Credentials': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/credentials'}
    },
    'distributionservers': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/distributionservers'}
    },
    'ipranges': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/ipranges'}   
    },
    'deploymentconfigurations': {
        'base_url': {
            'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/linux/patch/deploymentconfigurations'
        }
    },
    'scanconfigurations': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/linux/patch/scanconfigurations'}
    },
    'machinegroups': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/machinegroups'}
    },
    'machines': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/machines'}
    },
    'vendors': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/metadata/vendors'}
    },
    'operations': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/operations'}
    },
    'deployments': {
        'base_url': {'href': 'https://<consoleFQDN:port>/stconsole/api/v1.0/patch/deployments'}
    },
    'deploytemplates': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/deploytemplates'}
    },
    'downloads': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/downloads'}
    },
    'groups': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/groups'}
    },
    'patchmetadata': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/patchmetadata'}
    },
    'productlevelgroups': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/productlevelgroups'}
    },
    'scanTemplates': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/scanTemplates'}
    },
    'scans': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patch/scans'}
    },
    'patches': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/patches'}
    },
    'policies': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/policies'}
    },
    'servicecredentials': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/servicecredentials'}
    },
    'sessioncredentials': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/sessioncredentials'}
    },
    'users': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/users'}
    },
    'virtual': {
        'base_url': {'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/virtual'}
    }
}
