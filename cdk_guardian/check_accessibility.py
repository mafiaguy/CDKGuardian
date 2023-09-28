def check_accessibility(lines):
    inside_rds_instance = False
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if 'new rds.DatabaseInstanceFromSnapshot' in line:
            inside_rds_instance = True
        if inside_rds_instance:
            if 'publiclyAccessible: true' in line:
                return True, i
            elif '});' in line:
                inside_rds_instance = False
    if inside_rds_instance:
        return True, i
    return False, 0
