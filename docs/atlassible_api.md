# The atlassible API

## Note on Expansion and Pagination

Please read the 
[Atlassian docs regarding expansion and pagination](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#expansion)
before reading the rest of this section.
Beyond here, I'll assume the terms, and how Atlassian supports them, are understood.

### Support for the expand parameter

For each endpoint supported in atlassible,
the function to get the resource(s) will support a named parameter, `expand`.
If the user already knows they want to expand some resources, a string can be passed to the function to be added as a query parameter.
This should result in the specified resources being included in the returned resource(s).

As I experiment with each endpoint using the Python REPL,
I look into the expand options and try ones I think are interesting.
Based on that process, I will add a constant to each module, `EXPAND_ALL`.
To use what I've decided is interesting, set the `expand`  parameter to `'all'`.

#### expand example

Using the myself endpoint, in the myself.py module, the constant is defined as:

``` python 
EXPAND_ALL = "groups,applicationRoles"
```

And here's how to get the myself resource with an expand query parameter including that string:

``` python 
import atlassible

me = atlassible.myself.get_me(expand='all'')
```

To see this in action, run the `aticli` tool on the command line:

``` bash
aticli -b me -e all
```

Your browser should pop up with a page from a local temp file with the myself resource including the expanded values.
