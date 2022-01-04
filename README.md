![GMIT Logo](img/gmit-logo.png)

# Data Representation

Author: Shane Rylands

G00387904@gmit.ie
***

## Overview

This repository contains my project submission for the Data Representation module 2021. The purpose of this project is to demonstrate that I have achieved the learning outcomes of the module, which are:
- Describe the stochastic nature of real-world measurements.
- Select an appropriate mathematical model of a real-world problem.
- Select an appropriate cost function for a given machine learning task.
- Apply an optimisation technique to the parameters of a model.

and I able to create and consume RESTful API


Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.


***

## Table of Contents

- staticpages folder:
    - index.html
    - shopping_list.html
    - login.html
    - stlyes.css
- restfulAPI.py
- shopDao.py
- ReadMe.md
- gitignore
- requirements.txt
- img folder

***

## Install

To run my project submission on your local device you will need to do the following. First, download the GitHub repository (repo) to your local device. To do so, simple open this link [github repo](https://github.com/shaner1/data-representation-project). Click the green code button and select download ZIP at the bottom, then unzip the folder on your device. In your command line interface (CLI) navigate to the folder using `cd` + filepath, for example:`cd Downloads/Data-representation-project-main`. From your CLI you can launch the RESTful API in your web browser with `python restfulAPI.py`.

### Requirements

To run my project submission from your local device you will need a python environment. The easiest way to do this is to install Anaconda, which is a helpful python distribution package. You can find out how to do this here: [Python Installation Guide](https://docs.anaconda.com/anaconda/install/index.html)

You will also need to have flask installed. Information on how to do this you find here: [Flask Installation Guide](https://flask.palletsprojects.com/en/2.0.x/installation/)

To enusre no errors and run the project as I have, you will need to install all the same packages as on my device. I am working off a MAC. The requirements.txt file contains all the necessary package and their versions. The easiest way to install these files is, while you are in the repo folder in your CLI, enter: `pip install -r requirements.txt`.

Alternatively, if you do not wish to install all these packages and files to your local device you can run them in a virtual environment. While in the folder with the repo in your CLI, do the following:

1. Type `python3 -m venv venv` to create a virtual environment (VM).
2. Then `source venv/bin/activate` for MAC or `.\venv\Script\activate.bat` for Windows to open the environment.
3. Then `pip install -r requirements.txt` to install the necessary packages
4. Then `python restfulAPI.py` to run.

To exit the VM type deactivate.

***

## Run API

Once you have the API up and running all you need to do is open a web browswer and type:
`http://127.0.0.1:5000/index.html`

***

## Conclusion

In conclusion,

The styling of the static pages changes whether openen directly or through the restful api and I couldn'f figure out why.
***

## Troubleshooting

If you are unable to access any data from the web application, please check the DAO is working with curl. 
For testing the create method:
`curl -X POST -d "{\"product\":\"apple\",\"price\":\"0.80\",\"quantity\":30}" -H Content-Type:application/json http://127.0.0.1:5000/stock`
For testing the update method:
`curl -X PUT -d "{\"product\":\"apple\",\"price\":\"0.80\",\"quantity\":40}" -H Content-Type:application/json http://127.0.0.1:5000/stock/2`
For testing the delete method:
`curl -X DELETE http://127.0.0.1:5000/stock/5`

If you encounter any other errors with this project please contact me at [G00387904@gmit.ie](mailto) and I will be happy to assist you in any way I can.

***

## Credits

Throughout this project, I have borrowed heavily from the Data Representation module course work created by Andrew Beatty of GMIT.

***