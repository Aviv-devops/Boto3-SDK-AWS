import boto3
import datetime

#WORKS - first to run - return list_image_info
def read_from_file_return_list_image_info():
    image_from_a_file = []
    my_filer = open(r"C:\Users\Aviv\PycharmProjects\Final-Project-16.01.23\configuration.txt", 'r')
    for line in my_filer:
        split_list = line.split(": ")[1]
        split_list = split_list.split("\n")[0]
        image_from_a_file.append(split_list)
    my_filer.close()
    return image_from_a_file

#WORKS - second to run - return list
def create_ec2(info_of_instance : list):
    date_of_creation = datetime.datetime.now().strftime("%d/%m/%y")
    with open(r"C:\Users\Aviv\PycharmProjects\Final-Project-16.01.23\user-data.sh", 'r') as data:#with open - doesnt need to close the file
        user_data_script = data.read()

    try:
        count = 0
        ec2 = boto3.client("ec2")
        number_of_instances = int(input("how many instances would you like?"))

        for instance_num in range(1,number_of_instances+1):
            instance_info = (ec2.run_instances(
                InstanceType=info_of_instance[0],
                KeyName=info_of_instance[1],
                ImageId= info_of_instance[2],
                SecurityGroupIds=[info_of_instance[3]],
                MinCount=1,
                MaxCount=1,
                UserData=user_data_script,
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'web' + str(instance_num)
                            },
                            {
                                'Key': 'Date',
                                'Value': date_of_creation
                            },
                        ]
                    },
                ]
            )
            )
            # print private ip
            print(instance_info["Instances"][0]["PrivateIpAddress"])

    except Exception as e:
        print(e)
