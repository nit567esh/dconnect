# **dconnect** 
#### Power your data connections with python and query with dconnect
#
**dconnect** is a lightweight data source connector wrapper for different databases, User can also perfom queries and will get data.
#### Available datasources campactibility:
*SQLite, MySQL, SQL Server, Azure SQL, PostgreSQL, Redshift, Snowflake, Clickhouse, Oracle, IBM_Db, Vertica, MongoDB, AWS S3 Bucket, GoogleSheets, Elasticsearch, Google Analytics, Neo4j*
### Installation
#### Installation from Git
Clone repository using below command
```sh
git clone https://github.com/nit567esh/dconnect.git
```
Go to python package folder and use below command to install the package into library location:

```sh
$ cd <pkg_directory>
$ python3 setup.py install
```
#### Installation from Pypi
Install directly from Pypi using below command
```sh
pip install dconnect 
or
python3 -m pip install dconnect
```
### Usages
In order to use dconnect, use below steps
1. Download [credentails.json](https://github.com/nit567esh/dconnect/blob/master/credentails.json) file.
2. Configure the required connection using the credentails.json template.
3. Store it somewhere in safe folder.
4. Use below commands to run your dconnect
```sh
>>> import dconnect as c
>>> conids = c.conids('path_of_your_saved_credentails.json')
>>> print(conids) # Choose any connection id from list to validate the connection
>>> con = c.connect('your_connection_id(dsidentifier key in credentails.json)')
>>> df  = c.runsql(con, 'show tables;')
```
**Functions:**
1. List configured connection IDs
```sh
>>> import dconnect as c
>>> conids = c.conids('path_of_your_saved_credentails.json')
>>> print(conids)
```
2. Connect using a conid
```sh
>>> con = c.connect('<your_connection_id>')
```
2. You can only run SQL queries incase on Relational DBs/DWs connection object.
```sh
>>> df = c.runsql(con,'<Sql-Query>')
```
#### Examples:
**1. For Relational DBs/DWs**
```sh
>>> con = c.connect('redshift_<host>_<database>')
>>> df = c.runsql(con,'select top 10 * from edw.dim_product')
```
**Note** - Same is applicalble for the following list of DBs: *SQLite, MySQL, SQL Server, Azure SQL, PostgreSQL, Redshift, Snowflake, Clickhouse, Oracle, IBM_Db, Vertica* 

**2. For Others**

Function **runsql** is only applicable to relational DBs/DWs. For other data source dconnect only allow to connect with data source and for query purpose you can ues the respective generic packages using the connection object initilized by dconnect.

*Google Sheet Example*
```sh
>>> con = c.connect('gsheet_<username>@gamil.com') # using dconnect
>>> sh = con.open("<GsheetName>") # using pysgsheets
>>> wks = sh.worksheet_by_title("<GsheetTab>")  # using pysgsheets
>>> df = wks.get_as_df()  # using pysgsheets
```

| DataSource|Pythob Pkg|GitRepo|Pypi|Dependencies|
|:---------:|:--------:|:-----:|:--:|:------:|
|Google Sheet|pygsheets| https://github.com/nithinmurali/pygsheets  | https://pygsheets.readthedocs.io/en/stable/ |client_secret json file|
|Google Analytics|google2pandas| https://github.com/panalysis/Google2Pandas  | https://pypi.org/project/Google2Pandas/ |client_secret json file, token file|
|GoogleAds|googleads| https://github.com/googleads/googleads-python-lib  | https://pypi.org/project/googleads/ |client_secret json file|
|AWS S3|boto3| https://github.com/boto/boto3  | https://pypi.org/project/boto3/ ||
|Mongo DB|pymongo| https://github.com/mher/pymongo  | https://pypi.org/project/pymongo/ ||
|Elasticsearch|elasticsearch| https://github.com/elastic/elasticsearch  | https://pypi.org/project/elasticsearch/ ||
|Neo4j|neo4j| https://github.com/neo4j  | https://pypi.org/project/neo4j/ ||

### Todos
 - REST API, FTP, SFTP, Google Adsense/Manager/Search Console, Mixpanel, Hive, HDFC, Apache Kylin, Apache Druid and many more
