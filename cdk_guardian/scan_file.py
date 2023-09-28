from check_ssh import check_ssh
from check_ebs import check_ebs
from check_accessibility import check_accessibility

def scan_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    ssh_open_to_world, ssh_line_number = check_ssh(lines)
    ebs_not_encrypted, ebs_line_number = check_ebs(lines)
    accessible, accessibility_line_number = check_accessibility(lines)
    return ssh_open_to_world, ssh_line_number, ebs_not_encrypted, ebs_line_number, accessible, accessibility_line_number
