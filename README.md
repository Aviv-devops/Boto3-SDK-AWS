# Boto3-SDK-AWS
Create and terminate AWS instances.

# Goal of project:
Create AWS instanes as the user ask with the name "web1", "web2..." and prints the private ip of the instances it created.
After the creation the terminator.py search for instances with the tag "Date" in the format "%d/%m/%y" and delete those that were created more than a week ago.

# Dependencies
files: 
configuration.txt = contain information of the image to create instances.
user-data.sh = run on the instances when create them.
Creator.py = create the instanes and print the private ip (uses image from the configuration.txt).
Terminator.py = chek which to delete and delete them.
main.py = active the project

Installation of: Boto3, awscli


# Installations:
to install boto3:
Install Python on Your System 
Install PIP on your System 
Install Boto3 on System 

Install boto3 on PyCharm: 
https://blog.finxter.com/how-to-install-boto3-on-pycharm/ 

In the terminal PyCharm:  
Pip install awscli 
Run "aws configure" and connect to your user.

# Remember before running
Update the loation of "configuration.txt" and "user-data.sh" in creator.py

# where to start
Run main.py to initiate the program.
