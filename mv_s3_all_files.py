import botocore
import boto3
import sys
import os
from datetime import date

def print_help():
  print("Usage: python mv_s3_all_files.py")
  print("Remark: This script removes also original S3 CloudFront logs.")
  sys.exit(0)
  
if len(sys.argv) == 1:
  print("Enter S3 bucket name. Usage: python mv_s3_all_files.py <S3_BUCKET_NAME> <WORK_PATH>")
  print("Remark: This script removes also original S3 CloudFront logs.")
  sys.exit(0)
if len(sys.argv) == 2:
  print("Enter S3 work directory. Create S3 files in directory WORK_PATH. Usage: python mv_s3_all_files.py <S3_BUCKET_NAME> <WORK_PATH>")
  print("Remark: This script removes also original S3 CloudFront logs.")
  sys.exit(0)
  
bucketname = sys.argv[1]
workpath = sys.argv[2]

# Initialize.
s3 = boto3.resource('s3')
# Select the bucket.
bucket = s3.Bucket(bucketname)

# Get current date.
today = date.today()
today = today.strftime("%Y%m%d")
# Get current full path.
fullpath = os.path.dirname(os.path.abspath(__file__))

isLogFileRead = False

# Download all files from S3.
def download_s3_all_files():
  if not os.path.isdir(workpath):
    os.mkdir(workpath) 
  
  try:
    for s3_object in bucket.objects.all():
	    path, filename = os.path.split(s3_object.key)
	    bucket.download_file(s3_object.key, workpath+"/"+filename)
	    s3.Object(bucketname, s3_object.key).delete()
  except botocore.exceptions.ClientError:
    print("Access Denied Error when calling the ListObjects (Action: S3:ListBucket) operation.")
  except PermissionError:
    print("Permission Denied Error: '"+workpath+"/"+filename+"'.")

# Gunzip all files.
def extract_all_files():
  for root, dirs, files in os.walk(workpath):
    for filename in files:
      if filename.endswith('.gz'):
        #print("gunzip "+workpath+"/"+filename)
        os.system("gunzip "+workpath+"/"+filename)
        read_parse_log_file(workpath+"/"+filename[:-3])
	  
# Read a log file.
def read_parse_log_file(filename):
  isLogFileRead = False
  f = open(filename, "r")
  for row in f:
    try:
      cols = row.split('\t')
      date = cols[0]
      time = cols[1]
      csip = cols[4]
      csmethod = cols[5]
      csuristem = cols[7]
      scstatus = cols[8]
      csuseragent = cols[10]
      xedgeresulttype = cols[13]
      timetaken = cols[18]
      isWriteFileEnabled = write_log_to_file(date,time,csip,csmethod,csuristem,scstatus,csuseragent,xedgeresulttype,timetaken)
      if not isWriteFileEnabled:
        break
    except IndexError:
      print()
  f.close()
  
# Read the last line.
def read_last_line(filename):
  f = open(filename, "r")
  lines = f.readlines()
  lastline = lines[-1]
  f.close()
  return lastline

# Split a log row.
def split_log_line(line):
  try:
    cols = line.split('\t')
    return cols
  except IndexError:
    return []

# Write log to a file.
def write_log_to_file(date,time,csip,csmethod,csuristem,scstatus,csuseragent,xedgeresulttype,timetaken):
  if not os.path.isdir(fullpath+'/logs'):
    os.mkdir(fullpath+'/logs')
  logfilename = date.replace('-','')

  global isLogFileRead

  isWriteFileEnabled = False
  if isLogFileRead:
    isWriteFileEnabled = True
  else:
    if today == logfilename:
      if os.path.isfile(fullpath+'/logs/'+logfilename+'.log'):
        # Check whether this row already has written.
        lastline = split_log_line(read_last_line(fullpath+'/logs/'+logfilename+'.log'))
        lasttime = lastline[1]
        if date == lastline[0] and time[0:4] != lasttime[0:4]:
          isWriteFileEnabled = True
      else:
        isWriteFileEnabled = True
    else:
      if not os.path.isfile(fullpath+'/logs/'+logfilename+'.log'):
        isWriteFileEnabled = True
	
  # Now is write to a file is enabled.
  if isWriteFileEnabled:
    isLogFileRead = True
    print("Writing a new row: "+date+"\t"+time+"\t"+csip+"\t"+csmethod+"\t"+csuristem+"\t"+scstatus+"\t"+csuseragent+"\t"+xedgeresulttype+"\t"+timetaken+"\n")
    f = open(fullpath+'/logs/'+logfilename+'.log', "a")
    f.write(date+"\t"+time+"\t"+csip+"\t"+csmethod+"\t"+csuristem+"\t"+scstatus+"\t"+csuseragent+"\t"+xedgeresulttype+"\t"+timetaken+"\n")
    f.close()
	
  return isWriteFileEnabled

# List all log files.
def list_all_log_files():
  files = os.listdir(workpath)
  fileslist = [os.path.join(workpath,i) for i in files]
  filessort = sorted(fileslist, key=os.path.getmtime)
  for filename in filessort:
    print(filename)


download_s3_all_files()
extract_all_files()
# Debug.
#read_parse_log_file(workpath+"/"+'E3DZ6YCX50HAEO.2020-11-02-07.e023a326')
#list_all_log_files()

sys.exit(0)
