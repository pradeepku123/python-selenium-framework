Date: DEC 10 2021

Framework
Python
Slenium
pythest-Unit Testing Framework
POM
HTML Report
Log

## Setup Python Envirnment

    1.1: $python3.10 -m venv venv
    1.2: $source venv/bin/activate

## Dependencies Tree Management

    1.1: $pip freeze > requirements.txt
    1.2: $pip install -r requirement.txt # To installed all Dependencies which was present in Requirement.txt File(1f All ready exist)

## Check Envirnment Setup

    it should be Dispaly Commandline "(<Virtualenv Name>) <Sysytem Name>:~/workstation/pytest-playground-kickstart$"
    1.1: $python --version
    1.2: $pip --version

## Setup Git

    1.1: $git inti
    1.2: $git status

## Install Packages

    1.1:$pip install -U pytest
    1.2:$pytest --version

## Run your First Pytest

    1.1: $python -m pytest / $pytest

Library to install

pip install pytest-xdist
pip install pytest-html
pip install pytest
pip install selenium
pip install webdriver-manager

## To Start

python -m pytest
