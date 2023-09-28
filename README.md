# CDKGuardian

CDKGuardian is a simple Static Application Security Testing (SAST) tool designed to scan AWS Cloud Development Kit (CDK) code for potential misconfigurations.

## Features

Currently, CDKGuardian checks for the following:

- SSH port open to the world leading to password brute-forcing
- EBS disk not encrypted.


## Installation

To install CDKGuardian, simply run the clone the script and provide the path to the directory containing your AWS CDK code:

```bash
git clone https://github.com/mafiaguy/CDKGuardian.git
cd CDKGuardian
pip install .
```
if installed properly you can check the version
```bash
cdk_guardian --version
```
or
```
cdk_guardian --v
```

## Usage

1. To use CDKGuardian, simply run the Python script and provide the path to the directory containing your AWS CDK code:

```bash
cdk_guardian --dir=<yourdirectory>
```
2. if you want to scan from a particular check you can add --check
```bash
cdk_guardian --check=ebs
```
3. if you want to bypass this scan from a particular place you can add the bypass_security_check comment in the cdk code
```bash
encrypted: false,//bypass_security_check
```