from netmiko import ConnectHandler
import socket


class NetOperator(object):
    def __init__(self):
        self.username = "python"
        self.password = "*"

device_type = "cisco_ios"

current_operator = NetOperator()


def show_version(current_device):

    device_ip = socket.gethostbyname(current_device)
    command = "show version"
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=device_ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()
    net_connect.enable()
    output = net_connect.send_command(command)

    return (output)
