# CDKGuardian

CDKGuardian is a simple Static Application Security Testing (SAST) tool designed to scan AWS Cloud Development Kit (CDK) code for potential misconfigurations. 

## Features

Currently, CDKGuardian checks for the following:

- If an EC2 instance is created.
- If there's an open port configured.

## Usage

To use CDKGuardian, simply run the Python script and provide the path to the directory containing your AWS CDK code:

```bash
python cdk_guardian.py /path/to/your/cdk/code
