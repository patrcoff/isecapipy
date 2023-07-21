import re

links = """
AGENTS 

https://<consoleFQDN:port>/st/console/api/v1.0/agents

DELETE

https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}

GET

https://<consoleFQDN:port>/st/console/api/v1.0/agents

https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agent ID}

https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agent ID}/status

PUT

https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentId}/policy

----------------------------------------------------------------------

AGENT DEPLOYMENTS

https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment

GET

https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment/{agentdeployment ID}

POST

https://<consoleFQDN:port>/st/console/api/v1.0/agents/deployment

----------------------------------------------------------------------

AGENT TASKS

https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks

DELETE

https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/queuedTask/{queuedTaskId}

GET

https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/tasks

https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/queuedTask

https://<consoleFQDN:port>/st/console/api/v1.0/agenttask/{agentId}/queuedTask/{queuedTaskId}

POST

https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/checkin

https://<consoleFQDN:port>/st/console/api/v1.0/agenttasks/{agentId}/tasks/{taskId}

----------------------------------------------------------------------"""

endpoints = links.split('----------------------------------------------------------------------')



def get_get(text):
    try:

        intermediary = text.split('GET')[1]
        sections_list = []

        for key in ['POST', 'PUT', 'DELETE']:
            if len(section := intermediary.split(key)[0]) > 0:
                try:
                    sections_list.append(section)
                except:
                    pass
        return sorted(sections_list, key = len)[0]
    
    except:
        pass

def get_post(text):
    pass

def get_put(text):
    pass

def get_delete(text):
    pass

#print(re.findall(r'^https.*$',links,re.MULTILINE))

print('GETS:')

for endpoint in endpoints:
    
    print(get_get(endpoint))
        #print(re.split(r'GET|POST|DELETE|PUT'),endpoint,re.MULTILINE)
        #print(re.findall(r'^https.*$',endpoint.split('GET')[1],re.MULTILINE))

        #print(f'\n\nfailed to regex on endpoint {endpoint}\n\n')