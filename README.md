### Locally testing

First, I developed my web app locally using a Conda environment to manage dependencies, libraries and packages and so ensure consistency without affecting other projects on my local machine.

Within this Conda environment, I built and tested my web app, ensuring it met my requirements and performed as expected. Once satisfied with the local version, I proceeded to deploy it to a production environment using AWS CodePipeline.

AWS CodePipeline allowed me to automate the deployment process, streamlining the steps required to move my web app from development to production. I configured the pipeline to pull the latest version of my code from my repository, run tests to validate its functionality, and then deploy it to Elastic Beanstalk.

By leveraging CodePipeline's integration with Elastic Beanstalk, I could easily deploy and manage my web app in a scalable and reliable environment. This deployment approach ensured that my application was readily available to users while maintaining the flexibility and ease of development provided by Conda locally.

<img align="center" src="https://github.com/GBlanch/Student-Performance-Predictor/blob/main/static%20assets/index.png">

&nbsp; 
&nbsp; 

<img align="center" src="https://github.com/GBlanch/Student-Performance-Predictor/blob/main/static%20assets/predict_data.png">

&nbsp; 
&nbsp; 

<img align="center" src="https://github.com/GBlanch/Student-Performance-Predictor/blob/main/static%20assets/result.png">

