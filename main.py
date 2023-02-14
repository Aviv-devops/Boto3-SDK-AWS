import terminator
import creator

list_to_term = []

#create ec2 instances and prints their private ip
creator.create_ec2(creator.read_from_file_return_list_image_info())

#terminate the instances in the list list_to_term
terminator.teminate_instances(terminator.returns_list_instances_id_to_term())
