"""This is a placeholder module docstring"""

def placeholder():
    """This is a placeholder function to test importing structure"""

    pass

urls = {
    'AGENTS': {
        'base_url': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents',
        'get':{
            'agents': {
                'href': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents',
                'params': ['count', 'listening', 'name', 'Start']
            },
            'agent': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agent ID}',
            'status': 'https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agent ID}/status'
        }
    }
}