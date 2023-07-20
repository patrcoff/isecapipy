Library API Plans
=================

This document outlines the very early stage plans for how the library's API should be structured and function in user facing terms.
###################################################################################################################################

|
|
|

The basic usage of the library as I currently envision it is separated into the following sections:

- ISEC REST API references (built in documentation re-presenting the Ivanti documentation for Python users)
- ISEC REST API endpoint mappings - what non Python people call a hash table effectively
- A simple wrapper for each of the REST API's endpoints
- Dataclasses for the endpoint JSON request bodies and responses.
- A simple query schema for ISEC data structures, processes and commands
- Higher level workflow methods capable of combining multiple API calls to perform common ISEC workflows (using above query schema) to abstract use away from individual REST API endpoints

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
If such issues appear in early development, I'll move this to a class (prior to a 1.0.0 release) but I'm hoping that won't be necessary.

If such issues appear after a 1.0.0 release, I shall look toward resolving it using kwargs in the get_url_for() function to allow the ablity to add backward compatible functionality (such as overriding the default envar based CONSOLEFQDN per call).

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

Replicating this via REST API calls however requires mutliple calls, loops and script side filtering of patches (unfortunately you cannot simply run the same SQL via the API which runs when a Smart Filter is viewed in the console).

This would generally be implimented in raw Python code as follows:
::

    import requests
    from requests_kerberos import HTTPKerberosAuth, OPTIONAL

    kerby = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
    ver = 'rootcert_may2023.cer'
    baseurl = 'https://CONSOLEFQDN:3121/st/console/api/v1.0/'

    url = f'{baseurl}metadata/vendors?count=1' # ASSUMING THE .NET FAMILY IS FIRST IN THE RESPONSE LIST!!!
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
            break # WE DONE

    # then get patch id from kb

    url = f'{baseurl}patches?kbs={patch}'
    response = requests.get(url,auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),verify=False)

    patchid = response.json()['value'][0]['vulnerabilities'][0]['id']

    print(patchid) # THIS IS USED TO ADD TO A PATCH GROUP

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
    handler = isecapipy.handler('myconsolecertificate.cer',auth=kerberos, consoleFQDN = 'uwm-isec-01.uwm.local')

    family = handler.get_family(name = '.NET 6.0')
    patches = handler.get_patches(family=family.id)

    patch_list = [patch.kb for patch in patches if 'hosting' in patch.name]


That concludes my initial plans for this package, I hope the intended usage is nice and clear. Now on to implimentation!