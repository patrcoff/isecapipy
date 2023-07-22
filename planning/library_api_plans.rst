Library API Plans
=================

This document outlines the very early stage plans for how the library's API should be structured and function in user facing terms.
###################################################################################################################################

|

Firstly, I'd like to note how painfully aware I am of the potential for confusion between the terms API and REST API!
In this document, and the wider project more generally, I aim to diligently use the two terms consistently when talking about their respective meanings.

Where the two terms are referenced, please note their brief summary descriptions below for contextual understanding:

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| API       | This refers to the user interface API of the library itself, as in how developers using the library would be expected to do so.                                  |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REST API  | This refers to the actual calls or endpoints of the REST API of the ISEC console itself.                                                                         |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Endpoint  | This can also have two meanings but should be obvious from context. It can either mean a REST API endpoint (an individual uri available from the ISEC REST API)  |
|           | Or it could mean a physical or virtual hardware target such as a PC or Server, which is to be patched or otherwise managed via ISEC                              |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|

The basic usage of the library as I currently envision it is separated into the following sections:

- ISEC REST API references (built in documentation re-presenting the Ivanti documentation for Python users).
- ISEC REST API endpoint mappings - effectively what non Python people call a hash table and 1-1 function mappings to each of the endpoints' URIs as well as a function to generate the URIs.
- Simpler and higher level wrappers for each of the REST API's endpoint groups.
- Dataclasses for the endpoint JSON request bodies and responses.
- A simple query schema for ISEC data structures, processes and commands.
- Higher level workflow methods capable of combining multiple REST API calls to perform common ISEC workflows (using above query schema) to abstract use away from individual REST API endpoints.

|

Even with these higher level features and abstractions, ISEC and patching best practices should at all times be encouraged and the end user should also be directed into understanding fully what is happening at the console.
This is not just important for assisting efficient automation designs but in managing user expectations and ensuring they are kept realistic within what a console server is capable of within a given environment.

This will generally pull from my time as an Ivanti employee providing technical support for the product (though I am no longer employeed by Ivanti and this project has no association with Ivanti and receives no support or input from Ivanti itself).

|
|

Usage
-----

Starting with the REST API references - I envision including this as templated HTML which can view viewed from a CLI command if the package is installed
Of course, the library API for the mappings and wrapper methods will be documented with appropriate docstrings to assist in development when using the library, removing the need to separately reference the REST API docs or use the CLI command.

The mappings themselves will likely be referenced via a get_url_for() function or similar. I may implement them as a class but I feel the below might be cleaner usage:

|

Usage Example:
::

    import isecapipy

    ...

    isecapipy.get_url_for('agents',query=['name=myhostname'])

|

You might note I've left out the console FQDN which would be necessary in order to construct the full URL of an API endpoint.
While I don't plan on using module level global variables, I am currently thinking an environment variable might be best for holding this information.
We can then provide a module level function to set the CONSOLEFQDN env var if it needs to be done programatically within a script.
I don't see any issue with this direction, as it seems unlikely to me that peeople would want to write an automation targeting multiple ISEC consoles, but even if they did, they could simply change the env var on the fly as per above.

However, as I develop the rest of the library it may turn out to be of issue in the odd occurence where a context needs tracked within a script or automation for multiple consoles.
If this happens, I shall simply resolve this using kwargs in the get_url_for() function to allow the ablity to add backward compatible functionality (such as overriding the default envar based CONSOLEFQDN per call).

|
|

Moving on to the simple wrapper functions, this will provide a 1-1 function mapping to the individual endpoints.
It will however also include a slight amount more functionality (or abstraction) than the vanilla endpoint mappings or 'get_url_for' function.

This will likely be implemented with the following usage:
::

    import isecapipy

    ...

    api_handler = isecapipy.handler()
    agents_response = api_handler.get_agents()
    agents_query_response = api_handler.get_agents(name = 'myhostname')
    agent_task = api_handler.trigger_agent_checkin(name= 'myhostname')

|

In the above example you can see how you would instantiate a class of isecapipy.handler and use its methods to perform actions within ISEC via the available REST API endpoints.
Shown are two simple get requests which would map to individual REST API calls and one more complicated command to trigger a specific agent to check in.

Here we are now starting to stray into the realm of higher level abstractions as this task would actually require two individual REST API calls int the background.


As you can also see here, where as for the module level function to generate the url for a specific REST API endpoint we used a string as the full query parameter (or list of strings), here, this has been abstracted away providing a discrete variable parameter for each available query parameter relevant to the functions task.
This would be a simpler and more abstracted usage of querying for the end user than quoting the entire query parameter string and looks more Pythonic in my view.

