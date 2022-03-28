pipeline {
  agent any
   environment {
      dockerhub=credentials('dockerhub')
   }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
    timestamps() 
    timeout(time: 20, unit: 'MINUTES') 
  }
  
  stages {  
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vaibhavkumar779/FinalDevOpsKUP.git']]])
      }
    }
    stage('Setup') { 
      steps {
          sh " pip3 install -r requirements.txt "
      }
    }
    
    stage('Linting') { 
      steps {
        script {
          sh """
          pylint -E **/*.py
          """
        }
      }
    }
 
    stage('Testing') {
      steps {
          sh """
          python3 -m pytest
          """
      }
    }

    stage('Build Archive') {
      steps {
        sh """ python3 -m build"""
      }
    }

    //stage('Build and Run') {
    //  steps {
    //    sh """ nohup python3 -m gunicorn  wsgi:app """
    //  }
    //}
     stage("building docker image"){
                    steps{
                      sh 'docker build -t capstone:${GIT_COMMIT} .'
                       
                     }    
                }
            stage("Pushing the docker image"){
                    steps{
                      sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
                      sh 'docker tag capstone:${GIT_COMMIT} vaibhavkuma779/meanreview:${GIT_COMMIT}'
                      sh 'docker push  vaibhavkuma779/meanreview:${GIT_COMMIT}'
                      sh 'docker tag capstone:${GIT_COMMIT} vaibhavkuma779/meanreview:latest'
                      sh 'docker push  vaibhavkuma779/meanreview:latest'
                    }
                }

  }
}  
