import os
from termcolor import colored
from scan_file import scan_file

def scan_directory(directory_path, checks):
    ssh_files = []
    ebs_files = []
    accessible_files = []
    for root, dirs, files in os.walk(directory_path):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')  # remove 'node_modules' from the list of sub-directories to avoid scanning it
        for file in files:
            if os.path.splitext(file)[1] == '.ts':
                file_path = os.path.join(root, file)
                ssh_open_to_world, ssh_line_number, ebs_not_encrypted, ebs_line_number, accessibility_line_number, accessible = scan_file(file_path)
                if 'ssh' in checks and ssh_open_to_world:
                    ssh_files.append("\tFile: {}:{}".format(file_path, ssh_line_number))
                if 'ebs' in checks and ebs_not_encrypted:
                    ebs_files.append("\tFile: {}:{}".format(file_path, ebs_line_number))
                if 'ebs' in checks and accessible:
                    accessible_files.append("\tFile: {}:{}".format(file_path, accessibility_line_number))

    if ssh_files:
        print(colored("Ensure AWS EC2 port is not open for all",'green'))
        print(colored("Error: AWS EC2 port is open for all",'green'))
        print(colored('\n'.join(ssh_files),'red'))
    if ebs_files:
        print(colored("Ensure AWS EBS volumes are encrypted",'green'))
        print(colored("Error: AWS EBS volumes are not encrypted",'green'))
        print(colored('\n'.join(ebs_files),'red'))
    if accessible_files:
        print(colored("Ensure AWS RDS isn't publicly accessible",'green'))
        print(colored("Error: AWS RDS is publicly accessible",'green'))
        print(colored('\n'.join(accessible_files),'red'))
