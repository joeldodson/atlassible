# Changelog

## v0.1.1 (2024-06-19)

- supporting expand parameter, starting with myself endpoint
- started documenting the API with note regarding the expand parameter
- update aticli to support expand option for the 'me' sub-command
- fixed typo in pyproject.toml for docs URL

## v0.1.0 (2024-06-16)

- First release of `atlassible`!
- atlassible is an attempt to make using the Atlassian REST APIs easier.
  I wouldn't go so far as to call it an SDK, maybe it's more of a hack.
- also providing a CLI, aticli, for example usage
  (run `aticli -h` for details).
- Initial release of atlassible has a single query to Atlassian to get user information 
  (that is, query for 'myself').
  aticli has a single command, `aticli me`, to test the atlassible API.
- consider this the "hello world" release of atlassible and aticli. 
