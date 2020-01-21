# 365DaysOfLearning

## Day 0: Jan 1, 2020

**TIL**: Just setting up project and looking for Google Cloud Certified Professional Data Engineer syllabus on Linuxacademy
and found tool for create my own schedule it very awesome. This is my second time for learn in this course, first at Cousera.
My goal is to get that certificate for my first data learning path. I will focus learning on data engineering stuff.


**Thoughts**: Just doubt what will happen to my life at the end of this challenge. And it invole me a lot of tool for create my learning environment such Done for happbit tracking, Grammaly for check my grammar. When want to do good new thing in my life it require more power and self discipline like rocket leaving atmosphere.


## Day 1: Jan 2, 2020

**TIL**: Overall is foundation concept. 

* Data life cycle: Ingest => Store => Process => Visual order does matter. 
* Database Type such SQL, NoSQL.
* Batch and Streaming Data.
* GCS and way to import it just know it have service that ship more data such TB and encrypted HDD to google and will load to GCS
* Monitor and logging agent for unmanaged service.

**Thoughts**: I know some concept before but try to imagine it with real use case and try to don't stick with my early knowledge. And challenge on linuxacademy is very useful.


## Day 2: Jan 3, 2020

**TIL**: Cloud SQL thing.

* Overall of managed database service such CloudSQL, CloudSpanner, BigQuery, DataStore, Bigtable. And how to select them with criteria of
  * Structed or Unstructed data.
  * Relational or Non-relational
  * Workload Analytic
  * Holizontal Scale
  * Low latency
* Some Basic CloudSql such import, create, stop, disk capacity and disk throughput.
* SQL best pratice just 3 example
  * Normalize, more and small better that few and big.
  * Don't select *.
  * Use inner join rather than where.
* GCS as staging file 

