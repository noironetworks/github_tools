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

from github import Github

# Here are the keys for a GitHub issue:
# 'labels'
# 'number'
# 'assignee'
# 'repository_url'
# 'closed_at'
# 'id'
# 'title'
# 'comments'
# 'state'
# 'body'
# 'events_url'
# 'labels_url'
# 'author_association'
# 'comments_url'
# 'html_url'
# 'updated_at'
# 'node_id'
# 'user'
# 'milestone'
# 'closed_by'
# 'locked'
# 'url'
# 'created_at'
# 'assignees'
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
            print "%s %s" % (raw_issue['number'], raw_issue['html_url'])
