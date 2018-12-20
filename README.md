# LogsAnalysis
LogsAnalysis for udacity

# Required Libraries and such
1. Install python ... this version uses 3.6.5
2. Install Git Bash
3. Download Vagrant and VirtualBox 
4. install pip
5. pip install psycopg2 

# Required data and files

1. Get data: 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2. Unzip the file ... save it under your vagrant folder as newsdata

3. Download the main.py file from this repo ... save it under your vagrant folder as main.py

# How to run

1. Open up your git bash
2. cd into your vagrant folder
3. type: vagrant up ... to initilize the vagrant vm
4. type: vagrant ssh
5. type: cd /vagrant and now your console should say something like: vagrant@vagrant:/vagrant$ 

***Comment: this could have just been my mistake to misplace the file ***
***Might not need to do step 5 depending on where you save the file ... you should be operating within your vagrant vm***

6. pip install psycopg2 or pip install psycopg2-binary if you have not done so already 
7. type: python main.py
8. The output should be present in the console. 


