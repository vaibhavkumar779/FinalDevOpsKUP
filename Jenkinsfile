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
        git branch: 'main', url: 'https://github.com/vaibhavkumar779/FinalDevOpsKUP'
          sh """
          pip3 install -r requirements.txt
          """
        
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
    
  }
}  