This would then lead on to the notion of a query language or schema (I'm not really sure of what words to use to describe this) to make using the API feel even moe like using an ORM for example.

However, this more advanced concept may be left out of a 1.0.0 release for now, relying on simple method parameters for now. In fact, this may prove to be more than functional enough.

Also, for the notion of data classes for the JSON responses and request bodies - I envision this working very similarly to the requests module however it's likely there will be descrete classes for the different REST API endpoint specific JSON structures, rather than a module wide class.

They will likely inherit from a base class though to povide the same general functionality adding only the specific contextual functionality related to each endpoint's data structues.

Lastly, further high level workflows and abstactions would exist beyond the basic wrapper going beyond the scope of the individual REST API endpoints.

For example, a common task users of ISEC might wish to automate would be the automatic creation or modification of patch groups based on certain query parameters.

While this can be achieved manually in the console using Smart Filters, this is simply a filtered view of patches, and there is no console native method to automate updating a patch group with these filters. A user has to manually select all of the new matching patches, right click them and add them to a patch group.

Not a hugely laborious task of course, but one which still is open to human error or simply being forgotten about in a given month.

Replicating this via REST API calls however requires mutliple calls, loops and script side filtering of patches (unfortunately you cannot trigger the same backend SQL queries via the API as what run when a Smart Filter is viewed in the console).

This would generally be implimented in raw Python code as follows:
::

    import requests
    from requests_kerberos import HTTPKerberosAuth, OPTIONAL

    kerby = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
    ver = 'rootcert_may2023.cer'  # console STRootAuthority CA Certificate
    baseurl = 'https://CONSOLEFQDN:3121/st/console/api/v1.0/'

    url = f'{baseurl}metadata/vendors?count=1'    #  at time of writing, the .NET family is first in this response 
                                                  #  otherwise you'd need to be a little smarter here
    response = requests.get(url,auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),verify=False)

    for obj in response.json()['value'][0]['families'][0]['products']:
        #print(obj)
        if obj['name'] == ".NET 6.0":
            #print(obj['id'])
            prodversionid = obj['id']

    #--------------------

    url = f'{baseurl}patch/patchmetadata?sortOrder=Desc&orderBy=bulletinReleaseDate&productVersionids={prodversionid}&count=100'
    response = requests.get(url,auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),verify=False)

    for obj in response.json()['value']:
        if 'hosting' in obj['name'] :
            print(obj['kb'])
            patch = obj['kb']
            break # we only want the most recent hosting bundle patch so we can stop iterating now

    # then get patch id from kb

    url = f'{baseurl}patches?kbs={patch}'
    response = requests.get(url,auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),verify=False)

    patchid = response.json()['value'][0]['vulnerabilities'][0]['id']

    print(patchid) # THIS IS USED TO ADD TO A PATCH GROUP VIA THE REST API (can't use kb)

    url = f'{baseurl}patch/groups/2/patches'

    response = requests.post(url,auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),verify=False,json=[patchid])

    print(response)

    print(response.json())


|

This quick and dirty script calls the API endpoints required to obtain the '.NET 6.0' product family id, in order to obtain a list in reverse chronilogical order of patch metadata entries for patches in said family and adds them to a list if the patch name contains the word 'hosting'.
It then cycles through the patches endpoint to get the patch ids of said patches to be used in another script to add those patches to a patch group.

|

Yuck, clear as mud!!!

|

That's really the purpose of writing this library, to make the above look more like:
::

    import isecapipy
    handler = isecapipy.handler('myconsolecertificate.cer',auth=kerberos, consoleFQDN = 'uwm-isec-01.uwm.local')

    patches = handler.get_patches(family_name = '.NET 6.0', query = '"hosting" in name')

|

where sensible defaults exist such as orderBy=bulletinReleaseDate and sortOrder=Desc (I have no idea why this is not a default in the REST API itself) in context of the endpoints and data in question.

|

As previously mentioned, the 'query' functionality may be left for a future update to the library, and as such, there may be one or two more steps required if solely using function call parameter based querying per method targeting a given data structure or endpoint, but it would still be significantly cleaner than the raw code seen earlier:
::

    import isecapipy
    handler = isecapipy.handler('myconsolecertificate.cer',auth=isecapipy.KERBEROS, consoleFQDN = 'uwm-isec-01.uwm.local')

    product = handler.get_family(name = '.NET 6.0')
    patches = handler.get_patches(product=product.id)

    patch_list = [patch.kb for patch in patches if 'hosting' in patch.name]

|

Note, The stucture of the patch metadata JSON for example is highly nested [1] but the intention is to flatten this as much as possible in the public API usage.
This will result in some design decisions ommitting some 1-1 mappings of the REST API enpoints in the higher level wrapper methods of the public API but care will be taken to ensure broad coverage of use cases and sensible data structure choices based on what information users will actually be likely to need input and output of the API.

[1] see for example line 12 in the raw Python example from earlier:
::
    
    for obj in response.json()['value'][0]['families'][0]['products']:

|

That concludes my initial plans for this package, I hope the intended usage is nice and clear. Now on to implimentation!


Implimentation notes
====================

While it will be possible to generate the URL for any possible REST API query, most of the regular use of the library would be from the higher level wrapper functions which abstract individual REST API calls.

Each API endpoint's response will usually contain links to the related resources so generating links should not be necessary throughout many processes as the links will be obtained from each response.

The link generation would mainly be used as an entry point of a task and where querying is required at any level.

To assist with designing these entry and exit points where the endpoints will interlink, it might be useful to think of the endpoints as grouped broadly in the following way.

::

    Administrative and general config:

    Cloud Sync
    Configuration
    Credentials
    Distribution Servers and IP Ranges
    Users

    Patching related:

    Linux Patch Metadata
    Linux Patch Goup
    Linux Patch Deployment Configurations
    Linux Patch Scan Configurations

    Patches
    Patch Groups
    Patch Metadata
    Patch Scans
    Patch Scan Templates
    Product Level Groups
    Vendor Family Product Metadata
    Patch Downloads
    Patch Delpoyments
    Patch Deployment Templates

    Agents:

    Agents
    Agent Deployment
    Agent Tasks
    Policies

    Endpoints:

    Machines
    Machine Groups
    Virtual Infrastructure
    Asset Scan Templates ???

    Operation Management:

    Operations Controller
