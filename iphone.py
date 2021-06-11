from pyicloud import PyiCloudService

api = PyiCloudService('jsiddique@apple.com', 'Suite506!')

if api.requires_2fa:
    print( "Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

