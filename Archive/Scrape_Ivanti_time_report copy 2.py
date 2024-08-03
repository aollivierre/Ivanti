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

    # Session cookie from authentication response
    cookies = auth_response.cookies

    # Headers for subsequent requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://heat.novanetworks.com',
        'Referer': 'https://heat.novanetworks.com/HEAT/WorkspaceLoader.aspx?Id=dashboard%23Home&Profile=dashboard&LayoutName=&TabId=ext-comp-1084',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    # Report generation URL (this needs to be specific to your report)
    report_generation_url = 'https://heat.novanetworks.com/HEAT/Report/services/ReportService.asmx/ReportViewerSessionAssert'

    # POST data for report generation (this needs to be specific to your report)
    report_generation_data = {
        # Add the specific data needed for your report generation here
    }

    # Sending POST request to initiate report generation
    report_generation_response = requests.post(report_generation_url, headers=headers, cookies=cookies, json=report_generation_data)

    if report_generation_response.status_code == 200:
        print("Report generation initiated")

        # Report download URL (replace with the specific URL for your report)
        report_download_url = 'https://heat.novanetworks.com/HEAT/Report/handlers/ReportViewer.aspx?_csrfToken=TOKEN&ReportId=REPORT_ID'

        # Sending GET request to download the report
        report_download_response = requests.get(report_download_url, headers=headers, cookies=cookies)

        if report_download_response.status_code == 200:
            # Saving the report
            with open('report.html', 'wb') as file:
                file.write(report_download_response.content)
            print("Report downloaded successfully")
        else:
            print("Failed to download report")

    else:
        print("Failed to initiate report generation")
else:
    print("Authentication failed")
