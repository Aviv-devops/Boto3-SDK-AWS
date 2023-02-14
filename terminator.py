import boto3
import datetime

#WORKS - gets a list of instances_id to delete and terminate them
def teminate_instances(id_lists_to_term: list):
    print("The terminated intances are: ")
    print(id_lists_to_term)
    try:
        ec2 = boto3.client("ec2")
        for instance in id_lists_to_term:
            ec2.terminate_instances(InstanceIds=[instance])
    except Exception as e:
        print(e)


# WORKS - third to run - return id of instances with date more than a week
def returns_list_instances_id_to_term():
    list_to_term = []
    try:
        ec2 = boto3.client("ec2")
        #print(ec2.describe_instances())
        for reservation in ec2.describe_instances()["Reservations"]:
            for instance in reservation["Instances"]:
                for tag in instance["Tags"]:
                    data_cteation_of_instance = tag["Key"] #need to fix - go through all the tags instead of taking the first one only.
                    if data_cteation_of_instance == "Date":

                        string_of_date = tag["Value"]  # value of tag of date
                        date_of_today = datetime.datetime.now().strftime('%d/%m/%y')


                        # parse to datetime.datetime
                        datetime_instance = datetime.datetime.strptime(string_of_date, '%d/%m/%y')
                        datetime_today = (datetime.datetime.strptime(date_of_today, '%d/%m/%y'))

                        # caculate
                        delta = datetime_today - datetime_instance

                        if delta.days > 7:
                            list_to_term.append(instance["InstanceId"])
        return list_to_term
    except Exception as e:
        print(e)