**Thoughts**: I was just curious about what if I want to import hundreds of tables to CloudSql what and I think cloud console itself doesn't easy to do it. After googling it, found out in a document that needs to use gsutil and gcloud sql combined and write some script with for loop to do it.
[Ref](https://cloud.google.com/sql/docs/mysql/import-export/importing)

## Day 3: Jan 4, 2020

**TIL**: Datastore No-Ops

* When to use and not use it.
* Datastore organization it like compare word with SQL

| Relational    | DataStore     |
| ------------- | ------------- |
| Table | Kind  |
| Row  | Entity  |
| Column  | Property  |
| Primary Key | Key  |

* How to create entity, index, combinded index, and hierarchy.
* Index pitfall, Explode index.
* Stong and Eventually Consistent.
* Their query is like SQL and it very surprise me a lot. I thought it will like mongodb.

**Thoughts**: Why every product has its name, actually all concept is the same? The trick for remembering it is imagined with pictures and mapping it with old knowledge, in this case, is SQL.

## Day 4: Jan 5, 2020

**TIL**: BigTable

* Some history.
* BigTable Architecture, Design and Schema.
* Pitfall for design row key lead to hotspot.
* SST stand for sorted string table.

**Thoughts**: This make me a lot of time and curious and need to read it in their own google document and some deep technical (at lease for me) such as [SSTable](https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/) format, for sure I don't understand all technical deep dive detail but I found it very fun. About the recommend practice it always update
last time it said you can use hashed string as row key but this time it not recommend anymore so I need to refresh my knowledge with their [document](https://cloud.google.com/bigtable/docs/schema-design).

## Day 5: Jan 6, 2020

**TIL**: CloudSpanner, Architecture itself like Bigtable but it strong consistent and focus on horizontal scale rather than verticle like CloudSQL. Cover on topics.

* Architecture and Schema.
* Avoid hotspot.

**Thoughts**: It my first day for working after long holiday. And found a lot of interrupt so I cannot focus on topic long enough. So I must make an easy environtment to learn.


## Day 6: Jan 7, 2020

**TIL**: Do hand on for cloud Spanner and review all learned topic read everything via dossier. Try to quiz that I passed found out that I can't remember that question and it good for test my understanding again without memorize form last quiz, It pure understanding. I will take it again after 3, 7, 14 days.

**Thoughts**: It good for review conetent and take quiz again it make more clear understanding and make my memorize strong for recall those topic.


## Day 7: Jan 8, 2020

**TIL**: Intro to streaming data (aka unbounded data) and some challenge that require action in realtime such fraud detection. Sometime it shift storage and go to analytic to reduce latency. Example game, credit card transaction, traffic sensor it kind of infinite data and never end and from various source. And go back to read document about Bigtable, for now it can replicate across region but in video said it in beta.

**Thoughts**: Kind of slow progress and found out in morning is most suitable time to learn because it less interrupt for example, in evening sometime may have surpise event that I can't control and will end up with don't learning on plan.


## Day 8: Jan 9, 2020

**TIL**: Cover cloud pub/sub and a bit about kafka connector both source and sink. How to monitor unacked message and metric and how to troubleshoot and some common pitfall such as code not optimize for keep up with publish load and not correctly ack.

**Thoughts**: I used pub/sub as at my work and found this lesson improve me about how to troubleshoot and see that my subscriber is balance with my publish rate via stackdriver. And excited about kafka even it cover a bit of it, also surpise that can work together both pub/sub and kafka on same pipeline. Today after work I feel want to sleep but need to learn so I try hard to stay focus and make it complete for today. 


## Day 9: Jan 10, 2020

**TIL**: Try to help my college to deploy model on aws sagemaker and didn't work, its cli is not easy to use also document haha. Learn a bit about process data with batch and stream and dataflow that can solve challenge about unify batch and stream data and out of order data.

**Thoughts**: Both platform aws and gcloud their have some similar concept on tools. It will be cool if I can use both platform on full their capacity.

## Day 10: Jan 11, 2020

**TIL**: Learn about dataflow best pratice and look their handon and try to imagine to use it in real world. And concept how to handle late data.

**Thoughts**: Second learn make more clear or it depend on teacher or me in past, concept about watermark, window, trigger it not clear when I learn at cousera but learn this second time it more clear and find out it not complicate thing like a was thought.

## Day 11: Jan 12, 2020

**TIL**: Dedicate almost day to deploy my college model to sagemaker and it still doesn't work but I used other model and it work well. I learned how to use aws-cli to invoke model and use lambda and api gateway to send picture with base64 encode to predict with sagemaker. And found the way to train via sagemaker with pre-defined container. And learn a little concept for Dataproc.

**Thoughts**: I found my self very exciting to do ML stuff and I dedicate more time than usually. I think I like concept for watch and then do it with myself, I cannot remember the way to do it at first but I repeatly do it and can do it at the end.
But this technique require a lot of time per topic and I must have credit with that cloud for learn and play. My attention is go to aws so much, because it left more credit and I can learn anything I interest but it not good for my goal and I will back to google data engineer track. After got certified I will learn ML on aws as second course.


## Day 12: Jan 13, 2020

**TIL**: Learn about dataproc, concept about lift and leverage seperate between compute and storage. Just known that Hive and Hbase can move to store on BigQuery and Bigtable. Preemptible will not lost data on Dataproc but will lose on normal GCE suitable for more compute power and reduce cost.

**Thoughts**: This is suitable if you have Hadoop ecosystem but not me. Dataflow can do more and no overhead like Dataproc, as I known.

## Day 13: Jan 14, 2020

**TIL**: Learn about best pratice for dataproc such use cluster and storage in same region, add more disk size to increase disk performance because it actually network attached disk not actual disk. Add more preemptible node when face compute problem. And do lab with command and ui. Lastly, Quiz, with more confident but first time is 50% correct of 8 question kind of disappoint and another attempt until pass.

**Thoughts**: Problem for my quiz is I don't know IAM to much and hesitate between concept that overlab and some tool that I cannot remember it name 100% sure such as HIVE for BigQuery but I remember it Apache Impala but don't remember it just HIVE.
It very good to find my mistake early and I will improve that mistake. 

## Day 14: Jan 15, 2020

**TIL**: Learn a little about BigQuery Overview. It use for analytic for petabyte scale. And columnar store with good performance for read and not write and BQ not update just added and append.

**Thoughts**: My work is still on my head it make me loosing my focus when I need to concentrate to learning. So I just write everything in my head for work that pop up in my head and It make me clear my head and prepare for learning because I can't remember what detail in my head 100% so it good for write it down.

## Day 15: Jan 16, 2020

**TIL**: Learn how to import and export BigQuery just know it can read data form other such as Google Drive, Big Table just read not store in BQ. Some concept about views and cache. And review dataflow.

**Thoughts**: Sleep early will help me to have more time when morning and before sleep is suitable for just review thing I learn today.

## Day 16: Jan 17, 2020

**TIL**: Learn Bigquery Best practice and watch hand on abount query stream data. Learn concept for example Partition, Cluster and way to import multi TB scale with arvo file format and learn about nested for read performace and some monitor and logging via Stackdriver.

**Thoughts**: Try new learning method not pause just learn as smooth as possible and try to understand it. It good for not strugle when look for video but less confident that I know it 100%. I will test my understand via quiz tomorrow.

## Day 17: Jan 18, 2020

**TIL**: I join webinar about what is data engineer and learn that Apache Airflow (Cloud Composer) is very important tool for ETL tool. When I just curios how it different form Dataflow and found out it next level of Dataflow with have schedule time because in real life data pipeline is suppose to be automate and not manual and also have triggle condition when face senario not like cronjob but anytime that event occur. And suggest form webinar is when want to by data-engineer you need to get your hand dirty not just learn form video also tooling is move very fast better tool will come and you need to know it. I was pass quiz about Bigquery with one wrong answer. 

**Thoughts**: This learning method is work but I need to focus more on it. I will mix between new and old, don't slow my brain with pause so much and let it flow and review it again in different time. And suggest form webinar I will find my project to do it maybe coperate with my real work.


## Day 18: Jan 19, 2020

**TIL**: Still on BigQuery this time is do an hand on labs and then review what I learn about it and find more about partioning and clueter. And know about cardinality in database term is stress in high or low cardinaly, if high mean more unique and low is more repeat value in column.

**Thoughts**: When I review and don't understand it clear it good to find other resource to view it and make it clear. And found myself learn with explained picture is good for me and will better if I curious about that topic it by myself.


## Day 19: Jan 20, 2020

**TIL**: Learn about ML concept and type of it and learn how to prevent overfitting. Just know about L1 and L2 and when to use it. Try to apply knowledge to nn playground about L1 and L2 and found it work like I learned. 

**Thoughts**: Sometime I found myself want to know it deeply but I know it out of my certified scope so I need to focus about it and when I got it I will learn and play whatever I want, maybe I will struggle in some topic to deep and too long.

## Day 20: Jan 21, 2020

**TIL**: Learn AI platform on google cloud. Key concept and terminology such as models, version and jobs. And all pineline process about it.

* Preprocess Data
* Train
* Deploy
* Monitor
* Manage version

and just know about TPU.

**Thoughts**: It a bit of concept and nothing must but very excited when visit https://cloud.google.com/ai-platform/ and scroll down to Next'19 and it use kubeflow for ML pineline, It sound very interesting I will plan to include in to my daily learn. I feel very lucky to live in this era.
