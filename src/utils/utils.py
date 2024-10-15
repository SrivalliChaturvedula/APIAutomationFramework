# Contains common utilities
# Setting headers
# read data from excel file
# read data from csv,json file
# set headers - application/json, application/xml

class Utils(object):

    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml"
        }
        return headers

    def common_headers_put_patch_delete_basic_auth(self, basic_auth):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth),
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

