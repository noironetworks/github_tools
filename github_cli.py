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

from github_issues import GitHubIssueQuery

def run():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("--username", "-u", 
                        help="Username for github account")
    parser.add_argument("--password", "-p", help="Password for github account")
    parser.add_argument("--owner", "-o", default="", help="Owner for the issue")
    parser.add_argument("--state", "-s", default="open", help="State for the issue (open or closed)")
    parser.add_argument("--repository", "-r", default="noironetworks",
                        help="Repository for github account (default is noironetworks)")
    args = parser.parse_args()
    querier = GitHubIssueQuery(username=args.username,
                               password=args.password,
                               repository=args.repository)
    querier.show_issues(owner=args.owner, state=args.state)

if __name__ == '__main__':
    run()

