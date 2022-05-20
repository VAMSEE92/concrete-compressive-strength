# Concrete Compressive strength
### Demo
Link
[http://ec2-52-66-46-245.ap-south-1.compute.amazonaws.com](http://ec2-52-66-46-245.ap-south-1.compute.amazonaws.com:8080/)
![Web app demo Image](https://image-33.jpg) 
### Problem Statement
The actual concrete compressive strength (MPa) for a given mixture under a
specific age (days) was determined from laboratory. Data is in raw form (not
scaled).The data has 8 quantitative input variables, and 1 quantitative output
variable, and 1030 instances (observations).

### Context
Concrete is the most important material in civil engineering. The concrete
compressive strength is a highly nonlinear function of age and ingredients.
These ingredients include cement, blast furnace slag, fly ash, water,
superplasticizer, coarse aggregate, and fine aggregate.

##### 
### Steps performed 
1) Training a model to predict concrete compressive strength
2) Deploying it on AWS Instance

### Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/)
If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository

    pip install -r requirements.txt
### Deployment on AWS EC2
#### Step 1:
Launch an ec2 instance on aws. You can find instructions to launch ec2 instance [here](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html)
![ec2_instance_selection](https://image-33.jpg)
#### Step 2:
Connect to your instance using putty. You can find instructions on how to connect to ec2 instance using putty [here](https://asf.alaska.edu/how-to/data-recipes/connect-to-your-ec2-instance-using-putty-v1-1/)
#### Step 3:
Copy the app deployment files  into your ec2 instance using winSP, filezilla. [here](https://asf.alaska.edu/how-to/data-recipes/moving-files-into-and-out-of-an-aws-ec2-instance-windows/) are some instructions you can follow to transfer files into ec2 from your machine.
#### Step 4:
Go to your ec2 terminal and run the following commands

    sudo apt-get update
    sudo apt install python3-pip
    pip3 install -r requirements.txt
#### Step 5:
Got to security group in Network & Security and create a new security group with inbound rule as All traffic for this sinario. Add the recently created security group to your instance
![Creating security Group](https://image-33.jpg)
![Adding security Group](https://image-33.jpg) 
#### Step 6:
Go to your ec2 terminal and run the following command.

    python3 Server.py

In connect to instance window under SSH client tab you can find a public dns on which your web app is running
![Public DNS](https://image-33.jpg)
### Directory Tree
    |__ app
    |    |__static
    |    |__template   
    |    |__client.py
    |    |__Finalmodel.pkl
    |    |__Server
    |__images
    |__concrete.csv
    |__ConcreteComprehensiveStrength.ipynb
    |__Problem_Statment
    |__requirements.txt

### Technologies and Tools Used
![!technologies](https://image-33.jpg)
### References
[UCI ML repository on concrete comprehensive strength](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength) 