from netmiko import ConnectHandler

R8 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.0.1',
    'username': 'networkluke',
    'password': 'networkluke',
}

R14 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.1.2',
    'username': 'networkluke',
    'password': 'networkluke',
}

devices = [R8, R14]

for a_device in devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('show ip int brief')
    print(output)

