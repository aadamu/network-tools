import tornado.web
import cisco_status
import re


def cisco_status_web():
    class CiscoStatusHandler(tornado.web.RequestHandler):
        def get(self):
            show_version_output = None
            cisco_status_template = "html_templates\ciscostatus.html"
            self.render(cisco_status_template, show_version_output=show_version_output)

        def post(self):
            show_version_output = cisco_status.show_version(self.get_body_argument("device_hostname"))
            re_device_model = re.search(r"Cisco (.+?) .+bytes of memory", show_version_output)
            re_device_version = re.search(r"Cisco IOS Software.*Version (.+?),", show_version_output)
            #re_device_uptime = re.search(r".uptime is .*", show_version_output)
            re_device_hostname = re.search(r"((.+) uptime is .+)", show_version_output)
            re_device_serial = re.search(r"Processor board ID (.+)", show_version_output)
            cisco_status_template = "html_templates\ciscostatus.html"
            self.render(cisco_status_template,
                        show_version_output=show_version_output,
                        re_device_version=re_device_version.group(1),
                        re_device_model=re_device_model.group(1),
                        #re_device_uptime=re_device_uptime.group(1),
                        re_device_hostname=re_device_hostname.group(1),
                        re_device_serial=re_device_serial.group(1)
                        )

    return (CiscoStatusHandler)