# Copyright (c) 2019 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse
from github import Github

parser = argparse.ArgumentParser()

class GitHubIssueQuery(object):

    def __init__(self, repository, username, password):

        self.username = username
        self.password = password
        self.repository = repository

        # using username and password
        self.github = Github(self.username, self.password)

    def query(self, owner=None, state=None):
        kwargs = {}
        if owner:
            kwargs.update({'assignee': owner})
        if state:
            kwargs.update({'state': state})

        # get the github issues, based on these parameters
        issues = self.github.search_issues("", **kwargs)

        return issues

    def show_issues(self, owner=None, state=None):

        issues = self.query(owner=owner, state=state)
        for issue in issues:
            raw_issue = issue.raw_data
            # Need to replace URL with one user can access
            url = raw_issue['url'].replace('api.','').replace('repos','')
            print "%s %s" % (raw_issue['number'], url)
