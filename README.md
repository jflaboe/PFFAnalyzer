# PFFAnalyzer

Downloads PFF data weekly and also provides a UI for analyzing the PFF data

## Dev Environment Setup

You must be working on Windows in order to build the necessary development environment. 

### Clone the Repo

```
git clone https://github.com/jflaboe/PFFAnalyzer.git
cd PFFAnalyzer
```

### IIS Setup (Internet Information Services)

IIS is what allows you to run a server on your Windows machine, however it is an optional feature. In order to install IIS, please follow the tutorial at this [link](https://www.howtogeek.com/112455/how-to-install-iis-8-on-windows-8/).

When you get to the step where you are turning on/off Windows features, mark the IIS dropdown as specified, but also use the dropdowns to navigate to **Internet Information Services > World Wide Web services > Application Development Features** and enable CGI

### Python installation

Make sure you have Python 3.x installed. You will be working inside a virtual environment.

```
pip install virtualenv

virtualenv env

.\env\Scripts\activate

pip install -r requirements.txt #install known dependencies.
```

Once you've completed installing these Python dependencies, you need to enable wfastcgi:

```
wfastcgi-enable
```

You can disable it later using:

```
wfastcgi-disable
```



## How it works

First, it is important to schedule a task on the Windows server to pull from this repository on a regular interval, in order to update the service without having to manually update the device

Second, environment variables for the PFF API Key must be set on the server so it can access PFF for data


