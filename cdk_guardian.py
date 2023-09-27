import os

def print_cool_font():
    print("CDKGuardian by Mafiaguy (Siddhanth) 🚀🔒\n")
    print("Checking For port open to the world leading to password brute-forcing 🚀🔒\n")
print_cool_font()

def scan_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ssh_open_to_world = False
    ssh_line_number = 0

    for i, line in enumerate(lines, start=1):
        if 'addIngressRule' in line and ('0.0.0.0/0' in line or 'anyIpv4()' in line or 'anyIpv6()' in line) and 'bypass_security_check' not in line:
            ssh_open_to_world = True
            ssh_line_number = i

    return ssh_open_to_world, ssh_line_number

def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')  # remove 'node_modules' from the list of sub-directories to avoid scanning it
        for file in files:
            if file.endswith('.ts'):
                file_path = os.path.join(root, file)
                print(f"Scanning file: {file_path}")  # print the name of the file being scanned
                ssh_open_to_world, ssh_line_number = scan_file(file_path)
                if ssh_open_to_world:
                    print(f"Potential misconfiguration found in file: {file_path}")
                    print(f"SSH open to the world at line {ssh_line_number}.")

scan_directory('.')


