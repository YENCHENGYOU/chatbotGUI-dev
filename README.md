# chatbotGUI

## Overview

This repository is the senior project of NCCU MIS, we demo at Dec 2023. Entire system includes 3 part:

1. web server (Flask)
2. SQL server (MySQL)
3. LLM backend (cloud)

This repository only have part1. The remain parts are more environment setting rather than coding itself.

## Environment Setup

We use Python 3.11 with Flask to develop this project, environment can be created as follows:
```
conda create -n chatbotGUI python=3.11
conda activate chatbotGUI
pip install flask
pip install flask_sqlalchemy
pip install sqlalchemy
```

## Password

We store MySQL password outside of this directory ("../passwords.txt")