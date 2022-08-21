import boto3

#Default user
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")

ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
	if not "Tags" in each_item  and each_item['State']=='available':
		print('Deleting ',each_item['VolumeId'])
		ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
print("Delete all unused and untagged volumes.")
