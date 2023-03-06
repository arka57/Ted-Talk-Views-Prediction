# Ted-Talk-Views-Prediction


TED is devoted to spreading powerful ideas on just about any topic. Founded in 1984 by Richard Salman as a nonprofit organization that aimed at bringing experts from the fields of Technology, Entertainment, and Design together, TED Conferences have gone on to become the Mecca of ideas from virtually all walks of life<br>
These dataset contain over 4,000 TED talks including transcripts in many languages and  main objective was to build a model for predicting  views generated for these events.<br>

**Dataset info**

Number of records: 4,005<br>
Number of attributes: 19<br>

**Features information:**<br>

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

**Approach**<br>
Firstly EDA was performed on data to gain insights followed by Feature Engineering to remove unrelated columns and make it apt for model. Various models were tried upon the dataset such as Linear Regression and tree based models like Decision Tree, Random Forest. To reduce overfitting hyperparameter tuning was applied on each of the models to enhance the output of the model.<br><br>

**Results**:Random Forest with regularization using GridSearch performed the best among the models with least overfitting. Due to training time resource constraint XGBoost was not applied. The result were evaluated on various parameters like MSE,MSRT and R2 scores

**Scores**<br>
**Model**: Linear Regression<br>
                                     
|  Metric   | Training Score|  Testing Score |          
|-----------|---------------|----------------|            
|MSE        |  0.12010      |    0.12392     |         
|MSRT       |  0.34656      |    0.35202     |   
|R2         |  0.28532      |    0.29001     |  
<br> 

**Scores**<br>
**Model**: L1 Regression<br>
                                     
|  Metric   | Training Score|  Testing Score |          
|-----------|---------------|----------------|            
|MSE        |  0.12010      |    0.12392     |         
|MSRT       |  0.34656      |    0.35202     |   
|R2         |  0.28532      |    0.29001     |  
<br>

**Scores**<br>
**Model**: L2 Regression<br>
                                     
|  Metric   | Training Score|  Testing Score |          
|-----------|---------------|----------------|            
|MSE        |  0.12010      |    0.12392     |         
|MSRT       |  0.34656      |    0.35202     |   
|R2         |  0.28532      |    0.29001     |  
<br>

**Scores**<br>
**Model**: Decision Tree<br>

|  Metric   | Training Score|  Testing Score |          
|-----------|---------------|----------------|            
|MSE        |  0.12010      |    0.12392     |         
|MSRT       |  0.34656      |    0.35202     |   
|R2         |  0.28532      |    0.29001     |  
<br>

**Scores**<br>
**Model**: Random Forest<br>
                                     
|  Metric   | Training Score|  Testing Score |          
|-----------|---------------|----------------|            
|MSE        |  0.12010      |    0.12392     |         
|MSRT       |  0.34656      |    0.35202     |   
|R2         |  0.28532      |    0.29001     |  
<br>

<br>Further the model was deployed on AWS EC2 instance along with Dockerization

**Tool and Technologies used**: Colab IDE,VSCode,AWS EC2,WinSCP,Putty,Docker
<br>
Further scope is train with XGBoost model on the dataset
