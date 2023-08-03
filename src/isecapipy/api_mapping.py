"""This is a placeholder module docstring"""

from .response_models import response_models as ResponseModels
from .request_body_models import request_body_models as RequestModels


def placeholder():
    """This is a placeholder function to test importing structure"""
    return True


uris = {
    "AGENTS": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents"},
        "get": {
            "all": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents",
                "params": [
                    {"count": {"type": int, "default": 100}},
                    {"listening": {"type": bool, "default": True}},
                    {"name": {"type": str, "default": None}},
                    {"Start": {"type": int, "default": None}},
                ],
                "request_body": None,
                "return": ResponseModels.AgentDetail,
            },
            "one": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}",
                "params": None,
                "request_body": None,
                "return": ResponseModels.AgentDetail,
            },
            "status": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}/status",
                "params": None,
                "request_body": None,
                "return": ResponseModels.AgentStatus,
            },
        },
        "put": {
            "policy": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}/policy",
                "params": None,
                "request_body": RequestModels.Agents,
                "return": ResponseModels.SuccessCode,
            }
        },
        "delete": {
            "one": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}",
                "params": None,
                "request_body": RequestModels.Agents,
                "return": ResponseModels.SuccessCode,
            }
        },
        "post": None,
    },
    "Agent Deployments": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment"
        },
        "get": {
            "one": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/"
                "deployment/{agentdeployment ID}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.AgentDeploymentStatus,
            }
        },
        "post": {
            "one": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment",
                "params": None,
                "request_body": RequestModels.AgentDeployment,
                "response": ResponseModels.SuccessCode,
                # links to operations in header of response...
            }
        },
    },
    "Agent Tasks": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks"
        },
        "get": {
            "all": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/tasks",
                "params": None,
                "request_body": None,
                "response": ResponseModels.AgentPolicyTask,
            },
            "executedTask": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}"
                "/queuedTask",
                "params": None,
                "request_body": None,
                "response": ResponseModels.ExecutedTask,
            },
            "queuedTask": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}"
                "/queuedTask/{queuedTaskId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.QueuedTask,
            },
        },
        "post": {
            "checkin": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}"
                "/checkin",
                "params": None,
                "request_body": None,
                "response": ResponseModels.SuccessCode,
            },
            "taskById": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}"
                "/tasks/{taskId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.ExecutedTask,
            },
        },
        "delete": {
            "task": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}"
                "/queuedTask{queuedTaskId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.SuccessCode,
            }
        },
        "put": None,
    },
    "Asset Scan Templates": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/asset/scantemplates"
        },
        "get": {
            "templates": {
                "all": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/asset/scantemplates",
                    "params": [
                        {"count": {"type": int, "default": 10}},
                        {
                            "createdByMe": {"type": bool, "default": None}
                        },  # to be depracated soon
                        {"name": {"type": str, "default": None}},
                        {"start": {"type": int, "default": None}},
                    ],
                    "request_body": None,
                    "response": ResponseModels.ListAssetScanTemplate,
                },
                "one": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                        'asset/scantemplates/{id}",
                    "params": None,
                    "request_body": None,
                    "response": ResponseModels.NotImplementedModel,
                },
            },
            "UsedBy": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/asset/' \
                    'scantemplates/{id}/usedby",
                "params": None,
                "request_body": None,
                "response": ResponseModels.NotImplementedModel,
            },
        },
    },
    "Cloud Sync": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/cloudsync"
        },
        "get": {
            "activationKeys": {
                "all": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                        'cloudsync/activationkeys",
                    "params": None,
                    "request_body": None,
                    "response": ResponseModels.ListAgentActivationKey,
                },
                "one": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                        'cloudsync/activationkeys{keyId}",
                    "params": None,
                    "request_body": None,
                    "response": ResponseModels.AgentActivationKey,
                },
            },
            "consoles": {
                "all": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/cloudsync/consoles",
                    "params": None,
                    "request_body": None,
                    "response": (list, ResponseModels.ConsoleInformation),
                },
                "one": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                        'cloudsync/consoles/{consoleId}",
                    "parms": None,
                    "request_body": None,
                    "response": ResponseModels.ConsoleInformation,
                },
            },
            "policies": {
                "all": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/cloudsync/' \
                        'consoles/{consoleId}/policies",
                    "params": None,
                    "request_body": None,
                    "response": (list, ResponseModels.PolicyInformation),
                },
                "one": {
                    "href": "https://<consoleFQDN:port>/st/console/api/v1.0/cloudsync/' \
                        'consoles/{consoleId}/policies/{policyId}",
                    "params": None,
                    "request_body": None,
                    "response": ResponseModels.PolicyInformation,
                },
            },
        },
        "post": {
            "activationKeys": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                    'cloudsync/activationkeys",
                "params": None,
                "request_body": RequestModels.CloudSync,
                "response": ResponseModels.NotImplementedModel,
            }
        },
        "delete": {
            "activationKey": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                    'cloudsync/activationkeys/{keyId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.SuccessCode,
            }
        },
    },
    "Configuration": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/configuration"
        },
        "get": {
            "version": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/configuration/version",
                "params": None,
                "request_body": None,
                "response": ResponseModels.ConsoleVersions,
            }
        },
    },
    "Credentials": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials"
        },
        "get": {
            "credentials": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials",
                "params": {"name": {"type": str, "default": None}},
                "request_body": None,
                "response": (list, ResponseModels.UserCredential),
            },
            "credential": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                    'credentials/{credentialId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.UserCredential,
            },
            "credentialShare": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials/"
                "{credential id}/share",
                "params": None,
                "request_body": None,
                "response": list,
            },
            "serviceCrednetials": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/servicecredentials",
                "params": None,
                "request_body": None,
                "response": (list, ResponseModels.ServiceCredential)
                # ivanti docs don't say list here but most likely is
            },
            "serviceCredential": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/"
                "servicecredentials/{servicecredentialId}",
                "params": None,
                "request_body": None,
                "response": ResponseModels.ServiceCredential
                # ivanti docs don't say list here but most likely is
            },
        },
        "post": {
            "credentials": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials",
                "params": None,
                "request_body": RequestModels.Credentials,
                "response": ResponseModels.UserCredential,
            },
            "sessionCredentials": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/sessioncredentials",
                "params": None,
                "request_body": RequestModels.Password,
                "response": ResponseModels.NotImplementedModel,  # non in ivanti docs?
            },
            "credentialShare": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/' \
                    'credentials/{credential id}/share",
                "params": None,
                "request_body": RequestModels.CredentialsShare,
                "response": ResponseModels.UserCredential,
            },
            "credentialShareWithService": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/"
                "credentials/{credential id}/sharewithservice",
                "params": None,
                "request_body": None,
                "response": ResponseModels.SuccessCode,
            },
        },
        "put": {
            "cedential": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials/' \
                    '{credential id}",
                "params": None,
                "request_body": RequestModels.Credentials,
                "response": ResponseModels.SuccessCode,
            },
            "credentialShare": {
                "href": "https://<consoleFQDN:port>/st/console/api/v1.0/credentials/' \
                    '{credential id}/share",
                "params": None,
                "request_body": RequestModels.CredentialsShare,
                "response": ResponseModels.SuccessCode,
            },
        },
        "delete": {},
    },
    "distributionservers": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/distributionservers"
        }
    },
    "ipranges": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/ipranges"}
    },
    "deploymentconfigurations": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/linux/patch/"
            "deploymentconfigurations"
        }
    },
    "scanconfigurations": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/linux/patch/' \
                'scanconfigurations"
        }
    },
    "machinegroups": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/machinegroups"
        }
    },
    "machines": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/machines"}
    },
    "vendors": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/metadata/vendors"
        }
    },
    "operations": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/operations"
        }
    },
    "deployments": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/stconsole/api/v1.0/patch/deployments"
        }
    },
    "deploytemplates": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/deploytemplates"
        }
    },
    "downloads": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/downloads"
        }
    },
    "groups": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/groups"
        }
    },
    "patchmetadata": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/patchmetadata"
        }
    },
    "productlevelgroups": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/productlevelgroups"
        }
    },
    "scanTemplates": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/scanTemplates"
        }
    },
    "scans": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/patch/scans"
        }
    },
    "patches": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/patches"}
    },
    "policies": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/policies"}
    },
    "servicecredentials": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/servicecredentials"
        }
    },
    "sessioncredentials": {
        "base_url": {
            "href": "https://<consoleFQDN:port>/st/console/api/v1.0/sessioncredentials"
        }
    },
    "users": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/users"}
    },
    "virtual": {
        "base_url": {"href": "https://<consoleFQDN:port>/st/console/api/v1.0/virtual"}
    },
}
