import boto3                                                                                                              
from random import choice                                                                                                 
import sys                                                                                                                
                                                                                                                          
                                                                                                                          
                                                                                                                          
def get_iam_client_object():                                                                                              
   session=boto3.session.Session(profile_name="root")                                                                
   iam_client=session.client(service_name="iam",region_name="us-east-1")                                                 
   return iam_client   

def get_random_pass():
   len_pass = 8
   valid_chr="qwertyuiopasfghjklzxcvbnm!@#$%^&*()1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
   return "".join(choice(valid_chr) for each in range(len_pass))

                                                                                                               
def main():                                                                                                               
   iam_client=get_iam_client_object()                                                                                     
   Iam_user_name="sandy984@gmail.com"                                                                                 
   password = get_random_pass()                                                                       
   PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"                                                                
   try:                                                                                                                   
      iam_client.create_user(UserName=Iam_user_name)                                                                      
   except Exception as e:                                                                                                 
      if e.response['Error']['Code']=="EntityAlreadyExists":                                                              
          print("Already Iam User with {} is exist".format(Iam_user_name))                                              
          sys.exit(0)                                                                                                     
      else:                                                                                                               
         print("Please verify the following error and retry" )                                                             
         print(e)                                                                                                          
         sys.exit(0)                                                                                                      
   iam_client.create_login_profile(UserName=Iam_user_name,Password=password,PasswordResetRequired=False)                                                 
   print("IAM User Name={} Password={}".format(Iam_user_name,password))                                                                         
                  
   iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)                                                                                        
   return None                                                                                                            
                                                                                                                          
if __name__=="__main__":                                                                                                  
    main()