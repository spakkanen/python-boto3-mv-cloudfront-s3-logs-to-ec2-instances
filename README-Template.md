# Connect to S3 via Boto3. Boto is the Amazon Web Services (AWS) SDK for Python.

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

```
aws configure
```

Alternatively, you can create the credential file yourself. By default, its location is at ~/.aws/credentials:

```
[default]
aws_access_key_id = <YOUR_AWS_ACCESS_KEY>
aws_secret_access_key = <YOUR_AWS_SECRET_KEY>
```





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

