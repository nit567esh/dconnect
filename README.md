# **dconnect** 
#### Power your data connections with python and query with dconnect
#
**dconnect** is a lightweight data source connector wrapper for different databases, User can also perfom queries and will get data.
#### Available datasources campactibility:
*sqlLite, MySQL, SQL Server, Azure SQL DB, PostgreSQL, Redshift, Snowflake, Clickhouse, Oracle, IBM_Db, Vertica, MongoDB, AWS S3 Bucket, GoogleSheets, Elasticsearch, Google Analytics, Neo4j*
#### Installation
**connection** requires below packages **dependencies**:
*pandas, psycopg2, pyodbc, pymysql, pymongo, pygsheets, boto3, pysftp, elasticsearch, certifi, google2pandas, neo4j*
##### Installation Commands
Clone from Bitbucket **package** repository using below command
```sh
git clone https://github.com/nit567esh/dconnect.git
```
Go to python package folder and use below command to install the package into library location:

```sh
$ cd <pkg_directory>
$ python3 setup.py install
```
### Usages
**Functions:**
*1. See available connection IDs*
```sh
>>> import connection as c
>>> c.conids()
```
*2. Connect using a conid*
```sh
>>> con = c.connect('<conid-string>')
```
*2. Run SQL quries incase on Relational DBs/DWs connection object & get data into pandas*
```sh
>>> df = c.runsql(con,'<Sql-Query>')
```
#### Examples:
**1. For Relational DBs/DWs**
```sh
>>> con = c.connect('redshift_redshiftprod.bold.com_supplydemand')
>>> df = c.runsql(con,'select top 10 * from edw.dim_portal')
```
**Note** - Same is applicalble for the following list of DBs: *MySQL, SQL Server, Azure SQL DB, PostgreSQL, Redshift* 

### Todos
 - Google Adwords, Mixpanel, Sisense integrations and many more
