# FPgrowth
Finding association rules for a market dataset

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li> <a href="#about-the-project">Project Description</a></li>
    <li><a href="#getting-started">Dependencies</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Project Description

### Algorithm
The reository provides the implementation of FPgrowth algorithm in pyspark. The purpose of this project is to find sets of items that are often or rarely sold together.
In order to analyze our market basket we can use some algorithms like Apriori or FPgrowth. 
* Apriori algorithm
	Apriori is one of the algorithms that is used for pattern mining. Apriori algorithm depends on the frequencies of itemsets. It generates different tables including various items' combinations. To find the frequencies, the algorithm scans the database multiple times. There are two main disadvantages for Apriori:
	1. The size of candidate itemset could get large
	2. High cost because of scanning database over and over again
You can read more about Apriori [here](https://www.softwaretestinghelp.com/apriori-algorithm/)

* FPgrowth algorithm (Frequent Pattern Growth algorithm):
	FPgrowth is a more efficient and faster algorithm in comparison with Apriori. It compressed database into a tree called FP tree. FP tree structure reserves the itemset while keeps track of the association between itemsets. Frequent Patterns are generated from the Conditional FP Tree.
As we are going to implement FPgrowth for our dataset, we need to explain some more details about the function parameters.
We use FPgrowth from apache spark:
  ```sh
  import org.apache.spark.ml.fpm.FPGrowth
  ```
We need to set some hyper parameters for our function (the most important ones):
1. minSupport: the minimum support for an itemset to be identified as frequent. For example, if an item appears 3 out of 5 transactions, it has a support of 3/5=0.6. 
2. minConfidence: minimum confidence for generating Association Rule. Confidence is an indication of how often an association rule has been found to be true. For example, if in the transactions itemset X appears 4 times, X and Y co-occur only 2 times, the confidence for the rule X => Y is then 2/4 = 0.5. [source](https://george-jen.gitbook.io/data-science-and-apache-spark/fp-growth)

You can read more about FPgrowth algorithm [here](https://www.softwaretestinghelp.com/fp-growth-algorithm-data-mining/) 

### Data
As a data we are given the purchase history of transactions over time for H&M products.
Data can be downloaded from [kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data)
We need to download two datasets:
1. **transactions_train.csv** which contains date, customer ids and the purchased articles.
2. **articles.csv** which contains the information of all articles such as name, color, code, and so on.  



<!-- GETTING STARTED -->

### Dependencies

* install spark and pyspark 

* install jupyter notebook


<!-- USAGE EXAMPLES -->
## Usage

The folder data/ contains the configuration file and generated csvs during the process. You need to download datasets that were mentioned above and extract them here. All the other files except conf.yaml will be created during the process. 


**1. dataPreparation.ipynb** 
This script should be run after downloading and extracting datasets. In this part of code we preprocess data and do some data analyzation to get a sense of our datase.
We save a csv file from shopping baskets(they contain products that were purchased together by each customer).

**2. fpgrowth.py**
This script reads the csv file that is produced in the previous step. The reason of seperating codes is to increase efficiency and deal with memory limitations on the personal PC.
The itemsets are fed into the FPgrowth algorithm and the result is a csv containing the products that could be bought together with a specific confidence (association rules).
hyperparameters:
1. minsupport: 0.0001 (Because of memory shortage I set it to 0.0001. However, I think 0.00001 is a better choice as the bigger minsupport can throw away more data.)
2. minconfidence: 0.001

**3. AssociationRules**
Last step is to check for association rules that we extracted in the previous step. In this part of code we map the article ids to names of products.


**Note**
In the case that you are not able to install spark, you can check the association rules in last script. The output result of the second step is already available in the folder data. If you run first and second steps, the files will be overwritten.

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTACT -->
## Contact

Sara Mirzavand Borujeni - sarah.mb@outlook.com

Project Link: [https://github.com/Sara-mibo/FPgrowth](https://github.com/Sara-mibo/FPgrowth)

<p align="right">(<a href="#top">back to top</a>)</p>


