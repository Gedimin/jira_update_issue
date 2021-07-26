import os
import time
from jira import JIRA
from datetime import datetime
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()

jira_server = os.environ['jira_server']
jira_user = os.environ['jira_user']
project_code = os.environ['project_code']
created_after = os.environ['created_after']
max_results = os.environ['max_search_results']
assignee_person = os.environ['assignee_person']
field_to_search = os.environ['field_to_search']
status_issue = os.environ['status_issue']

jira_password = os.environ['JIRA_PASSWORD'] if "JIRA_PASSWORD" in os.environ else getpass(prompt='Password: ', stream=None)

start_time = time.time()

search_string = f'project in ({project_code}) AND created >= {created_after} AND status in {status_issue} AND assignee in ({assignee_person}) AND "{field_to_search}" is EMPTY order by created DESC'

jira_server = {'server': jira_server}
jira = JIRA(basic_auth=(jira_user, jira_password), options=jira_server)
issues_to_process = jira.search_issues(search_string, maxResults=max_results)

if len(issues_to_process) == 0:
    print('Issues not found')
else:
    print(f'INFO - Search returns up to first {max_results} results. You can increase it by changing value of \"max_results\" variable.')
    print(f'Found {len(issues_to_process)} issues. Updating...')
    for issue in issues_to_process:
        orig_value_date_depl = issue.fields.customfield_27700

        # getting date and update {field_to_search} field
        resolved_date = datetime.strptime(issue.fields.resolutiondate.split('+')[0], '%Y-%m-%dT%H:%M:%S.%f')
        updated_date_depl = resolved_date.strftime('%Y-%m-%d')

        # upgrading {field_to_search} field and print
        print(f'{issue.key}: {issue.fields.summary}, {field_to_search}: {orig_value_date_depl} -> {updated_date_depl}')
        issue.update(fields={'customfield_27700': updated_date_depl})

end_time = time.time()
print(f'Time spent: {end_time - start_time:.2f} sec')
