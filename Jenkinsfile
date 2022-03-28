pipeline {
  environment {
        dockerhub_repo = 'vaibhavkuma779/meanreview'
        dockerhub_creds = 'dockerhub'
        dockerImage=''
    
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
    timestamps() 
    timeout(time: 20, unit: 'MINUTES') 
  }
  agent any
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
                        script{
                            dockerImage = docker.build dockerhub_repo + ":$GIT_COMMIT"
                        }
                       
                     }    
                }
            stage("Pushing the docker image"){
                    steps{
                        script {
                            docker.withRegistry('', dockerhub_creds){
                                dockerImage.push()
                                dockerImage.push('latest')
                                dockerImage.push('$BUILD_NUMBER')
                            }
                        }
                    }
                }
    stage('Remove Unused docker image') {
             steps{
                    sh "docker rmi $(docker images -q)"
                    }
              }
  }
}  
