import requests
from requests.cookies import RequestsCookieJar

def invoke_auth_request(auth_url, tenant_url, username, password, role):
    # Construct the authentication body
    auth_body = {
        "tenant": tenant_url,
        "username": username,
        "password": password,
        "role": role
    }

    # Send the POST request
    response = requests.post(auth_url, json=auth_body, headers={"Content-Type": "application/json"})

    return response


# Usage example
tenant_url = "heat.novanetworks.com"
auth_url = "https://heat.novanetworks.com/HEAT/api/rest/authentication/login"
username = "aollivierre"
password = "carport shout volatile corral 6$"  # Be cautious with plain text passwords
role = "Engineering"

auth_response = invoke_auth_request(auth_url, tenant_url, username, password, role)

# session = requests.Session()
# cookies = RequestsCookieJar()
# # Add cookies from Fiddler output
# cookies.set('UserSettings', 'YourValueHere')
# cookies.set('SessionTimezoneName', 'America/Toronto')
# # Add other cookies as needed
# session.cookies = cookies


post_url = "https://heat.novanetworks.com/HEAT/Report/services/ReportService.asmx/ReportViewerSessionAssert"
post_headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    # Add other headers as necessary
}
post_data = {}  # Add your POST data here
response = session.post(post_url, headers=post_headers, json=post_data)



get_url = "https://heat.novanetworks.com/HEAT/Report/handlers/ReportViewer.aspx?_csrfToken=YourToken&ReportId=YourReportId"
get_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # Add other headers as necessary
}
report_response = session.get(get_url, headers=get_headers)

with open('report.html', 'wb') as f:
    f.write(report_response.content)

# Use smtplib or another library to send the report via email