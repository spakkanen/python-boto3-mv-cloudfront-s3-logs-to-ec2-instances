# Amazon Web Services (AWS) SDK for Python S3 and using CloudFront logs

Connect to S3 via Boto3. Boto is the Amazon Web Services (AWS) SDK for Python.

Fetching CloudFront log files. You can be analysed log files by downloading the files to the EC2 instance. This Python script does the following:

* Reads bucket name as the first argument.
* Saves CloudFront log files to the EC2 instance as the second argument.
* Combines the gzipped (gz) log files into a single date file.
* Decompresses the file.
* Removes comments.
* Removes S3 CloudFront logs.

## Getting Started

You can install Python version 3+ and Boto3 library. And all things will be done in few minutes.

### Installing

If your haven't installed Python with Boto3, you have to install.

Server system on Unix platforms:

```
sudo -i
yum -y install python36
pip install boto3
```

Using Boto3

After installing boto3. You can use it to configure your credentials file:

### Basic Configuration

You need to set up your AWS security credentials before run as Python script.

```
aws configure
```

Alternatively, you can create the credential file yourself. By default, its location is at ~/.aws/credentials:

```
[default]
aws_access_key_id = <YOUR_AWS_ACCESS_KEY>
aws_secret_access_key = <YOUR_AWS_SECRET_KEY>
```

## How to fetch Python code

You can clone this repository.

```sh
$ git clone https://github.com/spakkanen/python-boto3-mv-cloudfront-s3-logs-to-ec2-instances.git
$ cd python-boto3-mv-cloudfront-s3-logs-to-ec2-instances
$ python mv_s3_all_files.py <S3_BUCKET_NAME> <WORK_PATH>
```

## Connect to S3 services

This Python application connects to the AWS S3. Script fetch CloudFront log files.

	python mv_s3_all_files.py <S3_BUCKET_NAME> <WORK_PATH>

## Cron schedule

You should to set up automatically run Python scripts on a schedule.

Schedule syntax is normal Unix cron/crontab syntax for examples:

```sh
2,12,22,32,42,52 * * * * python /root/python-boto3-mv-cloudfront-s3-logs-to-ec2-instances/mv_s3_all_files.py <S3_BUCKET_NAME> <WORK_PATH> > /dev/null
# Removes all files older than 2 weeks.
02 04 * * * find /root/python-boto3-mv-cloudfront-s3-logs-to-ec2-instances/cloudfront_prod1/ -mtime +14 -type f -exec rm -f {} \;
```

## Read the log files

The log file is a UNIX standard format and that's easy using and read UNIX tools.

Find main page links (/) amount from current date log files.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t/\t' | wc -l
	
Find all main page links.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t/\t' | cut -f 5 | sort | uniq -c | sort -nr | head -n10

Find all 404 error links.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t404\t' | cut -f 5 | sort | uniq -c | sort -nr | head -n10

## Contributing

Contributions are welcome. Open an issue first before sending in a pull request. All pull requests review before they are merged to master.

## Contact

Please contact: saku@kliffa.fi .

## Workgroup

### Member

| Member Name |GitHub Alias|Company| Role |
| --- | --- | --- | --- |
| Saku Pakkanen | [@spakkanen] (https://github.com/spakkanen) | [Cybercom Finland Oy / Kliffa.fi] (https://kliffa.fi/en/) | Committer |