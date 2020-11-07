#This is my menu drivan system 
import os 
# import 
# ----------------------------------------------------------------------------------------------------------
# functions



def hadoop_srtup():
	print("your setup is in under construction")

def bank_app():
	print("your bank is in under construction")
	debit=[]
	credit=[]


#-----------------------------------------------------------------------------------------------------------------	

def task():
	pass






#-----------------------------------------------------------------------------------------------------------------	
def aws_app():
	print("------------------------------------------------------------------------------")
	print("------------------------------------------------------------------------------")
	print("press 1 for configure aws \npress 2 for ec2 services \npress 3 for s3 servicess \nPress 4 for ebs servicess  ")
	a=int(input("Enter here:"))
	# ----------------------------------------------------------------------------------------------------------
	# functions

	def ec2():

		print("-------------------------------------------------------------------------------\n-------------------------------------------------------------------")
		print()
		print("Enter 1 for launching instances \nEnter 2 for stop instances \nEnter three for get list of all instances\nCreate a key pair\nConfigure a security group")
		dd=int(input("Enter your choice here:"))
		if dd==1:
			inst_count=2
			print("You have{} instances running \n Enter 1 for amazon cli \n Enter 2 for rhel cli: ".format(inst_count))
			inst_input=int(input("Enter your choice here"))
			if inst_input==1:
				start_inst=int(input("Enter here"))
			if start_inst==1:
				asp=input("please put your instance id or if you want to use your older one press 1:")
				if asp==1:
					os.system('aws ec2 start-instances --instance-ids i-051caeab58eadd565')
				else:
					os.system('aws ec2 start-instances --instance-ids {}'.format(asp))
		elif dd==2:

			print("-------------------------------------------------------------------------------\b")
			runing_inst='2'
			print("You have {} instances running \nPress 1 for AWS OS \nPress 2 for Linux OS".format(runing_inst))
			stop_inst=int(input("Enter here"))
			if stop_inst==1:
				asp=input("please put your instance id or if you want to use your older one press 1:")
				if asp==1:
					os.system('aws ec2 stop-instances --instance-ids i-051caeab58eadd565')
				else:
					os.system('aws ec2 stop-instances --instance-ids {}'.format(asp))
			elif stop_inst==2:
				print("ho gya band ")	

		else:
			print("thanks for using this services")
	# ----------------------------------------------------------------------------------------------------------
	def s3():

		print("press 1 for Create a bucket \npress 2 for List buckets and objects \npress 3 for Delete buckets \npress 4 for Delete objects \npress 5 for Move objects \npress 6 for Copy objects \npress 7 for Sync objects ")	
		se_inp=int(input("Enter your choice  here :"))
		if se_inp==1:
			bkt_name=input("Enter your bucket name ")
			os.system('aws s3 mb {}'.format(bkt_name))
		elif se_inp==2:
			os.system('aws s3 ls')
		elif se_inp==3:
			dlt_bkt_name=input("Enter your bucket name you want to delete")
			os.system('aws s3 rb {}'.format(dlt_bkt_name))
		elif se_inp==4:
			dlt_obj_name=input("Enter your objects name you want to delete")
			os.system('aws s3 rm {}'.format(dlt_obj_name))
		else:
			return 0

	







	# ----------------------------------------------------------------------------------------------------------
	def ebs():
		print("pls fill those requirment to start a volume make insure u configure your aws first")
		vol_type=input("Enter your volume type  ")
		vol_size=input('enter your volume size in gb ')
		vol_size=int(vol_size)
		available_zone=input("Enter your zone name")	
	
		os.system('aws ec2 create-volume  --volume-type {}  --size {}  --availability-zone {}'.format(vol_type,vol_size,available_zone))





	# ----------------------------------------------------------------------------------------------------------

	if a==1:
		os.system("aws configure")

	elif a==2:
		ec2()
	elif a==3:
		s3()
	elif a==4:
		ebs()
	else:
		return 0	


# ------------------------------------------------aws module end ---------------------------------------------------------


def main():
	# os.system()
	print("Welcome to goutam os terminal ")
	print("-------------------------------")
	print("Enter 1 for setup hadoop :\nPress 2 to open aws services:\nEnter 3 for ansible :\nEnter 4 for Open bank app\n Enter 5 for hadoop \n Enter 6 for  Redhat  \nEnter 7 to open all task given by vimal sir")
	a=int(input("Enter your choice here:"))
	if a==1:
		print("your hadoop  is setup ")
		# hadoop_setup()
	elif a==2:
		aws_app()
	elif a==3:
		d=os.system("cal")
		print(d)
	elif a==4:
		bank_app()
		
	else:
		print("you know nothing johnsno")

main()
