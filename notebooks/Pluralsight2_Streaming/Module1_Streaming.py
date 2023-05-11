# Databricks notebook source
# MAGIC %md

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Spark Streaming
# MAGIC   * Spark Underlying Processing Engine

# COMMAND ----------



# Typical Pipelines do ETL 

# Data Source can be Structured or Unstructured or Streaming.

# Raw Data Stored in Data Lake, if it is Streaming Data it is ingested in Event Hub or Kafka

# Data Is lOaded to DW

# Two Types of Pipelines 
#   1. Batch
#   2. Streaming - work with infinite datasts, involves real-time data, Event Time is important, Process Data Continuesly
#       * For streaming, Monitor the application logs for system failures, track the deliveries
  
#   Streaming Applications does not mean Real TIme, it can be Near Real-time. Speed is important but don't need immediate output. 10 sec - 10 min
#   Ex (Near Real-time 10 sec - 10 min): Movie Recommmendations, Social Media Tracking, Application Monitoring, Weather Updates.

#   EX (Real Time 100 ms - 10 sec) : Fraud Detection, Self-Driving Cars, Online gaming, Network monitoring 

#   Complexities involved: 
#     1. Seperate batch & Stream Pipelines
#     2. Diverse Data sources & formats
#     3. Dirty / late arriving data
#     4. Run interactive queries on streaming data
#     5. Apply Machine Learning
#     6. Fault Tolerance

# This is where Apache Spark comes into play for above Complexities , It is open source. 


# Apache Spark in Memory Analytics Engine, for Unstructured, Structured and Real Time Data Processing
#     It is highly scalable
#     It Creates Unified Data Pipelines.

# What makes Apache Spark difficult to use?
#     1. Infrastructure Management
#     2. Manual Configuration
#     3. Upgrade Challenges
#     4. Tooling and Integration Complexity
#     5. Lack of UI
#     6. Difficuly to colleborate

# Therefore, Databricks Come into place because of Above Complexities
#     Databricks Completely managed and optimized platform for running Apache Spark
#     Provides whole bunch of tools out of box
#     It allows to create Infrastructure very easily.


# Spark + Databricks + Azure 

# COMMAND ----------

# RDD has 4 Feautures:
#     1. In-Memory
#     2. Partitioned - Data Partition Across Different Nodes
#     3. Read-Only - it means if you apply an operation it creates a New RDD. 
#     4. Resilient - Track their creation using Lineage Graph, therfore reconstructed in event of failure

# COMMAND ----------

# Spark Streaming
    # Set of APIs for batch and streaming processing. Spark SQL engine takes care of doing computation incrementally on streaming data
    # Use Dataframe APIs for stream processing language as well
    # Achieves end-to-end latencies as low as 100 ms

# COMMAND ----------

# Streaming
    # 1. Unbounded Dataset / Stream
    # 2. ETL Query - Sources, Transforms, Sinks 
    # 3. Execution Plan - Logical and Physical
    # 4. Trigger
    # 5. Checkpoint, Watermark, Windows, OutputMode and etc.

# COMMAND ----------

# reading from the source
# inputDF = spark.readStream.format("...").load()

# transform
# resultDF = inputDF.select(..).withColumn(..)

# load data
# resultDF.writeStream
#   .trigger(processingTime = '5 seconds')  -- specify stream interval  
#   .format("...").start()

# COMMAND ----------

# Two types of SPark Streaming Types
    # Spark Streaming
        # First Implementation
        # Works on RDDs
        # Seperate batch and streaming APIs

    # Spark Structured Streaming
        # Introduced with Spark 2.x
        # Works on Dataframes, highly optimized
        # Unified batch and streaming api
        # Modes:
            # Trigger(100ms)
            # Continuous(1 ms latency)

# COMMAND ----------

# Databricks
    # Infrastructure Management : Setup and scale an optimized Apache Spark environments
    # Collaboration : Workspace for Data Engineers, Data Scientists and Business Analysts

# COMMAND ----------

#Databricks 
    # 1. Cloud Services (AWS, Azure)
    # 2. DFS (Cluster comes pre installed DBFS, abstraction layer on Azure Storage)
    # 3. Runtime = Is a collection of core components run of Databricks Cluster, 
    # 4. Databricks I/O = Adds optimization related to : Caching, Disk read/write, File Decoding ...,, 50 Times faster Vanilla SPark Deployments
    # 5. Databricks High Concurrency = Shared Pool. Each user gets complete isolation and this improve the performance
    # 6. Runtime ML, built on top of Databricks Runtime. Pre Installed Libs , Tensorflow, Pytorch, Keras..
    # 7. Delta Lake. Open Source Storage Layer on Data Lakes, Features ACID Transaction support, Schema enforcement, Full DML Support, Time Travel, Audit History
    # 8. Workspace = Interactive Workspace (Explore and analyze data interactively. Visualize Data using Charts)
    # 9. Collaborate in real time
    # 10. Datbaicks Production (Can be run and deploy and schedule spark jobs), can monitor using logs and setup alerts.
    # 11. Security = Infrastructure Security (VM, )

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Single User 
# MAGIC   - No Fault Isolation
# MAGIC   - No task preemption

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Cluster Modes:
# MAGIC 1. Standart Mode
# MAGIC     1.1 Single User
# MAGIC
# MAGIC     1.2 No Fault Isolation (1 user Failure can affect other users)
# MAGIC
# MAGIC     1.3 No Task Premption (1 User work blocks)
# MAGIC
# MAGIC     1.4 Each user require Seperate Cluster
# MAGIC
# MAGIC     1.5 Support All Languages
# MAGIC
# MAGIC     1.6 Automated Cluster Only support Standart Mode, because only dedicated for that JOB.
# MAGIC
# MAGIC 2. High Concurrency Mode
# MAGIC     1.1 Multiple Users
# MAGIC
# MAGIC     2.2 Fault Isolation
# MAGIC
# MAGIC     2.3 Task Preemption - fair resource sharing
# MAGIC
# MAGIC     2.4 Maximum Cluster Utilization
# MAGIC
# MAGIC     2.5 Only supports Python, SQL, R, But not Scala

# COMMAND ----------

