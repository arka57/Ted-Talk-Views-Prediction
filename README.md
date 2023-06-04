# Ted-Talk-Views-Prediction


TED is devoted to spreading powerful ideas on just about any topic. Founded in 1984 by Richard Salman as a nonprofit organization that aimed at bringing experts from the fields of Technology, Entertainment, and Design together, TED Conferences have gone on to become the Mecca of ideas from virtually all walks of life<br>
These dataset contain over 4,000 TED talks including transcripts in many languages and  main objective was to build a model for predicting  views generated for these events from thr dataset.<br>

# **Dataset info**

Number of records: 4,005<br>
Number of attributes: 19<br>

# **Features information:**<br>

The dataset contains features like:<br>

**talk_id**: Talk identification number provided by TED<br>
**title**: Title of the talk<br>
**speaker_1**: First speaker in TED's speaker list<br>
**all_speakers**: Speakers in the talk<br>
**occupations**: Occupations of the speakers<br>
**about_speakers**: Blurb about each speaker<br>
**recorded_date**: Date the talk was recorded<br>
**published_date**: Date the talk was published to TED.com<br>
**event**: Event or medium in which the talk was given<br>
**native_lang**: Language the talk was given in<br>
**available_lang**: All available languages (lang_code) for a talk<br>
**comments**: Count of comments<br>
**duration**: Duration in seconds<br>
**topics**: Related tags or topics for the talk<br>
**related_talks**: Related talks (key='talk_id',value='title')<br>
**url**: URL of the talk<br>
**description**: Description of the talk<br>
**transcript**: Full transcript of the talk<br><br>
**Target Variable** :<br>
**views**: Contains Count of views of every talk

# **Data Pre-Processing and Feature Engineering**<br>
**1)Duplicate Rows:** No Duplicate Rows were present<br><br>
**2)Handling Missing Values:** <br><br>
      **occupation:** NULL values were replaced with 'Others'<br>
      **about_speakers:** NULL values were replaced with 'NA'<br>
      **comments:** NULL values were replaced with extreme value 0<br>
      **recorded_date,all speakers have very less number of NULL values(<1%): Rows were deleted**<br><br>
**3)Outlier Handling:** For numerical columns,outlier values were replaced with median<br><br>
**4)Feature Engineering:**
  --New Column **time_since_published** was created for storing how old the video is. Was calculated on the basis of the difference between last published date of any vdeo(last date assumed) and published   date of the current video<br>
  --New Column **daily_views** was created as it is better metric. Was calculated as views/time_since_published<br>
  --New Column **avg_speaker_1_views** was created as correlation between a particular spekaer and  average views of his/her videos<br>
  --New Column **is_weekend** was created to check whether the video released on weekdays or weekends<br>
  --New Column **available_lang_count** was created to store in how many languages a video is avialable<br>
  --New Column **topics_count**  was created to store  how many topics are present in a video<br>
  --New Column **avg_event_views**  was created to store  how many topics are present in a video<br><br>
# **EDA**<br>
EDA was performed on the dataset to gain insights on the dataset<br>
Following type of visulaizations were used:<br>
--Bar Plot<br>
--Box Plor<br>
--Scatter Plot<br>
--Count Plot<br><br>
# **Models Used**<br>
The dataset was divided in train and test set in the ratio of 80:20 .Various models were tried upon the dataset  such as Linear Regression and tree based models like Decision Tree, Random Forest. To reduce overfitting hyperparameter tuning was applied on each of the models to enhance the output of the model.<br><br>

# **Results**<br>
 Random Forest with regularization using GridSearch performed the best among the models with least overfitting. Due to training time resource constraint XGBoost was not applied. The result were evaluated on various parameters like MSE,MSRT and R2 scores<br>


# **Scores**<br>

| **Model**        | **MSE Training Score** |**MSE Test Score**  | **MSRT Training Score** | **MSRT Test Score**|**R2 Training Score** | **R2 Test Score**| 
|------------------|--------------------|----------------|---------------------|-----------------|------------------|--------------|
|Linear Regression |     13734743.9833               | 9048703.5828  |  3706.0415          |    3008.1063   |   0.7622         |     0.8102   | 
|L1 Regression     |     13811142.7076  |  8688681.1133  |   3716.3345         |     2947.6568   |   0.7608         |  0.8178      |              
|L2 Regression     |     13764151.3081  | 8907230.4988   |   3710.0069         |   2984.4983     | 0.7616           |0.8132        |
|Decision Tree     |    11233973.1642   |  18367479.3015 |   3351.7119         | 4285.7297       | 0.8054           |  0.6149      |
|Random Forest     |    2629275.8123    | 7230347.4333   |    1621.5041        | 2688.9305       |   0.9544         |   0.8484     |
|Gradient Boosting |    459258.8654     |  8088584.9908  |  677.6864           | 2844.0437       |  0.9920          | 0.8304       |
|XGBoosting        |   5734634.3142     | 11262460.5049  |  2394.7096          | 3355.9589       | 0.9007           | 0.7638       |
<br>
**Conclusion**<br>
Random Forest and XGBoosting are the two best performing models and R2 score above 0.9 was achieved by them. Hence Random Forest with hyperparameter tuning is the best  working model for the given problem
<br>Further the model was deployed on AWS EC2 instance along with Dockerization

# **Tool and Technologies used**<br>
Colab IDE,VSCode,AWS EC2,WinSCP,Putty,Docker<br><br>
# **Further scope**<br>
1) Applying NLP concepts to include title feature and check it's effect on views<br>
2) Use Related topics feature of a video and use it in the prediction
