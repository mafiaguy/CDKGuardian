def check_ssh(lines):
    for i, line in enumerate(lines, start=1):
        if line and 'addIngressRule' in line and ('0.0.0.0/0' in line or 'anyIpv4()' in line or 'anyIpv6()' in line) and 'bypass_security_check' not in line:
            return True, i
    return False, 0
