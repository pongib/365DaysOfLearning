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

## Day 21: Jan 22, 2020

**TIL**: Watch hand on lab for tranin model on AI platform on gcp how to train, deploy and predict it just know deployed model is called version. Predict can be both batch and rest api. And learn concept of pretrain model such as vision api and just heard about data prevention for protect sensitive data that also kind of pretrain model. And concept of AutoML that combined pretrain and manual train together. LA have cloud playgroud that I will try tomorrow for do an hand on lab of ML learned today, It very cool if I can try anything on this playground, I hope I not be ban like qwicklabs earlier.

**Thoughts**: For today found LA have cloud playground that most exciting part for today. Tomorrow will try to figure it out how dynamic it is. And today I wake up early like I plan and learn on 4 pomodoro that quite suiatble but be sleepy :D.

## Day 22: Jan 23, 2020

**TIL**: Try hand on by myself and use this [instruction]() form LA to follow best part is I can use cloud sandbox for try any hand on I want but this have limit that I found is I install tensorflow via LA instrunction and it can't, maybe form restrict network itself so I can't use local train model. Sum-up topic that I learn today.

* Train, Deploy and Predict via instruction.
* Labeling Service on AI Platform first I thought it auto label form AI but it like mechanical turk.
* Read about [predict](https://cloud.google.com/ml-engine/docs/v1/predict-request) via rest api and found it url to call and [how to struct rest api](https://cloud.google.com/ml-engine/docs/scikit/getting-predictions-xgboost#get_online_predictions).
* Prediction and auto scale and when it don't have request it scale down to zero and no cost.

**Thoughts**: It so funny that I can try thing out of it scope and very enjoy cloud sandbox and will try use rest predict by my own on weekend.

## Day 23: Jan 24, 2020

**TIL**: Learn a little bit of datalab and how it share via cloud source repository. And use service accout user to use datalab.

**Thoughts**: Today try to eat before learn and it don't work as I expect, it require a lot of power to start after breakfast because interrupted by play facebook and game. So I will learn around 2 pomodoro first and will eat breakfast after.

## Day 24: Jan 25, 2020

**TIL**: Watch datalab demo. At first I thought it will more clear example for share between but not quite, just push to cloud source repository. The useful thing is demo and example about it and contain such as query via Bigquery and plot to graph. It very useful if to figure something out quickly.

**Thoughts**: Spend more time on relax stuff and it not quite good. This datalab tool is very cool if use between team but it start time is very slow.

## Day 25: Jan 26, 2020

**TIL**: Learn a bit of Dataprep concept and iam role with dataprep user and dataprep service agent.

**Thoughts**: I used to use this tool in qwiklabs quiz and it very amazing that I can do a via it UI. If I spend more time with hand on labs it will be help my understanding.

## Day 26: Jan 27, 2020

**TIL**: Watch dataprep hand on it very very useful and easy to use it can transform log file to structure data and save to BigQuery, very awesome. And learn a bit of Data Studio.

**Thoughts**: It transform receipt to dataflow and it quite complex when use pure dataflow. If I use this Dataprep fluently or any data wrangler tools it will be great on data engineer role because it will spend more time to preprocess data.

## Day 27: Jan 28, 2020

**TIL**: Data Studio concept and watch it hand-on and just know about cache and prefetch cache and then take quiz. Wrong answer on file type that support on dataprep that is DOC and I answer XLS(Excel).

**Thoughts**: This lesson not a hard topic and I will do hand on later It almost done I very excite to take a certified exam.

## Day 28: Jan 29, 2020

**TIL**: Cloud Composer both hand-on and concept, It kind of high level to control other service, Cloud Composer = Apache Airflow + K8S Cluster + GCS, and DAG workflow.
Read about 2 way ssl and learn that if you are server you need to gen root CA to make certificate and learn about Certificate revoke list (CRL) to reject client when call to server. 

**Thoughts**: I clear that why most tool on DE path is use Airflow it very helpful and I need to know other service that Airflow control as well. 2 way ssl is my doubt earlier but now I understand it more and I will do hand on tomorrow for better understand.

**Ref**: 
* [Useful gist and updated code](https://gist.github.com/pcan/e384fcad2a83e3ce20f9a4c33f4a13ae)
* [have CRL but old code style](https://engineering.circle.com/https-authorized-certs-with-node-js-315e548354a2#.24nmlit7w)
* [Visa documentation for use in real life](https://developer.visa.com/pages/working-with-visa-apis/two-way-ssl)
* [Other example](http://www.developerdave.co.uk/2014/10/two-way-ssl-node-js/)

## Day 29: Jan 30, 2020

**TIL**: Finish course Data Engineer on Linux Academy but not take final exam yet. Learn a bit about other resource to learn before take real exam such as gcloud solution and codelabs. At work I learn that count on sql in specific way can be affect other transaction with have lock command.

**Thoughts**: I will go to view other blog about pass exam and reverse it and see what I don't know and will plan to fill that gap.

## Day 30: Jan 31, 2020

**TIL**: Find other suggest about certificate and just think it worth to get my hand dirty before take exam because it will useless cert for me if I can do anything but I will both try pratice exam and do dirty hand for get better understand. Learn at work that I nearly forgot how to write code in parallel way I will try pratice it again on tomorrow.

**Thoughts**: It worth for me to admit my weakness and try to improve, even at first it very hurt.

## Day 31: Feb 1, 2020

**TIL**: Do first pratice exam on google official. I got 22/30 on this [link](https://docs.google.com/forms/d/e/1FAIpQLSfkWEzBCP0wQ09ZuFm7G2_4qtkYbfmk_0getojdnPdCYmq37Q/viewscore?viewscore=AE0zAgA_0OFhTQQZ0JJSpGQsb2ZLyt7XnWDl7_b7N_G80UWQ2N6Y9O85sQnypSgxvn1-8Gs) and lost 30$ on Toreba and got nothing but learn how to win ball crane.

**Thoughts**: Mostly I fail on thing I don't know and can't understand question well enough. Practice exam is hard that normal and make me read it very long time. I need to improve on speed will try to do more.

## Day 32: Feb 2, 2020

**TIL**: Review my last exam and explain why I go wrong also go right. I learn

* Analytic function on BQ. Its concept and function example LAG, LEAD, ROW_NUMBER, PARTITION.
* MID for google graph api.
* BQ default encoding is UTF-8.
* Text to speech api and synthesis option with normal and waveform and SSML for customize synthesis.
* NLP feature.
* Sync and async for Speech to text.
* BQ maximun 1 parition and 4 clustering per table.

**Thoughts**: I learn a lot form my mistake and it take me a lot of focus and time for it. If I do another exam it will repeat this cycle, I hope next time I will have more speed on this.

## Day 33: Feb 3, 2020

**TIL**: Search blog for people who pass DE exam and learn from them. In search and collect process I will analyzie it after I gathering it enough.

**Thoughts**: It great for do it backward for pass an exam. Focus on topic that other people pass and it make me clear what I must do next.

## Day 34: Feb 4, 2020

**TIL**: Search blog again but found something very useful that is [awesome gcp de](https://github.com/sathishvj/awesome-gcp-certifications/blob/master/professional-data-engineer.md) it gathering what I want to read. I found some of topic that I not familar with and I will list it all and then try to understand it.

**Thoughts**: I know it kind of tricky one, to pass the exam but real thing is waiting for me to use this skill for build something useful.

## Day 35: Feb 5, 2020

**TIL**: Try to do lab start with data studio and try connnect with cloud sql instead of BQ and found something very weried it don't have cache option not like it said in labs. Even connect datasource as BQ but not found cache option but I found data liveness period with default is 12 hour.  

**Thoughts**: What if I see this prefetch cache question in exam what should I do reflect what I saw or just answer what I learn from labs video.

## Day 36: Feb 6, 2020

**TIL**: Review BQ, Composer and Data Studio. Do a Composer lab I made mistake by thought that environment is just env in this context even I learn that composer step is create environment, create variable, create workflow. So environmemt in composer context is kind of instance or project name. I found it very slow for provisioning and update variable. And update variable in gcloud ui is not equal in airflow web ui, I thought it global but after try it is not. I try to use airflow to create BQ from DP result in my own case.

**Thoughts**: It very fun to use it and need more time to practice in real use case and it out of exam scope but very useful in DE career. 

**Ref** 
* [Composer Example](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/b80895ed88ba86fce223df27a48bf481007ca708/composer/workflows)
* [Hands on](https://github.com/pongib/la-labs/tree/master/composer)


## Day 37: Feb 7, 2020

**TIL**: Do Linux Academy final exam and get result at 82/100. Here what I made a mistake.
* Cannot remember minimum advice for use BigTable that is 1 TB.
* I not see keyword **specific**, Auto ML use for specific business scenario and Vision API for basic scenario.
* Don't understand context of **segment** just focus on filter.
* Just know Best practice for protect live customer data that is **separate project** for dev, staging and production and use CI for migrate data from one env to other env.
* Use PCollection before write to any resouce such as pub/sub.
* Trigger type is timestamp, Element count or combine both.
* Denormalized data in BQ not reduce amount of data process and also less storage space used.
* Storage Transfer Service is use for repeat or scheduled transfer.
* Transfer Appliance is for ***physical** and **petabyte scale**.
* Pub/sub is **global scope**

**Thoughts**: I thought my score is not much and I will learn to improve it but I spend time to do exam faster than official exam. My strategy for this is need to review all of my question after finish not let me think that question without mark for reviewed is fine. Tomorrow I will review why my right answer is right.


## Day 38: Feb 8, 2020

**TIL**: Do a little challenge on BigQuery via goo.gle/bqchallenge and learn IFNULL function and growth form year to year mean and how to calculate, it just divide by newYear/oldYear. And see my old exam that correct answer and remind me of IAM of dataflow, spanner and its concept such "NewSQL" and both consistency and scalability. And some best practice concept such as
* Use a service account for automated jobs.
* For security grant IAM on smallest scope resource as few as possible.
* Critical workload may require High Availability, don't focus on save cost too much.
and [chalk](https://www.npmjs.com/package/chalk) on npm is very cool.

**Thoughts**: It good for do an challenge and me not fear of it and turn out it very easy but I also learn from it, also learn from correct answer is make me subtle better.

## Day 39: Feb 9, 2020

**TIL**: Learn so much from P'Parin Talk about life cycle of work and how he increase their salary up to 50x from start but money is not the point mindset for work is better. It very worth for me to listen his talk. And learn intro about DE in prepare google DE exam in coursera. I will learn their content and do an pratice exam on that.

**Thoughts**: I will rethink about what I learn today and make it useful for my career path.

## Day 40: Feb 10, 2020

**TIL**: Learn a little bayes and prediction form netflix documentary. And watch case study that I hate to do it at first but for now when I understand all concept and then look it back it very help me understand big picture and I can think follow with teacher.

**Thoughts**: I think when I don't understand something it doesn't mean I fool but it mean I need know prior knowledge and it concept next time when I face situation like this I will go to foundation concept first. I think I spend less time for learning I need to spend it more.

## Day 41: Feb 11, 2020

**TIL**: Learn case study 2 and it not much. Try to figure it out what Data Fusion will use for, it use for build data pipeline with UI and can portable but I don't understand it so sure I will watch Google Next 2019 for further detail.
I just know the Touchstone concept that I very curious when you learn all basic concept then go to next step with glue all basic knowledge together, and it call Touchstone.

**Thoughts**: I think service like Data fusion it make me think google cloud is just managed open source project. Because it open source project that is core value and then surround with google service such as IAM and stack driver.

## Day 42: Feb 12, 2020

**TIL**: Learn a bit about data representation and some of data fusion.

**Thoughts**: I think I need to wake up early than this.

## Day 43: Feb 13, 2020

**TIL**: Review concept on widely topic
* Spark with transform with lazy evaluate and action.
* Eager evaluate on Tensorflow
* Use cluster propertie to config Hadoop on Dataproc
* Dataflow template for east to use with other user who non-coder.
* BigQuery limit stream with 100k rows/table/sec
* Bigtable with 100,000QPS @ 6ms with 10node.
* Single and Multi route for Bigtable for failover scenario.
* Suggest Bigtable Cpu for 70% with single route and 35% with multiple route for handle traffic from unavailable cluter in other region.
* Spanner and Bigtable increase node for better performance.
* In same performance for 100,000 QPS in Bigtable use 10 node but Spanner use 150 node and very expensive.
* It resonable to store data in Bigquery because it inexpensive.

**Thoughts**: I lose focus in early morning but I learn all the way to office and learn again when back to home. I want to pass certificate quickly becase I want to do stuff in real use case and I know thing that I learn about in Bigtable it not on exam but I want to know it when I face real life.

## Day 44: Feb 14, 2020

**TIL**: Try answer question on cousera but struck with BQ question, 
* just known that BQ dataset cannot direct move from one location to another location after created, it need to export to GCS with same location and copy from GCS old location to new one and then create BQ on that new location and import it.
* It can copy dataset to other project but in same location.

**Thoughts**: Just think that when I prepare for exam I lack a lot of progress becase I need to review the same thing over and over that make me feel depress sometime but for now I understand it. I see about new DE [path](https://google.qwiklabs.com/courses/1156) on GCP and [new course](https://www.coursera.org/learn/smart-analytics-machine-learning-ai-gcp) on coursera. WTF.

## Day 45: Feb 15, 2020

**TIL**: Learn various topic on DE course I know the service better than before and answer wrong about view in BQ so I need to learn from [document](https://cloud.google.com/bigquery/docs/share-access-views) and know about view in BQ better with Authorize view and IAM with bq.user and bq.dataviewer and share dataset.

**Thoughts**: I feel great when spend my time with learning not just lay on my bed.

## Day 46: Feb 16, 2020

**TIL**: Do a practice exam and got 76% that didn't pass but second attemp is 96% here what I do wrong.
* keyword one way and one time that I don't understand exactly.
* Upgrade form develop to production in Bigtable it can upgrade directly.
* Miss undertstand IOT core.
* Not read some keyword carefully such minimize query cost. I understand that minimize all cost.
And learn about interconnect such partner and dedicate.

**Thoughts**: Sometime it make me unconfident that I didn't pass it at first but I think it great that I fall early and learn a lot from it.

## Day 47: Feb 17, 2020

**TIL**: Learn from blog that other people who pass wrote. A lot of topic such as
* dropout is on of reguralize technique for prevent overfit that drop node in hidden layer.
* systhesis feature is cross feature.
* L1, L2 will better if use with big data set but with small cross validation is fine.
* embedding is technique for change discrete object to vector or real number for easy calculate for computer such as word to vector.
* A lot of quota question.
* concurrent query for Bigquery is 100 concurrent.
* update table is 1000 update/table/day.
* DML is data manipulate language such as UPDATE, INSERT, DELETE.
* DML support only transaction not multiple transaction.
* Can combine only UPDATE + INSERT, DELETE + INSERT, INSERT + INSERT other will be fail one and success one.

**Thoughts**: A lot of topic that cover and need to read a lot from documentation.

## Day 48: Feb 18, 2020

**TIL**: A lot of work at morinig so I just learn only [slot](https://cloud.google.com/bigquery/docs/slots) in BigQuery
* Slot is computation unit for do an query.
* Defind by complexity and size of query.
* If slot exceed it just queue. No need money to pay.
* Default slot is 2000.
* Query is transform to stage and put in DAG.
* Stage require slot to execute and evaluate slot by stage optimal parallelization, it pretty cool name.

**Thoughts**: Feeling want to sleep but need to learn something as I commited to myself.

## Day 49: Feb 18, 2020

**TIL**: A lot of work at morinig so I just learn only [slot](https://cloud.google.com/bigquery/docs/slots) in BigQuery
* Slot is computation unit for do an query.
* Defind by complexity and size of query.
* If slot exceed it just queue. No need money to pay.
* Default slot is 2000.
* Query is transform to stage and put in DAG.
* Stage require slot to execute and evaluate slot by stage optimal parallelization, it pretty cool name.

**Thoughts**: Feeling want to sleep but need to learn something as I commited to myself.

## Day 50: Feb 19, 2020

**TIL**: Retake official exam this time I got 28/30 one is missing another is forgot to answer.
* What I miss is dataproc best practice is job specific mean that one job one duty for exam Hadoop cluster do two duty is analytic and processing when lift and ship to dataproc, analytic on dataproc is one job and second is processing job.
* More accuracy and speed time but I didn't remember anything so much just new analysis.
* Thing to learn more is secondary index on Spanner and use case of slidding window

**Thoughts**: Feel more confident but need to pratice more.


## Day 51: Feb 20, 2020

**TIL**: Watch document about Spanner, Dataflow.
* Secondary index is just indexing on other column rather than primary key.
* It good when want to query by specific that data column
* Best way to create it is when create table.
* It need time to effect secondary index if create after created table.
* Learn about dataflow window.

**Thoughts**: Not much learn because of a lot of work.


## Day 52: Feb 21, 2020

**TIL**: A little knowledge of mesurement of confusion matrix
* Accuracy use for symetric data set.
* Precision and Recall for asymetric data set.
* Learn about compliant such as
* GDPR for legulate how to use, collect of customer data.
* HIPAA for health data.
* FedRamp for security assesment and authorize of cloud service.
* COPPA for protect data and online operate for child age under 13.

**Thoughts**: Another day for limit time for learn but try hard for learn something useful for certified exam.

## Day 53: Feb 22, 2020

**TIL**: Register for exam on 27/02/2020 hope me pass. And do practice around 70 question and read document about partition in Bigquery.

**Thoughts**: It quite heavy load on my brain when take an pratce exam but it still fuction.

## Day 54: Feb 23, 2020

**TIL**: I try an practice exam and learn from my mistake yesterday but today I fail my exam (76%) with a lot of mistake that I just know. I will reanalysis tomorrow. For now I know a lot of thing I don't know before.

**Thoughts**: I feel bad this time and it stress sometime but still optimistic I will learn a lot from this failure.

## Day 55: Feb 24, 2020

**TIL**: Got 90% on practice 3 in Whizlabs and learn some concept.
* Read key visualizer
* Dataproc scale and autoscale
* Datastore export via api or gcloud and recommend when schedule export via script deploy to APP Engine and use cron.
* TPU the best.
* If don't manual export Bigquery, just use Dataflow for export Bigquery.
* Stream limit is 100,000 row/table/project/sec. and byte size is 100 MB/sec of size and 10000 row per request and max row size 1 MB.

**Thoughts**: Feel good when got better score and need to review detail in LA.

## Day 56: Feb 25, 2020

**TIL**: Got 98% on practice test in Linuxacademy.
* Read key visualizer again and understand almost well.
* Wrong answer on dataproc with HDFS storage and preemtible.
* Join data hero talk and learn a lot from it.
Data hero talk make me more clear some path of Data career and interest path is DS.
I know good question to ask myself when want to modeling something and I think it pretty good way to approach.

**Thoughts**: I think it because of instructor make it so funny and practicle every role is important.

## Day 57: Feb 26, 2020

**TIL**: The day before take exam I review all what I learn.
Also, learn UDF in Bigquery and Bigtable use case for single and multi cluster route.
I learn above topic because I failed pratice exam with 76% I need 1 more correct answer but I didn't.

**Thoughts**: I think that tomorrow I will pass exam or not because my last exam it go didn't well.

## Day 58: Feb 27, 2020

**TIL**: I write this with intention for delay gap with 2 days because I will mark it as milestone for my career.
I did pass real Google data enginner exam. I learn life lesson 3 thing.
* If I work hard in right way, I must success.
* Time in some period is very important. I almost lose all my dedicated if I go to take exam late.
* Accidents always happen be prepare!.

**Thoughts**: I feel very good that I get what I want. For now I need to look forward to next subject to learn and that is PYTHON!.

## Day 59: Feb 28, 2020

**TIL**: Read document and try hands on  to cloud endpoints.
* How to deploy both config and backend service.
* How to use default domain and custom domain.
* View log.
* Its overall concept.

**Thoughts**: It part of my work but I never do it before. I think it very fine grain and very code heavy.

## Day 60: Feb 29, 2020

**TIL**: Plan for learn python Here is my path.
* Start with Certified Entry-Level Python Programmer Certification in Linux Academy.
* Then take Introduction to Python Development and Programming Use Cases with Python both can be skip basic concept.
* Go to Datacamp and take python-programmer on career-tracks.
I will learn about Python develop and fundamental on Linux Academy and data relate on Datacamp such as pandas, numpy, mathplot.

**Thoughts**: This will take me a couple week to do and it will be fun with this language. 
My goal is to use this language as primary language and fluent it as much as I can.

## Day 61: Mar 1, 2020

**TIL**: I try to set my credential and linkedin page.
Write blog about my data engineer exam but not finish yet.

**Thoughts**: It not easy to write blog to other people for reading and easy to understand.
Need to curated list of topic carefully. Just doubt if I write blog very time, will I good at writing?

## Day 62: Mar 2, 2020

**TIL**: Write blog again and still not finish and learn that Medium not have anchor feature
I need to install extension. And learn Python but It not relate to any Python, mostly is editor.
* Remote Development for work with cloud sandbox.
* Sync setting for sync my setting to gist.

**Thoughts**: I used most of my time to write my blog it make a lot of afford but very fun.
I think it will finish tomorrow and hope it will useful for other people.

## Day 63: Mar 3, 2020

**TIL**: Complete my data engineer exam blog [here](https://medium.com/@pongtsu/%E0%B8%A3%E0%B8%B5%E0%B8%A7%E0%B8%B4%E0%B8%A7%E0%B8%AA%E0%B8%AD%E0%B8%9A-cert-google-data-engineer-%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%99%E0%B8%97%E0%B8%B3%E0%B8%87%E0%B8%B2%E0%B8%99-%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%A1%E0%B8%B5%E0%B8%AA%E0%B8%81%E0%B8%B4%E0%B8%A5%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99-data-788271fbfd50)
It require a lot of power to write but feel good when it done.
* Learn kubeflow 1.0 just read their blog and watch example but not try yet, will try on weekend.
* Know fact about diaper and beer legend, It fact it not look good like tale.

**Thoughts**: Story about diaper and beer is make me shcok that in the beginning everything is not look good like tale.
About blog is good to share with other but it make me a lot of effort, I will write again if I think it useful for other people. 

## Day 64: Mar 4, 2020

**TIL**: I use LA server for write python code via VSCODE and it very terible, very slow.
I will use docker in my local machine instead.

**Thoughts**: Noting much today I will find way to more effective with this learning.

## Day 65: Mar 5, 2020

**TIL**: Found that my macbook have python 3 installed so it very easy to run.
Mostly I use REPL to run. Here thing I learn about python today.
* Complier and Interpreter.
* Lexical like define token, Syntax is parse tree, Semantic is rule apply on tree.
* Python is Interpreter language that complied to byte-code before execute.
* Can change python file to executeable file with #!/usr/local/bin/python3 hello.py and chmod u+x hello.py
* Python don't have block comment in have only line comment with #.
* It object orient and have method like "Hello".lower() or "Hello".find("e")
* Both "" and '' is parse to ''.
* Very fun with "HA" * 4 will print "HAHAHAHA".
* Boolean is True and False with Capital letter at first.
* // is call floor divide, example 5 // 2 == 2.
* binary, octate, hex is represent with 0b1111, 0o17, 0xf all equal 15.
* can convert decimal to other with f'{15:b}' or bin(15) or f'{15:o}' or f'{15:x}'.

**Thoughts**: Sometime it very bore because it basic but some part that I don't know is very fun.
I like when I watch and then try to type follow lesson it help me to more understand and not bore.

## Day 66: Mar 6, 2020

**TIL**: Learn a bit about &, |, ^ (xor) in python. I already forgot how to do XOR.
Watch live about bacis NLP with word2vec, RNN, LSTM, Attention and a little on transformation with 12 attention.

**Thoughts**: Found it quite interest not in NLP subject but in their architect design of model.

## Day 67: Mar 7, 2020

**TIL**: Python basic.
* Learn about operator with order matter in python.
* Typecast such bool, int, str, float.
* Compare such "is" is from same memory address.
* Return order form "and" and "or" when it evaluated to True or False. For exam
* '123' and 0 and 1 will return 0 that evaluated to False.
* '123' and 1 and 1.23 will return 1.23 that the last and evaluated to True.
* int(1.23), int(1.89) will return 1.
* int('12.23') will return Error, WTF!
* Can't compare diffent type, for exam 'a' <= 123.
* ord('a') will return order of sting a.
* id('a') will return memory address of string a that is immutable.
* [] is not immutable, so [] is [] will return False.

**Thoughts**: I don't want to skip basic stuff even I know about but it will have subtle thing
that I don't know before.


## Day 68: Mar 8, 2020

**TIL**: Just learn a bit with print with end and sep option and input function.
* Use chalk and ora for spinner but didn't work well.

**Thoughts**: Just spend to much with those 2 lib for make it look pretty but not work like what I thought.


## Day 69 - 70: Mar 9 - 10, 2020

**TIL**: Forgot to commit in git but still learn I learn how to use slice in python
with string and list and how to use append and insert. String is immutable, it have
same address with same value if want new string value it must be new address but
list is mutable, it have same address with different value. Slice it have shorthand with
[start:end(not include):step] for exam [::] is take all 
* [2:10:3] is start with index 2 end with index 10 but not included and step with 2 char.

**Thoughts**: I never understand slice in python untill now it make me very happy and I'm not sure when I will forget it LOL.

## Day 71: Mar 11, 2020

**TIL**: Learn what is tuple and list in python.
* Tuple is immutable but List is mutable.
* Can have list in tuple and vice versa.
* List in List is called nested list and it is metric, len(my_metric) is rows and len(my_metric[0]) is column.
* List can sorted and reversed on item that same type.
* Reversed need to cast to list again.
* Also have index method.
* Can check item in List by use "'a' in my_list" or "'a' not in my_list".
* Tuple syntax is (1, 2, 3) or (4,).

**Thoughts**: Finally I understand tuple and it limitation.

## Day 72: Mar 12, 2020

**TIL**: Learn dictionary in python and Learn how to use auth0 with openapi.
* Learn method dict.keys() dict.values() dict.items() that return tuple in list of key value pair.
* Build dict with method dict(key=value, key2=value) and dict([('key', value)]).
* Key is immutable can be both string and tuple.
* Dict itself is mutable.

**Thoughts**: Spend so much time to understand auth0 and their audience in cliam.

## Day 73: Mar 13, 2020

**TIL**: Learn utf 8 in python and how to represent it and method to use with string.
* '\u2122' or '™' can use ord('™') or ord('\u2122') to watch code number.
* Can use chr(8482) to see what that unicode is.
* Learn split() and ','.join() to concat string in list or tuple.
* More method like isnumeric() or iswhatever and lower(), upper(), title(), capitalize().
* template string use with {} or use with {1}, have index but cannot combined.
* Sorted(list) when compare string it compare first char. Example ['This', 'is', 'a', 'book'] will be ['This', 'a', 'book', 'is'] becase 'T' < 'a' < 'b' < 'i'.
* Learn how to commit and push via gitlens in VSCODE but found out it not have commit and push LOL.

**Thoughts**: Some method not useful such as isnumeric, isdigit, isdecimal it return the same and can't use with '1.0' with period.

## Day 74: Mar 14, 2020

**TIL**: A little with if else statement. In python it else if with elif and after condition it must have : and indent need to equally.

**Thoughts**: Today not much learn because of Netflix LOL!

## Day 75: Mar 15, 2020

**TIL**: Learn how to use loop in python.
* While loop.
* For loop.
* Use range function to use certain range in for loop.
* Range use less memory than list because it use only needed and not store entire list.
* Can use if in loop but need to care about indent.
* Use break and continue for control loop.
* Can use else: when for or while loop. Useful in case for loop combine with break when need to search something.
* Pass is use for complete syntax in if else.
* Comprehension list is the best.

**Thoughts**: Like comprehension list very much.

## Day 76: Mar 16, 2020

**TIL**: Learn how to defined function and a bit about parameter and argument.
* Parameter is varible we define on function.
* Argument is value that assign when call function.
* Can have positional arguemnt, key value argument and mix.
* If use with key value argument, the rest must be key value argument not positional argument.
* Side effect is do something but not return value such as print in function but not return anything.

**Thoughts**: Not much today but still progess. And finally I know about different parameter and argument.

## Day 77: Mar 17, 2020

**TIL**: Learn how to import sequelize model via folder.

**Thoughts**: It a bit progress but take more time. It struck in my mind for longtime for understand it.

## Day 78: Mar 18, 2020

**TIL**: Learn how to use default parameter.
* If declare default parameter must follow with default parameter not alone paramter.
* Use recursive function.
* Create palindrome function.

**Thoughts**: It make me quite complex for me for create a palindrome but it very fun way to imagine and use my knowledge.

## Day 79: Mar 19, 2020

**TIL**: Learn generator in python.
* It kind of pause and resume concept and not require to run entire list.
* Useful when use with list and need high memory that normal loop can't do.

**Thoughts**: I compare myself with solution and found that I think way to much and didn't look at big picture.

## Day 80: Mar 20, 2020

**TIL**: Do generator lab and know about scope, global and shadow in python.

**Thoughts**: This is final episode of this course I will find way to know more about python.

## Day 81: Mar 21, 2020

**TIL**: Test pratice exam and pass with 82% LOL.
* Learn that list is reference on same address if I assign my_list2 = my_list
it will reference on same address if I remove value in my_list2 it will effect on my_list.
* Divide always return float.
* Mistake about not print at last or ask for value of variable that operate but didn't assign.

**Thoughts**: I found new course that associate level I will learn this course before go to Datacamp.

## Day 82: Mar 22, 2020

**TIL**: Learn lambda on associate course.
* Lambda it like anonymous function that take argument and execute one expression.
* Map, Filter, Reduce is higher order fuction.
* HOC is function that take function as argument and return function.
* Reduce is not build in it need to import form functools.

**Thoughts**: This time I use schedule for management my learning time I hope it will be good.

## Day 83: Mar 23, 2020

**TIL**: Learn how to use sorted with lambda.
* Or can use str.lower methon instead.
* Can access dict with d['name'] not d.name
* If use f'' make sure in expression didn't have ' in it.
* For example f'This is a d['book']' will error. Correct is
* f'This is a d["book"]' or f"This is a d['book']".
* Condition expression is short hand for if else. my_var = 20 if CONDITION else 28.
* Example: my_var = 20 if False else 28. my_var will equal 28.
* It useful when need to assign to value and don't write to much code.

**Thoughts**: I will not write untill I finish my schedule learning so sometime I will late to write to github. This time I forgot how to access dict LOL. I think lambda is very useful.

## Day 84: Mar 24, 2020

**TIL**: Mostly is create custom jwt in cloud endpoints and a bit of python.
* Service account can use with x509 or jwks with public link, no need to create our domain.
* x509 with https://www.googleapis.com/service_accounts/v1/metadata/x509/sa-name@gserviceaccount.com
* jwks with https://www.googleapis.com/service_accounts/v1/jwk/sa-name@gserviceaccount.com
* This methon is sign token with RS256.
* Do lab: Change from condition statement to  condition expression.

**Thoughts**: I think it will hard to create jwk public but it very easy with that gcloud support.


## Day 85: Mar 25, 2020

**TIL**: Review how to add domain and verify and use it with endpoint.
* A bit about API versioning.
* Everyting is about openapi.yaml and argument service at endpoint container in deployment.yaml.
* Not relate with DNS but require to check if dns is exist when deploy openapi.
* Learn how to import with python and name entity concept.
* Name entity in everything that can be name in that file.py.
* Such as function name, variable name. Can import and call or reference from that name.

**Thoughts**: Not learn python much I will try learn python first in tomorrow.

## Day 86: Mar 26, 2020

**TIL**: Learn import stuff in python.
* Import from module, package.
* Use ``__init__`` for handle export method.
* Search package or module order is build in -> path file.
* If not found in build in will look for path file.
* PYTHONPATH='absolute/path or realative path' python3 is way to add path for python to search specific module in other folder.
* Build in module will overwrite specific module.
* Since python3.3 it no need to create ``__init__`` for use package.
* Hidden module use with from module_name import *
* Hidden module is use ``__all__ = ['method name']`` of use underscore _method_name for private it.
* But can still access if use from module_name import that_private_method_name.
* Can excecute module as script with -m flag.
* Example python3 -m module_name
* ``__name__`` if it main script it will assign to ``__main__``.
* Other module will ``__name__`` as it file name.

**Thoughts**: So long about just import thing.

**Pomodoros**: 4

## Day 87: Mar 27, 2020

**TIL**: Mostly is gateway stuff.
* Read TYK updater and how to reload it with created file and call reload api.
* How to versioning endpoint in scenario compatible and incompatible.
* It can have multiple openapi file but need to deploy in one command.
* SDK execute multiple file to one file. But can have multiple version.
* Don't use same path name in different version.
* Create private and public path.
* CORS in endpoint but it apply to all path. If want more custom need to use nginx config.
* I think use cors in express layer is better.
* Just know that ESP with rollout_strategy='managed' is need to wait up to 5 min before config will applied.
* It recommend for use managed not specific config id.
* Just look video for python how to create package and how to install it public.

**Thoughts**: Spend more with gateway stuff when learn python at midnight it feel sleepy.

**Pomodoros**: 8 + 1

## Day 88: Mar 28, 2020

**TIL**: Learn how to create distribute package with wheel.
* Use tree command for view directory structure.
* Python have pypi for view package.
* Use pypa sample project to create setup file.
* Download only one setup file via github with 
```bash
curl -O https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py
```
* __python3 setup.py bdist_wheel__ for create distribute file.
* __pip3 install that_wheel_file__ will install package to site_package that sys.path will lookfor it when import package in python code.
* Can uninstall it with __pip3 uninstall that_wheel_file__.
* Package name that in setup file must be same name as package folder name.

**Thoughts**: Quite hot head when command don't work so I need to dig to root cause and spend more time debug it.

**Pomodoros**: 3


## Day 89: Mar 29, 2020

**TIL**: Learn docstring and doctest and shebang in python
* There is some usuful command I found.
* __pip3 uninstall -y helpers_pack__ -y is confirm for not type everytime.
* __pip3 install --editable .__ install local package with no need to install it again when code change.
* __``helpers_pack.__doc__``__ is view docstring.
* Docstring is string document sith """ DOC """ in header file can use in package or module or even fuction.
* __python3 -m doctest src/helpers_pack/helpers.py --verbose__ to run doc test in function. Like this

``"""
DOCUMENT HERE
``>>>`` function_in_module(name)
['a', 'b', 'c'] #Expect result function is this line it like assert.
"""``

**Thoughts**: I struck for create package in lab. So I use local instead but unfortually my glasses is broken so I need to stop it for today.

**Pomodoros**: 4


## Day 90: Mar 30, 2020

**TIL**: Complete yesterday lab on my local. I found mistake that I didn't write command __package_dir={'': 'src'}__ in setup file. So it cannot see my packages.
* Can use __pip3 install --user package_name__ to install when permission is proble.
* Learn tool and technique for เราไม่ทิ้งกัน infrastructure for handle 20m register from facebook live.

**Thoughts**: It awesome that see big success work in my country.

**Pomodoros**: 2

## Day 91: Mar 31, 2020

**TIL**: Learn life experience from my ancle on tomb sweeping day and learn a bit on object in python.
* Can use dir(object) to see all value and method.
* Everything in python is object.

**Thoughts**: That learn lesson today, it question me that who am I.

**Pomodoros**: 0.5

## Day 92: Apr 1, 2020

**TIL**: Basic Class in python.
* ``__init__`` for setup variable.
* @classmethod a methon that return class, it called decoration use for return class to be instance not methon alone and have access to other methon or variable useful when want to change some attribute in class. It live with in class.
* Can add attribute attach to instance or change current attribute on current instance. Attribut for me mean variable and function.
* self is keyword for reference attribute both variable or function.

**Thoughts**: Feeling confusing for myself. Not this python lesson but myself question.

**Pomodoros**: 2

## Day 93: Apr 2, 2020

**TIL**: Inheritance and multiple inheritance.
* self.__class__.__name__ for read class name.
* Use super for refer to parent class.

**Thoughts**: Not understand multiple inheritance and it method resolution order. I will try again tomorrow.

**Pomodoros**: 2


## Day 94: Apr 3, 2020

**TIL**: MRO methon resolution order in python.
* Just know that if send key value argument that didn't match key in parameter it will error.
* ``Classname.__mro__`` to see order of method when super() is referred.
* Use **kwargs to pass key word argument to other class useful when have multiple parameter in class.
* **kwargs is dictionary.
* Use self.method when don't want to redefind any method.
* Use super when name of parent class is same as child class.
* Use key value argument is effective than position argument when have multiple class.

**Thoughts**: Finally understand multiple class. But it feel not learn to much.

**Pomodoros**: 2

## Day 95: Apr 4, 2020

**TIL**: Mangling in python.
* Can use __function for private method.
* Mangling use for same name method in both parent and child. But child didn't have init and want to create instace with init and have to invoke parent function not child function,So to use local parent method (with same name as child) it must use mangle with __function_name.

**Thoughts**: I think it not useful at all LOL. I want to learn thing more practical than this. Maybe it downside of learn from class that prepare to certified.

**Pomodoros**: 1.5

## Day 96: Apr 5, 2020

**TIL**: Mostly is CI with cloud endpoint and incomplete python object lookup.
* Jenkinsfile have code that have it own clone branch to folder, not show in jk config.
* Can deploy develop directly not have to change any code to test deploy.
* Can use name for represent port not port digit directly in container port.
* Gcloud reserve external ip for service type LoadBalancer and when deploy again it not change.
* debug flag on helm will show all file template that deploy included all env.
* Divide task to small and cover all fundamental is the best way to adapter to complex ci.
* A bit on ``__bases__`` , ``__subclasses__`` for know who is parent and child.
* dir() have some attribute that not show such as ``__bases__``.

**Thoughts**: Cool part is when I can deploy it success I felt very good. Sometime I didn't remember what my goal for learn python is, LOL, I will go back to my track again.

**Pomodoros**: 4 + 0.5


## Day 97: Apr 6, 2020

**TIL**: Attribute in python class.
* If parameter that class not use it will not show in __dict__ even it have default value assigned
* If use cog.``__module__`` and it return ``__main__`` it mean it load from that module. Normally it return like module cat for example cat.``__module__`` will return cat.
* Instace of class has no attribute ``__bases__`` and ``__subclasses__`` only Class itself have.
* Use __str__ to customize print detail of instance for better debug purpose.

**Thoughts**: It almost done for class stuff. Useful thing for this time is custom method for debug.

**Pomodoros**: 2

## Day 98: Apr 7, 2020

**TIL**: Do class lab in python.
* Set is dict that have only value or key and it unorderd on indexed.
* Zip is combined of one or more list and return tuple with each element. If one list it will be ``{(2,), (3,), (1,)}``
* If declare vaiable in class it will share it with other instance. But if declare in ``__init__`` it will use only in that instance not shared.

**Thoughts**: I forgot how to use sort so I need to open w3 for document. Also forgot how to convert tuple to dict LOL.

**Pomodoros**: 2

## Day 99: Apr 8, 2020

**TIL**: Do a work and fix bug and little python file with mode r, w, r+, w+, x, a.

**Thoughts**: Spend time to work exceed my limit and I found if I learn too much like this it feel very intense but it increase my capacity I decide to not learn much because I won't remember anything so sleep is better idea. Tomorrow I will try to learn at lease 4 pomodoro.

**Pomodoros**: 20 + 0.3

## Day 100: Apr 9, 2020

**TIL**: Learn how to redirect via nginx.
* Just known that cannot redirect with CNAME in dns it use for record purpose.
* Can redirect by use nginx.ingress.kubernetes.io/temporal-redirect: https://example.com via annotation in ingress.
* Ingress resource is useful when it have ingress controller install first.
* It can install with __helm install my-nginx stable/nginx-ingress__

**Thoughts**: Not learn python today and feel lazy don't know why. Still can't do what I expected.

**Pomodoros**: 2

## Day 101: Apr 10, 2020

**TIL**: File in python.
* r+ + mean opposite of read is write so this mode is have both read and write.
* r+t t mean return text.
* r+b b mean return in byte.
* If open file it must close to good pratice.
* Lazy to close file everytime can use with syntax, it will close file automatic no need to write code manually.
* Core concept for file manipulate is cursor it have cursor and move forward when write. So when want to read, it will read from current cursor position.
* If want to read all file when not already close, need to use my_file.seek(0) to move cursor position to start of file and read it untill end of file.
* my_file.readlines() will return list of txt seperate with \n.

**Thoughts**: Try not to learn today but after wash my face it feel want to complete, I'm not the same person who always procastinate.

**Pomodoros**: 1

## Day 102: Apr 11, 2020

**TIL**: Review file in python.
* Need to move seek to 0 when want to use read or readlines everytime.
* If not use close properly some change to file may not effect.
* with statement will release resource properly, I mean auto close file, it will make code no bug.

**Thoughts**: Very lazy for today but still need to learn.

**Pomodoros**: 1

## Day 103: Apr 12, 2020

**TIL**: Do file lab, it combine of classmethod and for sure I forget it. Still not finish yet I will complete it tomorrow.
* byte in python and it immutable like string.
* But bytearray is mutable it can change with slice or use position, if use position it need to be hex type for example 0x11.
* my_file.readinto(bytearray(10)) can read file and store to bytearray.
* my_file.read(10) it read from current seek position to 10.
* bytearray(my_file.read(10)) it store byte data from read to bytearray it equal to my_file.readinto(bytearray(10)).

**Thoughts**: I think it not practical much I need more lesson that very practical than this. It make me not fun and learn like when I'm at school. I know because this course design for certificate.

**Pomodoros**: 4

## Day 104: Apr 13, 2020

**TIL**: Finish yesterday lab and use other function that I learned.
* enumerate can return with index. Ex: for index, line in enumerate(f.readlines()).
* str.strip(), str.lstrip(), str.rstrip() it like trim() in JS but can select with side to trim.
* Can set default value from unpack, use with *varible. It combine with condition expression. 
Ex:
```
a, b, *c = [1, 2, 3]
c = c[0] if c else None
assert c == 3

a, b, *c = [1, 2]
c = c[0] if c else None
assert c == None
```

**Thoughts**: This is second time that I stuck and I go search on google how to use index and strip in python. It good sign.

**Pomodoros**: 1.5

## Day 105: Apr 14, 2020

**TIL**: Try to use SSL with cloud endpoint.
* Most part for this is bug from end of line error. It from -----END CERTIFICATE----- error that not in correct structure.
* It must be our.crt intermediate.crt root.crt for concat to cert.crt for use.
* esp will cacahe mount volume for a while so when change nginx.crt it take sometime to take effect.
* nginx in esp default certificate file named is nginx.crt and nginx.key so need to make sure file is named correctly.
* It can't use secret object in k8s with tls type it only use opaque that is default type.

**Thoughts**: Feel excite when read story of great thai people that will be researcher. And this bug make me frustrated for a while because I think I can do it at first try.

**Pomodoros**: 4

## Day 106: Apr 15, 2020

**TIL**: Most time is spend with work on deploy gw with project.
* Learn how to write helm with variable.
* Use template in openapi when path is variable. It need to config and require more parameter than usally such as parameter: require, type.
* Endpoint is work only jwt and apikey that is google api key it will validate but other custom api key is not process by endpoints, security definition must specific with type ApiKey and name is 'key' in query.
* Apikey can restrict to api and endpoint name is one of api service, so can restrict with name of endpoint that I deploy.
* Apikey is for identify suitable for project such as web or service not for user. User must use token that from authenticate and authorize.
* It can also call endpoint in ClusterIp for internal backend.
* When need new sub domain, domain verify need mail that verifid domain for deploy openapi config for first time then can use service account for deploy later.

**Thoughts**: Spend more time to learn and do it in real situation but also want to learn python next time will balance time better.

**Pomodoros**: 8

## Day 107: Apr 16, 2020

**TIL**: Learn how to use *(asterisk) syntax in python.
* [1] + [1] = [1,1]
* [0] * 3 = [0, 0, 0] or (0,) * 3 = (0,0,0)
* *args or **kwargs called for packing or variadic argument. For accept arbitary parameter.
* *args use for positional argument and packing to tuple.
* **kwargs use for key word argument and pakcing to dict.
* def(**kwargs, *args): will raise Error because position not follow keyword argument.
* func(*numbers) use for unpack list to argument for call function.
* a, b*, c = [1,2,3,4,5] a = 1, b = [2,3,4], c = 5

**Thoughts**: It very fun that asterisk can use in multiple way in python here I learn form this [link](https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558)

**Pomodoros**: 2

## Day 108: Apr 17, 2020

**TIL**: Learn how to use exception in python.
* except: (IndexError, KeyError) can be multiple exception in tuple.
* If class (sub-class) that inherit from that exception class (parent-class) still can go to that exception even not write it down explicit.
* else is happy path when exception not raise.
* finally still call even have exception.
* sys.argv is list of all argument when run python script.

**Thoughts**: A little progress. I plan to use all my python knowledge to create cli with my work project, for now in research stage.

**Pomodoros**: 1

## Day 109: Apr 18, 2020

**TIL**: Try to figure it out why IP not show in log of cloud endpoint.
* Remove service object that have external ip will release ephemeral ip.
* Try use x-forward-for but it didn't work.
* Can use gcloud endpoints service list and gcloud endpoints services delete NAME.
* I found this to solve the issue that is add this to service externalTrafficPolicy: Local.
* It will not cause to second hop for loadbalance service type and keep client ip but will have issue about traffic spread. This [ref](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip)
* My intuition from this is sidecar pattern compare to old one with have one container in pod.

**Thoughts**: First I want to learn python again but this issue struck in my mind and make me to overcome this. This time I will know ip that try to bruteforce my endpoint.

**Pomodoros**: 4

## Day 110: Apr 19, 2020

**TIL**: A bit on Exception.
* Relearn about Class.``__bases__`` and Class.``__subclasses__()``
* Use raise keyword for throw error.

**Thoughts**: Not much for today. I sleep very late and not much on learning, feel bad :(

**Pomodoros**: 1

## Day 111: Apr 20, 2020

**TIL**: Still on raise keyword try to use it with try except keyword.
* Exception class is kind of parent of all error class.
* raise keyword with error class will show Traceback error detail.
* It have a lot of error class to specific and deal with it can see via Exception.``__subclasses__``() and also have child under that child class.
* Update sql with created_at is '0000-00-00 00:00:00' is solved by CAST function.
```sql
UPDATE `code` SET created_at = updated_at where CAST(created_at AS CHAR(20)) = '0000-00-00 00:00:00'
```

**Thoughts**: Still lazy but this phase pop in my head if I don't walk, just crawl.

**Pomodoros**: 1


## Day 112: Apr 21, 2020

**TIL**: Python Error and relearn doctest and shebang.
* Use custom error that class inherite from Exception.
* Use assertion when want to debug and raise error and see how my code react.
* -O flag is use for optimize in production that will remove assert in my code, so it will skip assert part and make weired logic to our program.
* -OO is do what -O does plus remove docstring.

**Thoughts**: Try back to learn early and it work well.

**Pomodoros**: 2

## Day 113: Apr 22, 2020

**TIL**: Do exception lab.
* Just know varible in try except is not have local scope it global scope
```python
try:
    f = open("root_files/name_repeated.txt", "w")
except (OSError, IOError) as err:
    print(f'File error is {err}')
else:
    names = [name + "\n" for i in range(1, repeat_count + 1)]
    f.writelines(names)
    f.close()
```
see f variable can be reference in both try and else, not like js that is local scope.
* sys.exit(1) is exit code not do the rest. 1 not 0 mean exit with an error.
* Learn kaggle progess. Just know it have free GPU to train.

**Thoughts**: Love kaggle very much I will pratice myself in here. I dream to be grandmaster LOL.

**Pomodoros**: 2

## Day 114: Apr 23, 2020

**TIL**: Try assessment python on pluralsight got 208 but found a lot that I didn't know.
* ``__iter__`` and ``__next__`` is make class iterable.
* debug module in python.
* wite statement use with other thing than open file.
* Just know that can use '''string name''' triple single quote with string.
* Python package no need to use ``__init__`` to import package.
* Use multiple if in list comprehensive that if is nested if. Example
```python
[i for i in range(100) if i > 10 if i < 20]

or

[i for i in range(100) if 10 < i < 20]

is equal to

arr = []
for i in range(100):
  if i > 10:
    if i < 20:
      arr.append(i)

```
* In sequelize learn how to use reload, increment and save.
* txn.reload() is select command again from database.
* instance.save() is not effect if other is in tranasction.
* Learn more about kaggle and found that china and russia also have competetive like kaggle.

**Thoughts**: First try feel bad that have lower score but after change my attitude, I feel good that I can learn a lot from my mistake and know better. I have set and with statement to findout more.

**Pomodoros**: 4


## Day 115: Apr 24, 2020

**TIL**: Try last python lab and review scope lesson in python.
* It have error FileNotFoundError and PermissionError.
* remove(file) can remove file import via os.
* Class in file can reference regradless put in head or bottom of file.
* Python doesn't have variable declarations, so it has to figure out the scope of variables itself. It does so by a simple rule: If there is an assignment to a variable inside a function, that variable is considered local.
* Condition and loop do not defind their own scope.
* Parameter always win global.
* Sum-up scope can reference in function, new assign is new variable called shadowing, 
use outter variable in local scope via global, also can reference variable in local to outter via global variable that assign inside local function scope.

**Thoughts**: It feel good that review scope lesson again because at first I confused some concept but now is cleary.

**Pomodoros**: 2

## Day 116: Apr 25, 2020

**TIL**: Learn how to use with statement.
* It use for acquire and release resource.
* Must have 2 function ``__enter__`` for acquire and ``__exit__`` for release.
* If use this class with with statement, after create class it will call ``__enter__``
and execute code after excecute complete it call ``__exit__`` for release resource.
* ``__enter__`` and ``__exit__`` are called context manager.
* In ``__enter__`` must return resource descriptor such as file from open function.
* ref [1](https://www.geeksforgeeks.org/with-statement-in-python/),[2](https://docs.python.org/2.5/whatsnew/pep-343.html)

**Thoughts**: This time I learn with out any course instruction, feel very fun when want to know something and no need to wait teacher to taught.

**Pomodoros**: 2

## Day 117: Apr 26, 2020

**TIL**: Learn one of common mistake in python. ref [link](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)
* except Exception as e: will transform to
```python
try:
  connentDb()
except DbError as e:
  print(f'Error {e}')

  will translated to 

try:
  connentDb()
except DbError as e:
  try:
    print(f'Error {e}')
  finally:
    del e
```
So this will raise issue if you use e as vairable in that function
```python
def bad():    
    e = None
    try:        
        bar(int(sys.argv[1]))
    except KeyError as e:        
        print('key error')
    except ValueError as e:
        print('value error')
    print(e)
```
So print(e) will error like UnboundLocalError: local variable 'e' referenced before assignment because when except statement is translated it will delete e, so print(e) will raise error because e is deleted.

Solution for this is use another variable for reference that e in except scope.
For example.

```python
def good():    
    exception = None
    try:        
        bar(int(sys.argv[1]))
    except KeyError as e:        
        print('key error')
        exception = e
    except ValueError as e:
        print('value error')
        exception = e
    print(exception)
```

* Just hear word like reference cycle and stack frame. Just know about reference cycle.
It is object that refer to itself. [ref](https://stackoverflow.com/questions/9910774/what-is-a-reference-cycle-in-python)
```python
l = []
l.append(l)
```
**Thoughts**: I didn't do final test yet and will try tomorrow. I didn't read whole pitfall topic but will learn it by pick one topic per day LOL.

**Pomodoros**: 2

## Day 118: Apr 27, 2020

**TIL**: Jump myself to data scientist world on data camp. Learn how to use pandas.
* Just know that table data in pandas is called DataFrame that I known before but already forget.
* Use dict to create data frame.
* Import from csv file to create data frame.
* Use index_col for index row.

**Thoughts**: I will create plan for this learning and need to mix with dl course and fast.ai course.

**Pomodoros**: 1

## Day 119: Apr 28, 2020

**TIL**: A bit on loc and iloc will try practice tmr.
* If use double square bracket, array_df[[]] will return dataframe object.
* If use single square bracket, array_df[] will return series object.
* loc use for row label.
* iloc use for index.
* dataframe can select column by array_df[['column_name']] and row with array_df[1:4].
* but with loc and iloc can use to select column, row or both with one function.
* array_df.loc[['row1_label', 'row2_label'], ['column_name1', 'column_name2']]

**Thoughts**: I forget numpy array will learn it first and continue on dataframe.

**Pomodoros**: 1

## Day 120: Apr 29, 2020

**TIL**: Learn 1D numpy array.
* It can operate in an array like np.array([1,2,3]) * 2 = np.array([2,4,6])
* It can filter with condition expression like 
np.array([1,2,3]) > 3 = np.array([False,False,True])
* Can apply filter for get result.
* Have type coercion.


**Thoughts**: Tomorrow will learn 2D numpy array. This lib is amazing.

**Pomodoros**: 1.5

## Day 121: Apr 30, 2020

**TIL**: A liitle on 2D numpy array and how to access it.

**Thoughts**: I have some home problem to solve that make me sick and effect my learn.

**Pomodoros**: 0.5

## Day 122: May 1, 2020

**TIL**: Hand on numpy 2D array.
* Mostly like 1D array but have slice and sugar syntax with np_array[row, column]
and can use with slice ex. np_array[2:6, 3]
* very like
```python
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

np_mat + np.array([10, 10])

equal to.

array([[11, 12],
       [13, 14],
       [15, 16]])
```

**Thoughts**: Numpy it very easy to use and very intuitive.

**Pomodoros**: 1

## Day 123: May 2, 2020

**TIL**: Basic stat with numpy.
* std, mean, median, corrcoef(column_list_1, column_list_2)

**Thoughts**: Very useful when want to describe data.

**Pomodoros**: 1

## Day 124: May 3, 2020

**TIL**: Use loc and iloc in dataframe and series.
* It like 2D numpy array except it need .loc or .iloc not use directly.
* Can use slice with df.loc[:, ['column1']].
* Row index can be string if it use row only but not when combine it with column index ex.
```python
df.iloc[[1, '2']] is fine

df.iloc[[1, 2], [1, '2']] is error
```

**Thoughts**: Continue to learn after complete numpy for better understand.

**Pomodoros**: 2

## Day 125: May 4, 2020

**TIL**: Learn how to use df to filter data and use and, or in numpy and df.
* Dataframe build on top of Numpy.
* filter data step
  1. Get column to series.
  2. Do a condition expresstion like >, <, logical_and, logical_or.
  3. Subset df, apply that expresstion to dataframe to get only data that meet condition.
```python
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
# or use between = cpc >= 10
cars_medium = cars[between]
# sometime prefer on line like this
cars_medium = cars[np.logical_and(cpc > 10, cpc < 80)]
```

**Thoughts**: It very easy to use.

**Pomodoros**: 1


## Day 126: May 5, 2020

**TIL**: Review how to loop such while, for, for with dictionary and loop through numpy array.
* Dictionary are unorderd.
```python
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print("the capital of "+k+" is "+v)

    # it will print, see it unorder
    # the capital of austria is vienna
    # the capital of poland is warsaw
    # the capital of norway is oslo
    # the capital of france is paris
    # the capital of spain is madrid
    # the capital of italy is rome
    # the capital of germany is berlin  
```
* Use np.nditer(np_array) to look at element in n dimension array. It will print first column untill finish then print second column.
```python
for x in np.nditer(np_baseball):
    print(x)
```

**Thoughts**: I learn at night almost week and half make me feel sick and my memory are inefficiency.

**Pomodoros**: 1


## Day 127: May 6, 2020

**TIL**: Learn how to loop through dataframe and add column.
* Loop using df.iterrows() will return label and row, that row is series.
* Can use apply(function) for better performance (not use loop).
* Can loop through series directly it look like array list.
**Thoughts**: I found myself very curious about that syntax and datatype that return from syntax both numpy, series, dataframe, loc, iloc.

**Pomodoros**: 2

## Day 128: May 7, 2020

**TIL**: Learn how to use random in numpy.
* np.random.seed() can set or not set seed, If set it will random same number every call, it mean can reproduce. Ex np.random.seed(123).
* np.random.randint(1, 7) random int number from 1 - 6 not include 7.
* np.random.rand() just random decimal number.

**Thoughts**: Not much for today feeling lost my opportunity.

**Pomodoros**: 1


## Day 129: May 8, 2020

**TIL**: Implement that randoms walk and create graph with mathplot lib.
* plt.plot(x, y) if add argument only x like plt.plot(list) it will use index of list as x axis and value as y axis.

**Thoughts**: A little progress and still learn very late it feel like I pay my debt with lowest possible.

**Pomodoros**: 1

## Day 130: May 9, 2020

**TIL**: Do lab till finish and learn how to use histrogram and bin and np.transpose.
* plt.hist(data, bins=5) bins is split data into bins chunk number.
* hist is use for see distribution of your data how it look like.
* np.transpose to swap row to column and column to row.

**Thoughts**: It make sense for this lab for play and use all I learn to figure it out.

**Pomodoros**: 2

## Day 131: May 10, 2020

**TIL**: Do a project TV, Halftime Shows, and the Big Game in datacamp with use of all intermediate course and a bit data manipulate.
* Maybe data thing is from curiosity that what you need to know.
* Can select column from dot or key Ex. no_bands.num_songs == no_bands['num_songs']
* Know how to filter out NaN wit dropna() Ex. no_bands['num_songs'].dropna()
* Filter text by using str.contains Ex. halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
* Know how to sort with sort_values('column', ascending=False) Ex. no_bands.sort_values('num_songs', ascending=False)
* Sub plot graph with plt.subplot(Number_graph, 1, index) Ex. plt.subplot(3, 1, 1)

**Thoughts**: Project base is make my intuition very sharp. It connect dot of knowledge together and make it useful.

**Pomodoros**: 4

## Day 132: May 11, 2020

**TIL**: Learn about basic dataframe again with expand.
* It consist of 3 component values is data values, index row is row index and row label, column is index of columns that is column name Ex df.values, df.index, df.columns.
* df.describe() is very useful for show basic stat of this df data.
* df.sort_values(['columns1', 'columns2'], ascending=[True, False]) it sort with chunk of data not all data.
* Filter with expression and is & or is | it can't use "and", "or" literally.
* If filter multiple variable on one column use df[df['column'].isin(['value1', 'value2'])] for short hand, full is 
df[(df['column'] == 'value1') | (df['column'] == 'value2')] don't forget parenthesis () is very important.

**Thoughts**: Step up a littile knowledge.

**Pomodoros**: 2

## Day 133: May 12, 2020

**TIL**: Learn about add new column and learn how to use python in automate way.
* homelessness.sort_values(['total', 'p_individuals'], ascending=[False, False]) same value type in this is float it will priority first array (index 0) to make it happen to true condition for example this will sort descending total column and doesn't care about p_individuals, and vice versa.
* Most common types of data manipulation: sorting rows, subsetting columns (column select), subsetting rows (row select by condition expresstion), and adding new columns. In a real-life data analysis, you can mix and match these four manipulations to answer a multitude of questions.
* Just know way to calculte this question Number of homeless individuals per 10,000 people in the state or when you face 10000 people, How many homeless you will see? It easy just use homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']
* Know about send email with python to do an automate task and it can calculate more than excel and graph boke is better than mathplot. [This is link that I learn](https://youtu.be/vmUgaNaJfIs).

**Thoughts**: Do a lot of work today and feel like robot haha I need more automate skill.

**Pomodoros**: 2

## Day 134: May 13, 2020

**TIL**: Learn about JWE, JWS that is part of JWT this [link](https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3).
* Just know about JWE it like encrypt token and send it with key.
* Contain 5 part 
  1. JOSE is header part.
  2. Key that encrypted use for encrypt JSON context and it encrypted by RSA algorithm for send key.
  3. Initial vector it like nounce for encrypt same context but result will not same.
  4. Encrypted context this encrypted by key in 2.
  5. Signature that come form encrypt process of 4.
* I think it can't use with clound endpoint.
* JWS is simple just signature and payload like JWT that I known.
* Compact serialization is dot separate of JWE and JWS.
* Do SQL assessment and got 110 from 300 feel WTF haha. Fortunately it doesn't show correct answer for improvement.

**Thoughts**: This SQL assessment make me feel I don't really know to write SQL at all, nevermind I will try to be better.

**Pomodoros**: 2

## Day 135: May 14, 2020

**TIL**: Learn how to use basic stat in df and use cummulative of it and df[['cl1', 'cl2']].agg(custom_fuction) is like apply function but it dynamic can use with custom function.

**Thoughts**: I feel lack of statistic knowledge that I cannot look data and see their meaning. And df.describe() is very useful to see all basic stat at once.

**Pomodoros**: 1

## Day 136: May 15, 2020

**TIL**: Count values per column and drop duplicate values.
* sales.drop_duplicates(subset=['store', 'department']) can drop single or multiple column.
* departments['department_num'].value_counts(sort=True, normalize=True) normalize is very useful to see percentage of each values.

**Thoughts**: I cannot remember command in video in first time and need to switch back to see and then go to type again.

**Pomodoros**: 1


## Day 137: May 16, 2020

**TIL**: Lern how to use groupby and pivot table.
* pivot is just another way to do groupby, it can see all data at once and can deal with NaN data.
* pivot default is mean().
* df.pivot_table(values='weekly_sales', index='type', column='department', aggfunc=[np.mean, np.median], fill_value=0, margins=True) index is group by column, column is another groupby, agg function is like agg in groupby it can add function to it like np.median and margins is sum of all row and column and see it at once.
* Group by is like in sql way can use with multiple function.
* sales.groupby(['type', 'is_holiday'])[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])
* for access multiple groupby is allg.iloc[1,0] and label is allg.loc[('A', True), ('unemployment', 'amin')] use tuple as key for access.

**Thoughts**: It make more fun when just think beyond scopre and try to figure it out.

**Pomodoros**: 3


## Day 138: May 17, 2020

**TIL**: Change column to index and make access index with loc easier then use isin function.
* Easier like 
```python
# have index for make code clean
dogs[dogs['name'].isin(['Bella', 'Stella'])]
to 
dogs.set_index('name') # change column name to index
dogs.loc[['Bella', 'Stella']]
```
* df.set_index('cl1') to change cl1 to index.
* df.reset_index() discard index, change index back to column.
* df.reset_index(drop=True) will delete column that used to be index.
* Multi level index is make index more than one column df.set_index(['cl1', 'cl2']) can access with tuple df.loc[[('cl1', 'cl2')]]
* sort_index is like sort_values except it use for index and key is level not values like 
df.sort_index(level=['cl1', 'cl2'], ascending=[True, False])
* It good to know index but it break the "tidy data" principle that data have it own column but index isn't have their own column.
* If make all column as index and drop all of it, it will remain just array of row number like this [0, 1, 2, 3, 4, 5, 6, 7, 8]

**Thoughts**: I need to find some project to do that can recall my learning and make it strong memory.

**Pomodoros**: 2

## Day 139: May 18, 2020

**TIL**: Learn how to slice again but this time is very useful when use with date.
* _Note that because the date isn't set as an index, a condition that contains only a year, such as df['date'] == '2009', will check if the date is equal to the first day of the first month of the year (e.g. 2009-01-01), rather than checking whether the date occurs within the given year. Sum up (df['date'] == '2009') == (df['date'] == '2009-01-01')
* You can only slice an index if the index is sorted.
* The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd.

**Thoughts**: Use with date is very useful.

**Pomodoros**: 2

## Day 140: May 19, 2020

**TIL**: Learn how to slice pivot table it like in dataframe.
* A pivot table is just a DataFrame with sorted indexes, pivot are automatic sort so can use loc without sort first.
* Can also subset date with column not just index.
* axis in mean of pivot is like which index or column you want to compute, if axis='columns' it will colapse all into index vice versa. Ex. temp_by_country_city_vs_year.mean(axis='columns')
* dataframe["column"].dt.month will select only month from column data, dataframe["column"].dt.year will select only year from column data. This useful when you want to use with date column Ex. temperatures['year'] = temperatures['date'].dt.year add new column only year from date column.

**Thoughts**: Not much for today have a lot of work to do.

**Pomodoros**: 1

## Day 141: May 20, 2020

**TIL**: Learn how to visualize with mathplotlib and use plot function.
* Scatter plots are ideal for visualizing relationships between numerical variables.
* df.plot(x='cl1', y='cl2', kind='scatter', rot=45) can plot line and scatter, rot is x axis label to rotate how much degree.
* alpha near 0 in histogram mean more tranparent and near 1 is opaque. df['cl1'].hist(alpha=0.5, bins=20)

**Thoughts**: I didn't know how to read data from graph much.

**Pomodoros**: 1


## Day 142: May 21, 2020

**TIL**: Learn how to handle missing value with basic
* df.dropna(subset=['cl1', 'cl2']) and df.fillna(value)
* df.isna().any() will show each column whether it have NaN or not, show as boolean.
* df.isna().sum() will show each column with sum of NaN.
* avocados_complete.isna().sum() can plot grapht like this avocados_complete.isna().sum().plot(kind='bar')

**Thoughts**: It kind of slow progess but review old knowledge and that plot will make more clear about NaN in your data.

**Pomodoros**: 2

## Day 143: May 22, 2020

**TIL**: Learn how to create manual dataframe and read and write csv.
* Can use list of dictionaries or dictionary of lists to create df object by use pd.DataFrame(list_of_dict)
* Can read csv by use pd.read_csv('filename.csv')
* Can write csv by use df.to_csv('filename_to_save.csv')

**Thoughts**: Dictionary of list is intuitive for tabular data than list of dict.

**Pomodoros**: 1


## Day 144: May 23, 2020

**TIL**: Do project that user seaborn and plotly, personally plotly is way better and more interactive.
* A good practice is to always use the info() to see type that not suitable such "price" but type is object, this should convert to correct type such float.
* len(apps['App'].unique()) use for count total value of column.
* Change data type that not suitable and remove non useful character like $ , + in value is very useful.
* astype() method is used to cast a pandas object to a specified dtype
```python
# List of characters to remove
chars_to_remove = [',', '$', '+']
# List of column names to clean that column is object that not suitable it must be float.
cols_to_clean = ['Installs', 'Price']
# Loop for each column
for col in cols_to_clean:
    # Replace each character with an empty string
    for char in chars_to_remove: # astype() method is used to cast a pandas object to a specified dtype
        apps[col] = apps[col].astype(str).str.replace(char, '')
    # Convert col to numeric
    apps[col] = pd.to_numeric(apps[col]) 
```
* Filter rows where both Rating and Size values are not null 
```python
apps[(~apps['Rating'].isnull()) & (~apps['Size'].isnull())] 
```
use ~ combine with isnull() for select only not null value.
* Can use filter after groupby for select groupby size more that x number.
Note not select or calculate any column after groupby.
```py
apps_with_size_and_rating_present.groupby('Category').filter(lambda x: len(x) >= 250).reset_index()
```
* Sum ups.
  * Check data type that correct or not.
  * Remove null or unwant character.
  * Make assumption from data.
  * Select data for make graph mostly is data for x and y axis.
  * Plot graph and read result.

**Thoughts**: I see a lot of technique that beyond from learning lesson that very useful for tackle real world data.

**Pomodoros**: 4


## Day 145: May 24, 2020

**TIL**: Learn how to load muliple csv file with list comprehensive and reindex it like join when use other index as our index.
* Comprehensive like
```py
dataframes2 = [pd.read_csv(file) for file in filenames]
print(dataframes2[0].head())
```
* medals = gold.copy() for copy df object.
* Can replace df with new column Ex. medals.columns = ['NOC', 'Country', 'Gold']
this change from Index(['NOC', 'Country', 'Total'], dtype='object') to Index(['NOC', 'Country', 'Gold'], dtype='object')
* Use index_col to specific column to be index when read csv Ex. `pd.read_csv('monthly_max_temp.csv', index_col='Month')`
* df.reindex(index_list) will return only index list with current df value, not have value will result to NaN but still have that index.
* df.ffill() stand for forward fill, will replace NaN with value before it that not NaN and replace till see next not NaN value.

**Thoughts**: It like basic join when use other index as our index in reindex() and how to load list is very useful.

**Pomodoros**: 1.5


## Day 146: May 25, 2020

**TIL**: Learn how to do + - * / (arithmetic) to broadcast in df with function
* Remember, ordinary arithmetic operators (like +, -, *, and /) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.
* It very trick for change via str function and can use all str function can do.
`temps_c.columns = temps_c.columns.str.replace('F', 'C')`
* Need parse_dates=True when use with data index.
`pd.read_csv('GDP.csv', index_col='DATE', parse_dates=True)`
* Resample is just like groupby with select date time, mostly use when key is datetime.
'A' is anually, can be 3D mean select every 3 day of data from date. it combine with stat function like mean. 
[Ref](https://www.w3resource.com/pandas/series/series-resample.php)
.last() mean select last observation, can combo with time like df.last('3D') selct only last 3 calendar day from data.
`yearly = post2008.resample('A').last()`
* It better than * (multiply) only because it more control with axis to calculate, normally it should same column for * to work, Can do with only series but can't with df.
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

**Ref**:
  * [Code](python/df_arithmetic.py)
  * Slide [MERGING DATAFRAMES WITH PANDAS - Arithmetic](python/slide/datacamp/merging_df_with_pandas.pdf)

**Thoughts**: It very useful when date is index. And [w3pandas](https://www.w3resource.com/pandas/index.php) is awesome it have visual and code example.

**Pomodoros**: 2


## Day 147: May 26, 2020

**TIL**: Learn about concat and append in both Datafram and Series
* concat is more useful than append because it can control axis to compute. Ex.
```python
# 1 mean columns or horizontal
# 0 mean rows or vertical (default)
weather = pd.concat(weather_list, axis=1)
```
* append reset index use df1.append(df2).reset_index(drop=True) or df1.append(df2, ignore_index=True)
* concat reset index use pd.concat([df1, df2], ignore_index=True)
* Can iloc with date like this `quarter1.loc['jan 27, 2015':'feb 2, 2015']`
* `medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=['Country', 'goal'])`
  * names use for change column name, this time is from ['Country', 'Total'] to ['Country', 'goal']
  * header make that row as header but I didn't know this benefit

**Ref**: 
  * [Code](python/df_concat_append.py)

**Thoughts**: I didn't watch video because it stuck, and try to read from doc and do an exercise.

**Pomodoros**: 2


## Day 148: May 27, 2020

**TIL**: Learn how to slice with inner level index only.
* `medals_sorted.loc[pd.IndexSlice[:, 'United Kingdom'], :]` for slice by specific inner index can use in both axis index row and index columns.
* `pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])` key for apply outter level index in that df. axis use for concat on verticle or horizontal.
* `month_data.groupby('Company').sum()` it group on that key and make every columns that is number calculate on that stat function like sum, mean.
**Ref**: 
  * [Code](python/df_concat_append.py)

**Thoughts**: I try to put keys on 2 layer it success but can't slice with pd.IndexSlice properly.

**Pomodoros**: 2


## Day 149: May 28, 2020

**TIL**: df.concat([df1, df2], join='inner') join type inner and outer, default is outer.
* inner is like intersect in set, intersect between index can be row or column depend on axis If axis = 0 verticle it will see columns index but axis=1 horizontal it will index by row index.
* outer is like union in set.
* pct_change and resample if want to compare it value it must corresponding. Ex.
```py
china = china.resample('A').last().pct_change(10).dropna()
# it calculate percentage with offset 10 for each value
# to show in resample with 10 anual (decate) that corresponding.
print(china.resample('10A').last())
```
**Ref**: 
  * [Code](python/df_concat_append.py)

**Thoughts**: It very important to process data and show that relate each other.

**Pomodoros**: 1

## Day 150: May 29, 2020

**TIL**: Use df.merge it like join with columns name but mostly it don't have index row, it use default row number.
* df.merge use columns name that same name for join and will find intersect value.
* I think different than df.concat is df.merge don't have row index but df.concat have row index.
* Merge it look for columns index only and default is inner join but keyword use "how" Ex.`df.merge(df1, df2, how='outer')`.
* Use left_on and right_on when df don't have same columns name. Ex.
```py
pd.merge(revenue, managers, left_on='city', right_on='branch')
# Can be multiple columns
pd.merge(revenue, managers, left_on=['city', 'change'], right_on=['branch', 'state'])
```
* `revenue = revenue.drop(columns='state')` Use df.drop(column='cl1') for drop column, argument can be vary.
* Can merge on multiple column Ex. `pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])`

**Ref**: 
  * [Code](python/df_merge.py)

**Thoughts**: Sometime I feel lazy for do sum-up here. After this change 1 pomodoro to 51 min.

**Pomodoros**: 1

## Day 151: May 30, 2020

**TIL**: Learn join but do lab only merge LOL.
* ffill if start is null later is still null it not help when timeseries statr with null
* df1.join(df2) will join on row index so it should have index row like concat.
* pd.merge_ordered(df1, df2) default join is outer different from pd.merge(df1, df2) that default is inner.
* pd.merge_ordered(df1, df2) is sorted like lexicography, it mean sort like litteral dictionary (it real dictionary book).
* left_on and right_on can be list. Ex. `pd.merge(sales, managers, left_on=['city', 'state'], right_on=['branch', 'state'], how='left')`
* how in merge is left, right, inner, outer default is inner.
* resample can specific column by using "on" Ex.`merged.resample('A', on='Date')[['mpg', 'Price']].mean()`
* df1.join(df2) both must have row index.

**Ref**: 
  * [Code](python/df_merge.py)

**Thoughts**: I think I need to direct learn to fast.ai. My learning still very late. And df1.join(df2) is kind of not useful if you can do with merge.

**Pomodoros**: 1

## Day 152: Jun 2, 2020

**TIL**: Learn frontend basic with html and element in it.
* Contain of DOCTYPE html for tell browser that use html5.
  * html
  * head contain information such title and css style.
  * body contain thing that want to show.
* br tag stand for break.
* alt in img tag for alternative text when image cannot display. `<img src="notfound.jpeg" alt="This will show.">`
* target _blank in a tag for open new tab `<a href="https://chomchob.com" target="_blank">Go to chomchob with new tab</a><br>`
* a tag can be internal file or external link. `<a href="logo.jpg" target="_blank">Access to internal file.</a>`
**Ref**: 
  * [Code](frontend/project/clone-blog-post/index.html)
  * [People face Generator](https://randomuser.me/)
  * [Mockup Text Generator](https://www.blindtextgenerator.com/lorem-ipsum)

**Thoughts**: I think I need to learn frontend for paid my debt first before follow my passion and it very hurt that I can't do what I want because I have no money to much. This time for learn is DDD Debt Driven Developmemt.

**Pomodoros**: 1


## Day 153: Jun 4, 2020

**TIL**: Just know about RGB color and attribute in it.
* RGB = #RRGGBB max is ff(255) min 0, Ex. Red is #ff0000, Green = #00ff00, Blue = #0000ff. mix it is yellow = red + green = #ffff00
* if all value are the same Ex. #555555 just use #555.
* color can have opacity like  rgba(38, 46, 135, 0.92);
* Use class for specific element can be multiple, use id for one element. But good practice is always use class not use id because we don't know future yet.
* Use # for selector id and . for selector class.
* Block element such h1 it have their own line break (<br>) and full width.
* inline element such strong, a tag don't have line break (<br>).
* box-sizing: border-box; for use width and height to apply to border not content.
* Learn abit about typescript.

**Thoughts**: Just know abit about css and typescript.

**Pomodoros**: 2

## Day 154: Jun 5, 2020

**TIL**: Learn about config of typescript and use eslint and nodemon.
* Use tsc --watch for auto complie from ts to js.
* Combo with nodemon will easy to develop with no overhead.
* TS have source map for return error on ts file not just js.

**Thoughts**: This typescript will improve my software skill a lot and it very fun to learn new thing.

**Pomodoros**: 0.7

## Day 155: Jun 29, 2020

**TIL**: Learn about basic typescript to discreminated union type.

**Thoughts**: Long time didn't learn it make me feel lack something very important and back to use life as earlier that not productive.

**Pomodoros**: 2

## Day 156: Jun 30, 2020

**TIL**: Jest and basic test and concept of TDD.

**Thoughts**: I didn't write test for longtime. But still think it very useful tool for do a software.

**Pomodoros**: 2

## Day 157: Jul 1, 2020

**TIL**: Lecture of testable architechture that goal is reliable small component glue together to whole system.

**Thoughts**: I didn't realize how defenition of testable architecture is, and how to design good system. This ep is clarify me a lot.

**Pomodoros**: 1.5

## Day 158: Jul 5, 2020

**TIL**: Watch how to do api with test and understand what clear line defind is.
And make some hand dirty after watch whole video but still not finish lab yet because some code that break. And learn how to use supertest.

**Thoughts**: It very flow process that watch whole video untill finish and do otherting for forgot it and try to write code after it, because it will recall from memory combine with understanding not just pure memory. And make me feel great when I refactor code and it didn't break result because it have test!!!

**Pomodoros**: 2.5

## Day 159: Jul 9, 2020

**TIL**: Do an homework for ep4 that make me strongly realize that have test will make me to code very efficient, dare to change, dare to think better.
* Learn about [esModuleInterop](https://stackoverflow.com/questions/56238356/understanding-esmoduleinterop-in-tsconfig-file) flag, just know that import, namespace it must be plain object not callable. And know way to combine commonjs with es6 module and make it callable.

**Thoughts**: This time make me more focus and very enjoy when want to make code look better.

**Pomodoros**: 3

## Day 160: Jul 22, 2020

**TIL**: Learn lecture ep 6

**Thoughts**: This time make me more focus and very enjoy when want to make code look better.

**Pomodoros**: 3

## Day 161: Jul 23, 2020

**TIL**: Assignment ep6 and lecture
* optional chaining

**Thoughts**: 

**Pomodoros**: 3

## Day 162: Oct 14, 2020

**TIL**: Learn how to use widget in python to create UI for predict bear model from fastai.

**Thoughts**: It very fast, easy for demo and deploy model I will learn how to use it with binder tmr. But can't use voila in sagemaker because plugin is incompatible.

**Pomodoros**: 2

## Day 163: Oct 15, 2020

**TIL**: Deploy to Binder with new repo and know about requirement.txt it like package.json in nodejs. Binder is very easy to show notebook and with voila it very greate interactive but I don't know how to layer it properly. Learn to use git repo in notebook sagemaker for push without fill in credential everytime.

**Thoughts**: I will purchase book and review it for chapter 1 and 2 after finish video lesson 3. I want to do more and more.

**Pomodoros**: 4


## Day 164: Oct 19, 2020

**TIL**: It kind of a little deep dive for just MNIST data set. First just create baseline but it very fun thing that accuracy is 95% by just easy math and not use deep learning concept at all. Learn about broadcasting that operate more element wise with easy syntax and do it under the hood. And know a bit about tensor in pytorch.

**Thoughts**: I need to read a book for better understanding because this time is quite more detail even it just little deep dive.

**Pomodoros**: 2

## Day 165: Oct 21, 2020

**ML**: Gradient = slope, I just know it. I hear a concept about fine minimal error rate by diff graph to find bottom but I don't understand it clear till this day. I know why we need to diff becase we need to go to bottom and one thing that can indicate is slope and similar name is gradient. And word descent it mean fall of droping that character to find lowest loss.

**TRADE** I learn about trading and how to use CDC action zone in trading view. That answer me a lot when I have doubt why I not buy on that past situation and see price soar, because I don't have system that clear enough, when to buy when to sell so I just learn form CDC because it very easy to understand.

**Thoughts**: I very excited that I found trading setup like this. I will learn how to backtest. About ML I will get my hand dirty for use tensor in calculate loss and calculate gradient.

**Pomodoros**: 6

## Day 166: Oct 22, 2020

**TIL**: Just answer question in lesson 2 and know a bit on DataBlock and research about refresh token and know about RTR refresh token rotation to prevent stole token. And know about Proof Key for Code Exchange (PKCE) in oauth authorize code that I already seen implementation about code verify and code challenge in my job. It use when cannot store client secret in frontend. and use code challenge and verify instead.

**Thoughts**: I spend too much time for research this token stuff and didn't spend on ML much. But it worth for my job it will reduce a lot of cost.

**Pomodoros**: 3

## Day 167: Oct 25, 2020

**TIL**: Hand on in MNIST. Know about broadcasting in pytorch that sugar syntax and fast. L1, L2 (rmse) implement.

**Thoughts**: It very low level for me now but it very fun and clear understand.

**Pomodoros**: 4

## Day 168: Oct 26, 2020

**TIL**: Review lecture process for create model in 7 step. init -> predict -> loss -> gradient -> step -> repeat predict -> stop when find low loss.

**Thoughts**: Will go hand on this in tmr for better understanding.

**Pomodoros**: 1
















