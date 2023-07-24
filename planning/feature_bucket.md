# Feature Bucket

In this document we shall simply list desired features for consideration for inclusion within the project.

While we may add some descriptive information and general notes, it is not the purpose of this doc to thoroughly 
plan or schdeule features accepted for development, or prioritise or order them in any strict way.

-----

## Basic List for 1.0.0 release



The below list of features should take us well up to a 1.0.0 release.

- [] One-to-one mapping of REST API endpoint URIs  ==In Progress==
- [] URI generator based on endpoing and params with basic validation
- [] Data models (pydantic) of request bodies
- [] Data models (pydantic) of response objects  ==In Progress==
- [] Package level functions for each REST API method available per endpoint
- [] Class for Agent
- [] Class for Agent policy
- [] Class for Machine
- [] Class for patch (including patch metadata)
- [] Class for scan template
- [] Class for deployment template
- [] Class for deployment (may consolidate with above)
- [] Class for operations controller
- [] Class for query handler (to return multiples of above objects based on provided params and filters)


----

## Future consideration

- [] SQL query handler (direct connection to isec db for requests slow over REST API)
- [] 