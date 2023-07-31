from .api_mapping import uris


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
    It will then filter all available endpoints based on args provided and attempts to select one,
    injecting the relevant parameters into the returned uri.
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

    if len(endpoints) > 1:
        raise Exception(
            f"Unable to determine unique endpoint URI from provided "
            f"arguments:\n\n"
            f"endpoint={endpoint}\nmethod={method}\nsub_endpoint={sub_endpoint}"
            f"\nmult={mult}\nparameters={kwargs}"
        )

    return endpoints[0][1]["href"]
