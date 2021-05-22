# Importing required libraries
import os, sys, pandas, json, urllib.parse, requests, certifi

# Available connection ids function
def conids(path=None):
    global data
    data = json.load(open(str(path)))
    conids=[]
    for i in data.keys():
        for j in data[i]:
            conids.append(j['dsidentifier'])
    return conids

# Connection function
def connect(conid=None):
    df = pandas.json_normalize(data[str(conid).split('_')[0]])
    df = (df[(df['dsidentifier'] == conid)]).reset_index()
    
    if conid.split('_')[0].lower() in ('redshift', 'postgresql'):
        import psycopg2
        con = psycopg2.connect("dbname='"+str(df['db'][0])+"' port='"+str(df['port'][0])+"' user='"+str(df['user'][0])+"' password='"+str(df['pswd'][0])+"' host='"+str(df['host'][0])+"'")       
    
    elif conid.split('_')[0].lower() in ('snowflake'):
        import snowflake.connector
        con = snowflake.connector.connect(user=df['user'][0], password=df['password'][0], account=df['account'][0], warehouse=df['warehouse'][0], database=df['database'][0],)
        
    elif conid.split('_')[0].lower() in ('clickhouse'):
        from clickhouse_driver import Client
        con = Client(database=df['db'][0], host=df['host'][0], port=df['port'][0], user=df['user'][0], password=df['pswd'][0])        
        
    elif conid.split('_')[0].lower() in ('azuresql', 'sqlserver'):
        import pyodbc
        con = pyodbc.connect(driver=str(df['driver'][0]),server=str(df['host'][0])+','+str(df['port'][0]),database=str(df['db'][0]),uid=str(df['user'][0]),pwd=str(df['pswd'][0]))
    
    elif conid.split('_')[0].lower() in ('mysql'):
        import pymysql
        con = pymysql.connect(host=str(df['host'][0]),port=int(df['port'][0]),user=str(df['user'][0]),password=str(df['pswd'][0]),db=str(df['db'][0]))
    
    elif conid.split('_')[0].lower() in ('mongodb'):
        from pymongo import MongoClient
        con = MongoClient(str(df['url'][0]))
        
    elif conid.split('_')[0].lower() in ('gsheet'):
        import pygsheets
        pwd = os.getcwd()
        path = str(df['path'][0])
        file = str(df['client_secret_file'][0])
        os.chdir(path)
        con = pygsheets.authorize(file)
        os.chdir(pwd)        
        
    elif conid.split('_')[0].lower() in ('googleanalytics'):
        import google2pandas
        pwd = os.getcwd()
        path = str(df['path'][0]) 
        file = str(df['client_secret_file'][0])
        token_file = str(df['token_file'][0])
        os.chdir(path)
        con = google2pandas.GoogleAnalyticsQuery(secrets=file, token_file_name=token_file)
        os.chdir(pwd)
        
    elif conid.split('_')[0].lower() in ('googleads'):
        import sys,locale,_locale
        from googleads import adwords
        _locale._getdefaultlocale = (lambda *args: ['en_US', 'UTF-8'])
        pwd = os.getcwd()
        path = str(df['path'][0])   
        file = str(df['client_secret_file'][0])
        os.chdir(path)
        con = adwords.AdWordsClient.LoadFromStorage(file)
        os.chdir(pwd)

    elif conid.split('_')[0].lower() in ('awss3'):
        import boto3
        con = boto3.client('s3', aws_access_key_id=str(df['access_key'][0]),aws_secret_access_key=str(df['secret_access_key'][0]))
    
    elif conid.split('_')[0].lower() in ('ftp'):
        import pysftp
        from ftplib import FTP
        con = FTP(str(df['host'][0]))
        con.login(user=df['user'][0], passwd = df['pswd'][0])
    
    elif conid.split('_')[0].lower() in ('sftp'):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        con = pysftp.Connection(str(df['host'][0]), username=str(df['user'][0]),password=str(df['pswd'][0]),port=int(df['port'][0]),cnopts=cnopts)
    
    elif conid.split('_')[0].lower() in ('elasticsearch'):
        import elasticsearch
        if str(df['security'][0])=='http':
            con = elasticsearch.Elasticsearch(str(df['host'][0]),http_auth=(str(df['user'][0]), str(df['pswd'][0])),port=int(df['port'][0]),)
        elif str(df['security'][0])!='https':
            con = elasticsearch.Elasticsearch(str(df['host'][0]),http_auth=(str(df['user'][0]), str(df['pswd'][0])),port=int(df['port'][0]),use_ssl=True,verify_certs=True,ca_certs=certifi.where(),)

    elif conid.split('_')[0].lower() in ('neo4j'):
        import neo4j
        con = neo4j.GraphDatabase.driver(str(df['uri'][0]), auth=(str(df['user'][0]), str(df['pswd'][0])))

    elif conid.split('_')[0].lower() in ('restapisearchmetric'):
        response = requests.post(str(df['endpoint'][0]), data={'grant_type': 'client_credentials'},auth=(str(df['api_key'][0]), str(df['api_secret'][0])))
        con = json.loads(response.content)
        con = str(con['access_token'])
        
    return con

# Query function
def runsql(con=None,query=None):
    cur = con.cursor()
    cur.execute(query)
    try:
        result = pandas.DataFrame([tuple(t) for t in cur.fetchall()])
        columnname = [i[0] for i in cur.description]
        result.columns = columnname
        con.commit()
        return result
    except:
        try:
            con.commit()
            return cur.statusmessage
        except AttributeError:
            pass