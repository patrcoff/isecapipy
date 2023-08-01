"""This module provides functionality required in generating URIs based on user given parameters."""

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
    """This function generates individual endpoints from the uris dict."""

    if urls:
        for key, val in urls.items():
            parents = parents[:depth]
            if key == "base_url":
                continue

            if val and "href" in val.keys():
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


def inject_params(endp, kwargs):
    """This function takes in the selected uri and injects uri parameters."""
    generated_uri = endp["href"]
    for key, val in kwargs.items():
        if f"{{key}}" in endp["href"]:
            endp["href"].replace(key, val)
            endp["href"].replace("{", "")
            endp["href"].replace("}", "")
        if endp["params"]:
            if "?" not in generated_uri:
                generated_uri += "?"
            for param in endp["params"]:
                if key in param:
                    if (
                        "=" in generated_uri
                    ):  # if there is already at least one url param
                        generated_uri += "&"  # then you need to separate them with &
                    generated_uri += f"{key}={val}"

    return generated_uri


def generate_uri(endpoint=None, method=None, sub_endpoint=None, mult=None, **kwargs):
    """This function attempts to return a unique URI for an ISEC REST API endpoint

    It takes in the string name of the endpoint, HTTP method, sub_endpoint, mult and kwargs
    It will then filter all available endpoints based on args provided and attempts to select one,
    injecting the relevant parameters into the returned uri.
    """

    endpoints = list(get_endpoints(urls=uris))

    if endpoint:
        endpoints = [x for x in endpoints if x[0][0] == endpoint]

    if method:
        endpoints = [x for x in endpoints if x[0][1] == method]

    if sub_endpoint:
        endpoints = [x for x in endpoints if x[0][2] == sub_endpoint]

    if mult is True:
        endpoints = [x for x in endpoints if "all" in x[0]]

    if mult is False:
        endpoints = [x for x in endpoints if "one" in x[0]]

    # -------------- END FILTERING VIA COMPREHENSIONS ------------------#
    # filtering now is selective instead of subtractive... this is important to note

    replacement = []

    for key in kwargs:
        for endp in endpoints:
            if f"{{key}}" in endp[1]["href"] and endp not in replacement:
                replacement.append(endp)
            else:
                if "params" in endp[1].keys():
                    if endp[1]["params"]:
                        for param in endp[1]["params"]:
                            if key in param and endp not in replacement:
                                replacement.append(endp)

    if len(replacement) > 0:
        # replacement = list({s for s in replacement})
        endpoints = replacement

    # we now have ideally a list of only one URI to work with

    if len(endpoints) == 1:
        return inject_params(endpoints[0][1], kwargs)

    if len(endpoints) > 1:
        names = [x[1]["href"] for x in endpoints]
        raise NonUniqueFilter(
            f"Unable to determine unique endpoint URI from provided "
            f"arguments:\n\n"
            f"endpoint={endpoint}\nmethod={method}\nsub_endpoint={sub_endpoint}"
            f"\nmult={mult}\nparameters={kwargs}"
            f"\n\nURIs remaining in filter:"
            # f"{len(names)}"
            f"{names}"
        )

    raise NoURIsFound(
        f"No endpoints found matching applied filters: "
        f"arguments:\n\n"
        f"endpoint={endpoint}\nmethod={method}\nsub_endpoint={sub_endpoint}"
        f"\nmult={mult}\nparameters={kwargs}"
    )
