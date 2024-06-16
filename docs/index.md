# Welcome to atlassible

This is an attempt to encapsulate the various RESTful APIs offered by Atlassian.
It's built to help blind people more easily interface with tools like Jira.
It can be included in Python scripts to optimize command line interfaces.
Or used, along with [domible](https://joeldodson.github.io/domible)
to build static HTML pages for more easily reading through Jira issues in an accessible way.

The actual atlassible package is barely in skeletal form,
I'll provide more detailed docs as I figure out what I'm doing.

There is an optional extra package installable with atlassible, aticli.
aticli is a typer based python script to both give examples of using atlassible,
and hopefully be a useful tool out of the box.
See below for how to install aticli along with atlassible.

## Getting Started (Configuration)

### Using Basic Auth for REST API calls

Atlassible is using Basic Auth to access the REST APIs.
Atlassian does not allow a password to be used for Basic Auth, you'll need a token.
This [Atlassian article on Basic Auth](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/)
explains the various authentication options and includes a link for directions to get an API token for your account.

### Environment Variables

The following is from the `__init__.py` file to show the environment variables needed for atlassible to access your Atlassian services.

``` python 
atl_user = os.getenv("ATLASSIAN_USER", "ATLASSIAN_USER is missing")
atl_token = os.getenv("ATLASSIAN_API_TOKEN", "ATLASSIAN_API_TOKEN is missing")
atl_base_url = os.getenv("ATLASSIAN_BASE_URL", "ATLASSIAN_BASE_URL is missing")
atl_api_url = os.getenv("ATLASSIAN_API_URL", "/rest/api/3/")
```

- ATLASSIAN_USER is the username you use to log in to Atlassian services.
- ATLASSIAN_API_TOKEN is the token you obtained as described in the link above regarding Basic authentication.
- ATLASSIAN_BASE_URL is the URL you use to log in to Atlassian (e.g., https://yourcompany.atlassian.net).
- ATLASSIAN_API_URL affects which version of the REST API you're accessing.  It defaults to version 3.

As you can hopefully see from above, failing to set user, token, or base_url will result in failure.
The complete base URL used for REST queries is a concatenation of the base_url and api_url.
The base_url should not have a trailing slash,
and the api_url needs to begin and end with slashes.
As long as your environment variable for the base_url does not end with the slash, you should be fine.

Unless you really know what you are doing,
I suggest not changing the api_url.
It's very unlikely I've tested atlassible on anything other than the default.

### Install atlassible and aticli

To install only atlassible, and packages used by atlassible, run:

``` python
pip install atlassible
```

If you want to try aticli, run:

``` python
pip install atlassible[aticli]
```

aticli uses the typer package.
for details on its usage, run:

``` bash
aticli -h
```

My intent is to keep the help in aticli current
thus don't intend to provide any instructions in these docs.
I might add some notes if it turns out there's confusion around aticli.
Or maybe I'll fix aticli to avoid the confusion. 

## Future

Someday I might package aticli as a python executable perhaps runnable via `pipx`.
Or maybe I'll write something in [BeeWare](https://beeware.org) 
and release that as a package.
