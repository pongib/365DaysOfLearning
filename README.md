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
