# CDKGuardian

CDKGuardian is a simple Static Application Security Testing (SAST) tool designed to scan AWS Cloud Development Kit (CDK) code for potential misconfigurations. 

## Features

Currently, CDKGuardian checks for the following:

- SSH port open to the world leading to password brute-forcing
- EBS disk not encrypted.

## Usage

To use CDKGuardian, simply run the Python script and provide the path to the directory containing your AWS CDK code:

```bash
python cdk_guardian.py /path/to/your/cdk/code
```
if you want to bypass this scan from a particular place you can add
```bash
encrypted: false,//bypass_security_check
```



