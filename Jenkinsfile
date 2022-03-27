pipeline {
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
        sh """python3 -m pip install --upgrade build \n
        python3 -m build"""
      }
    }

    stage('Build and Run') {
      steps {
        sh """ python3 -m pip install gunicorn \n
        gunicorn -d wsgi:app """
      }
    }
    stage('build docker image'){
         
      steps{
        sh 'docker build -t capstone:${GIT_COMMIT} .'
      }
    }    
  }
}  
