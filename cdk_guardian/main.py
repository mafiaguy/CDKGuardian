# cdk_guardian.py

import argparse
from scan_directory import scan_directory

def print_cool_font():
    print("CDKGuardian by Mafiaguy (Siddhanth) 🚀🔒\n")
    print("Checking for Misconfiguration in Your CDK Code ☠️✨⚡️\n")

def main():
    VERSION = 'v1.0'
    parser = argparse.ArgumentParser(description='Scan for misconfigurations.')
    parser.add_argument('--check', type=str, help='Specify which check to perform (ebs or ssh)')
    parser.add_argument('--dir', type=str, default='.', help='Specify the directory to scan')
    parser.add_argument('-v', '--version', action='version', version='CDK Guardian {}'.format(VERSION))
    args = parser.parse_args()

    print_cool_font()
    checks = [args.check] if args.check else ['ssh', 'ebs', 'accessible']  # perform specified check, or all checks if none specified
    scan_directory(args.dir, checks)

if __name__ == "__main__":
    main()
