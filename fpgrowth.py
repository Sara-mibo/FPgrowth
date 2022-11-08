'''
Usage:
spark-submit {--driver-memory 8g} fpgrowth.py --cpath {config file path} --dpath {data path}

Hyper_parameters:
1. minSupport: the minimum support for an itemset to be identified as frequent. For example, if an item appears 3 out of 5 transactions, it has a support of 3/5=0.6. 
2. minConfidence: minimum confidence for generating Association Rule. Confidence is an indication of how often an association rule has been found to be true. For example, if in the transactions itemset X appears 4 times, X and Y co-occur only 2 times, the confidence for the rule X => Y is then 2/4 = 0.5.

inputs: 
- list of itemsets saved as csv file
- configuration file

-output:
a csv file containing association rules 
'''
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.fpm import FPGrowth
from pyspark.shell import spark
import argparse
from pyspark.sql.functions import *
import yaml
from types import SimpleNamespace


def load_data(path,spark):
    # read data
    df=spark.read.options(delimiter=",",header=True).csv(path) 
    print(f'total number of itemsets:{df.count()}') 
    # convert strings of items to list of items  
    new_df=df.withColumn("itemset",  split("itemset",','))
    new_df= new_df.withColumnRenamed("itemset", "items")
    new_df=new_df.select(col('items'))
    return new_df





if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cpath", help="path of config file",default='data/conf.yaml')
    parser.add_argument("--dpath", help="path of data",default='data/itemsets.csv')
    args = parser.parse_args()
    # load config data
    with open(args.cpath, "r") as f:
        d = yaml.safe_load(f)
    cfg = SimpleNamespace(**d)
    # start spark session
    sc = SparkSession.builder.master("local1").appName("fpgrowth_new").getOrCreate()
    data= load_data(args.dpath,sc)    
    data.show()
    # Run FPGrowth and fit the model.
    fp = FPGrowth(minSupport=cfg.min_support, minConfidence=cfg.min_confidence)
    
    model = fp.fit(data)
    print('model is finished..........................')
    ##itemsets=model.freqItemsets
    # save rules in pandas df
    rules=model.associationRules
    model.associationRules.show()
    df_ruls=rules.select("*").toPandas()
    ##df_itemsets=itemsets.select("*").toPandas()
    data_path=args.dpath.split('/')[0]
    csv_path=data_path+'/rules_'+str(cfg.min_support)+'_'+str(cfg.min_confidence)+'.csv'
    df_ruls.to_csv(csv_path,index=False)
    print('data is saved................')
    sc.stop()
    ##df_itemsets.to_csv('freqitems.csv',index=False)
