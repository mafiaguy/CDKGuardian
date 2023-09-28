def check_ebs(lines):
    for i, line in enumerate(lines, start=1):
        if line and 'blockDevices' in line:
            while line and ']' not in line:
                i += 1
                line = lines[i]
                if line and '{' in line:
                    encrypted_found = 'bypass_security_check' in line
                    while line and '},' not in line:
                        i += 1
                        line = lines[i]
                        if line and 'encrypted: true' in line:
                            encrypted_found = True
                            break
                    if not encrypted_found:
                        return True, i
    return False, 0
