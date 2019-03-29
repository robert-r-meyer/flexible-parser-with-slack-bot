import os
import check_mk_web_api
from lighthouse.format import FormatFor


class CheckMkClient():
    def __init__(self):
        self._api = check_mk_web_api.WebApi(
            os.getenv('CHECK_MK_SERVER', 'ERROR'),
            username=os.getenv('CHECK_MK_USER', 'ERROR'),
            secret=os.getenv('CHECK_MK_PASSWORD', 'ERROR')
            )

    def all_hosts(self):
        try:
            blob = self._api.get_all_hosts()
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def host(self, hostname):
        try:
            blob = self._api.get_host(hostname)
            return FormatFor.slack_json_as_code_blob(blob)
        except check_mk_web_api.CheckMkWebApiException as inst:
            return str(inst)

    def discover_services(self, hostname):
        try:
            blob = self._api.discover_services(hostname)
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def discover_all_services(self):
        try:
            blob = self._api.discover_services_for_all_hosts()
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def set_downtime(self, host_name, message, downTime=120):
        try:
            blob = self._api.set_downtime(host_name, message, downTime)
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def get_all_downtimes(self):
        try:
            blob = self._api.get_all_downtimes()
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def get_alerts(self):
        try:
            blob = self._api.get_alerts()
            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst
