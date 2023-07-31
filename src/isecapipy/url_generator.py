from .api_mapping import uris
from .response_models import response_models as ResponseModels
from .request_body_models import request_body_models as RequestModels

"""
function takes:
 endpoint name,
 sub_endpoint name,
 mult = True/False,
 method = one_of(GET,POST,PUT,DELETE)
 kwargs -> these will map to url params - should be validated against available params of selected endpoint URI

 """


# taking an endpoint name, method and mult args, can we determine in isolation each sub endpoint? probably not...
# so how would this be achieved


# yes this is a better way to structure the uris dict to specify individual uris more easily

# inspired by article on making better apis - don't repeat yourself in nesting, don't name functions with the module name etc
# no need for agents.agent etc


# first get endpoint and method:
#    if sub_endpoint exists, go into that next
#        if mult:
#            'all'
#            ...
#    if not:
#        if mult:
#            'all'
#            ...

# function default behaviours (can be overridden)
# if mult not included, and all/one availble in current branch of tree - choose all
# if method not included choose get first, do not attempt put/post/delete if not explicit
# if sub endpoint not provided, and multiple non all/one options available - select based on whether variables exist in url and kwarg matches...

# the function should have two paths, a happy and a sad:

# - the filter determines one unique URI (including using default biases)
# - the filter cannot determine one URI and raises an exception


# walk through the tree
# if method provided, filter by methods (these are all at the same level in the dict)
# ignore base_url
# extract all endpoint dicts - i.e. where the href is included
#
# if sub_endpoint provided, filter by all sub enpoints (on level after method and not one/all)
# if mult provided: filter out all 'all' items

# pass 2
# for remaining dicts
# if kwargs - filter out if kwargs not in params of dict or inside href ({})


def get_endpoints(urls, parents=[], depth=0):
    if urls:
        for key, val in urls.items():
            parents = parents[:depth]
            if key == "base_url":
                continue

            elif val and "href" in val.keys():
                parents.append(key)
                yield parents, val

            else:
                parents.append(key)
                for sub_parents, sub_item in get_endpoints(
                    val, parents=parents, depth=depth + 1
                ):
                    yield sub_parents, sub_item

    else:
        return


def select_uri(endpoint=None, method=None, sub_endpoint=None, mult=None, **kwargs):
    """This function attempts to return a unique URI for an ISEC REST API endpoint

    It takes in the string name of the endpoint, HTTP method, sub_endpoint, mult and kwargs
    It will then filter all available endpoints based on args provided and attempts to select one
    """

    endpoints = get_endpoints(urls=uris)

    if endpoint:
        endpoints = [x for x in endpoints if x[0][0] == endpoint]

    if method:
        endpoints = [x for x in endpoints if x[0][1] == method]

    if sub_endpoint:
        endpoints = [x for x in endpoints if x[0][2] == sub_endpoint]

    if mult == True:
        endpoints = [x for x in endpoints if "all" in x[0]]

    if mult == False:
        endpoints = [x for x in endpoints if "one" in x[0]]

    for key, val in kwargs:
        endpoints = [
            x
            for x in endpoints
            if (key in x[1]["href"] or key in x[1]["params"].keys())
        ]

    # after this point, we would ideally have a list of 1 URIs, and we can inject params if applicable

    return endpoints[0][1]["href"]
