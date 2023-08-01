from .api_mapping import uris


class NonUniqueFilter(Exception):
    """Exception raised for URI filters not returning a unique URI.

    Attributes:
        params -- input parameters including kwargs
        message -- explanation of the error
    """

    def __init__(
        self, params, message="Insufficient arguments to identify unique URL!"
    ):
        self.params = params
        self.message = message
        super().__init__(f"self.message\n\n{params}")


class NoURIsFound(Exception):
    """Exception raised for URI filters not returning any URIs.

    Attributes:
        params -- input parameters including kwargs
        message -- explanation of the error
    """

    def __init__(self, params, message="Filters provided did not return any URIs!"):
        self.params = params
        self.message = message
        super().__init__(f"self.message\n\n{params}")


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


def inject_params():
    pass


def select_uri(endpoint=None, method=None, sub_endpoint=None, mult=None, **kwargs):
    """This function attempts to return a unique URI for an ISEC REST API endpoint

    It takes in the string name of the endpoint, HTTP method, sub_endpoint, mult and kwargs
    It will then filter all available endpoints based on args provided and attempts to select one,
    injecting the relevant parameters into the returned uri.
    """

    endpoints = [x for x in get_endpoints(urls=uris)]

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

    # -------------- END FILTERING VIA COMPREHENSIONS ------------------#
    # filtering now is selective instead of subtractive... this is important to note

    replacement = []

    for key, val in kwargs.items():
        for endp in endpoints:
            if key in endp[1]["href"]:
                replacement.append(endp)
            else:
                if "params" in endp[1].keys():
                    if endp[1]["params"]:
                        for param in endp[1]["params"]:
                            if key in param:
                                replacement.append(endp)
    if len(replacement) > 0:
        endpoints = replacement

    # after this point, we would ideally have a list of 1 URIs, and we can inject params if applicable

    if len(endpoints) == 1:
        return endpoints[0][1]["href"]

    elif len([x for x in endpoints]) > 1:
        names = [x[1]["href"] for x in endpoints]
        raise NonUniqueFilter(
            f"Unable to determine unique endpoint URI from provided "
            f"arguments:\n\n"
            f"endpoint={endpoint}\nmethod={method}\nsub_endpoint={sub_endpoint}"
            f"\nmult={mult}\nparameters={kwargs}"
            f"\n\nURIs remaining in filter:"
            f"{len(names)}"
        )

    else:
        raise NoURIsFound(
            f"No endpoints found matching applied filters: "
            f"arguments:\n\n"
            f"endpoint={endpoint}\nmethod={method}\nsub_endpoint={sub_endpoint}"
            f"\nmult={mult}\nparameters={kwargs}"
        )
