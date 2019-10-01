# github_tools
Tools to help extract information from github

This is meant to be a repo for providing automation around our noironetworks github.
The initial checkin is a simple CLI to extract github issues, but we can extend this
as needed.

To run the github issues tool, use:

    $ python github_cli.py -u \<github usernmame\> -p \<github password\> -o \<username to query\> -s \<state of bug (open|closed)\>

It should provide output like the following:

    925 https://github.com//noironetworks/support/issues/925
    922 https://github.com//noironetworks/support/issues/922
    918 https://github.com//noironetworks/support/issues/918
    916 https://github.com//noironetworks/support/issues/916
    915 https://github.com//noironetworks/support/issues/915
    909 https://github.com//noironetworks/support/issues/909
...
  
