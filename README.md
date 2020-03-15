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
