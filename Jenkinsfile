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
          sudo apt install pylint -y \n
          sudo apt install python3-testresources -y \n
          pip3 install -r requirements.txt
          """
        
      }
    }
    stage('Linting') { 
      steps {
          sh """
          pylint **/*.py
          """
      }
    }
    stage('Unit Testing') {
      steps {
          sh """
          python3 -m unittest discover -s tests/unit
          """
      }
    }
    stage('Integration Testing') { 
      steps {
          sh """
          python3 -m unittest discover -s tests/integration
        """
    }
   }
  }
}  
