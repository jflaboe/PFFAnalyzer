# PFFAnalyzer

Downloads PFF data weekly and also provides a UI for analyzing the PFF data

## Dev Environment Setup

You must be working on Windows in order to build the necessary development environment. 

### IIS Setup (Internet Information Services)

IIS is what allows you to run a server on your Windows machine, however it is an optional feature. In order to install IIS, please follow the tutorial at this [link](https://www.howtogeek.com/112455/how-to-install-iis-8-on-windows-8/).

### Python installation

Make sure you have Python 3.x installed. You will also need to install a few Python packages:

```
pip install flask
pip install wfastcgi
```

Once you have successfully install wfastcgi, please run the following command:

```
wfastcgi-enable
```


## How it works

First, it is important to schedule a task on the Windows server to pull from this repository on a regular interval, in order to update the service without having to manually update the device

Second, environment variables for the PFF API Key must be set on the server so it can access PFF for data


