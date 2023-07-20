Library API Plans
=================

This document outlines the very early stage plans for how the libraries API should be structured and function in user facing terms.
###################################################################################################################################

The basic usage of the library as I currently envision it is separated into the following sections:

- ISEC REST API references (built in documentation re-presenting the Ivanti documentation)
- ISEC REST API endpoint mappings - what non Python people call a hash table effectively
- A simple wrapper for each of the REST API's endpoints
- Dataclasses for the endpoint JSON request bodies and responses.
- A simple query schema for ISEC data structures, processes and commands
- Higher level workflow methods capable of combining multiple API calls to perform common ISEC workflows (using above query schema) to abstract use away from individual REST API endpoints

Even with these higher level features and abstractions, ISEC and patching best practices should at all times be encouraged and the end user should also be directed into understanding fully what is happening at the console.
This is not just important for assisting efficient automation designs but in managing user expectations and ensuring they are kept realistic within what a console server is capable of within a given environment.

This will generally pull from my time as an Ivanti employee providing technical support for the product (though I am no longer employeed by Ivanti and this project has no association with Ivanti and receives no support or input from Ivanti itself).