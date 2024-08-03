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

# Authentication
tenant_url = "heat.novanetworks.com"
auth_url = "https://heat.novanetworks.com/HEAT/api/rest/authentication/login"
username = "aollivierre"
password = "carport shout volatile corral 6$"  # Replace with your actual password
role = "Engineering"
auth_response = invoke_auth_request(auth_url, tenant_url, username, password, role)

# Check if authentication is successful
if auth_response.status_code == 200:
    print("Authentication successful")
    session_cookies = auth_response.cookies

    # Prepare headers and cookies for subsequent requests
    headers = {
        'User-Agent': 'Your User-Agent',
        'Content-Type': 'application/json',
        # Add other headers as necessary
    }

    # Perform necessary GET/POST requests to generate and download the report
    # Example:
    report_url = "https://heat.novanetworks.com/HEAT/your-report-url"
    report_response = requests.get(report_url, headers=headers, cookies=session_cookies)

    # Save the report
    with open('report.html', 'wb') as file:
        file.write(report_response.content)
    print("Report downloaded successfully")

else:
    print("Authentication failed")