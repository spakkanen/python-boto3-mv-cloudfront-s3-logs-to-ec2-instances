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

	python mv_s3_all_files.py <S3_BUCKET_NAME> <DIR>

## Read the log files

The log file is a UNIX standard format and that's easy using and read UNIX tools.

Find main page links (/) from current date log files.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t/\t' | wc -l
	
Find all main page links.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t/\t' | cut -f 5 | sort | uniq -c | sort -nr | head -n10

Find all 404 error links.

	cat logs/$(date +"%Y%m%d").log | grep -P '\t404\t' | cut -f 5 | sort | uniq -c | sort -nr | head -n10

# CRONTAB AJASTIN!
LOPPUUN KIRJOITUS TYÖSKENTELYSTÄ JA KLIFFA.fi
# ESITTELY JOLLAIN:
Jeff Barr

Jeff Barr is Chief Evangelist for AWS. He started this blog in 2004 and has been writing posts just about non-stop ever since.

KERRO OHJEESSA, ETTÄ TÄTÄ TÄYTYY AJAA 10 Min. välein.



```
mkdir -p /opt/www
cd /opt/www
git clone https://github.com/spakkanen/kliffa-booking-platform.git
```

## Running the Tests

You can run test in Perl code complited carry on check  the syntax of the script.

```
perl -cw /opt/www/kliffa/cgi-bin/login/index.cgi
```

## Database MySQL or MariaDB

If your haven't installed Database, you have to install.

Create database.

```
CREATE DATABASE kliffa CHARACTER SET = 'utf8' COLLATE utf8_general_ci;
```

Add users of database.

```

```

```
```


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Bugs & Issues

Please feel to report any bugs or issues to us, email to: saku.pakkanen@gmail.com.

## License

Copyright (C) 2016 - 2019 Saku Pakkanen.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

