# jira_update_issue
Script to update jira issue

<!-- ModuleNotFoundError No module named pipenv.vendor.vistir -->
pip install "pipenv==2018.11.26"
# Dependencies:
Modules `jira` and `python-dotenv` will be instaled.
```bash
pipenv install
```

# Usage
Create .env file with variables mentioned in script:
```bash
cat << EOF > .env
jira_server=https://jira_uri
jira_user=username
project_code=PROJECT_CODE
created_after=2021-01-01
max_search_results=10
assignee_person=User_JIRA
field_to_search='Custom_Field'
status_issue=("Solved", Closed)
EOF
```

Then just run:
```bash
pipenv run python jira_update_issue_field.py
```
