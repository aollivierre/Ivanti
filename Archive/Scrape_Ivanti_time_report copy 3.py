import requests

def invoke_auth_request(auth_url, tenant_url, username, password, role):
    # Authentication body as per your function
    auth_body = {
        "tenant": tenant_url,
        "username": username,
        "password": password,
        "role": role
    }
    # Sending the POST request for authentication
    response = requests.post(auth_url, json=auth_body, headers={"Content-Type": "application/json"})
    return response

# Authentication parameters
tenant_url = "heat.novanetworks.com"
auth_url = "https://heat.novanetworks.com/HEAT/api/rest/authentication/login"
username = "aollivierre"
password = "carport shout volatile corral 6$"  # Replace with the actual password
role = "Engineering"

# Perform authentication
auth_response = invoke_auth_request(auth_url, tenant_url, username, password, role)

# Check if authentication is successful
if auth_response.status_code == 200:
    print("Authentication successful")
    session_cookies = auth_response.cookies

    # Headers for the POST request to start report generation
    post_headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        # ... [Other Headers] ...
    }

    # The POST data/body for report generation
    # This data needs to be identified from the Fiddler output or the web application's behavior
    report_generation_data = {
        # Add the specific data required for report generation here
    }

    # Report generation URL
    report_generation_url = 'https://heat.novanetworks.com/HEAT/Report/services/ReportService.asmx/ReportViewerSessionAssert'

    # Send POST request to initiate report generation
    report_generation_response = requests.post(report_generation_url, headers=post_headers, cookies=session_cookies, json=report_generation_data)

    if report_generation_response.status_code == 200:
        print("Report generation initiated")

        # Report download URL
        # The token and report ID need to be dynamically determined
        report_download_url = 'https://heat.novanetworks.com/HEAT/Report/handlers/ReportViewer.aspx?_csrfToken=DYNAMIC_TOKEN&ReportId=DYNAMIC_REPORT_ID'

        # Send GET request to download the report
        report_download_response = requests.get(report_download_url, headers=post_headers, cookies=session_cookies)

        if report_download_response.status_code == 200:
            with open('report.html', 'wb') as file:
                file.write(report_download_response.content)
            print("Report downloaded successfully")
        else:
            print("Failed to download report")
    else:
        print("Failed to initiate report generation")
else:
    print("Authentication failed")
