pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '5')) 
    ansiColor('xterm') 
    timestamps() 
    timeout(time: 20, unit: 'MINUTES') 
  }
  agent any
  stages {  
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup') { 
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Linting') { 
      steps {
        script {
          sh """
          pylint **/*.py
          """
        }
      }
    }
    stage('Unit Testing') {
      steps {
        script {
          sh """
          python -m unittest discover -s tests/unit
          """
        }
      }
    }
    stage('Integration Testing') { 
      steps {
        script {
          sh """
          python -m unittest discover -s tests/integration
        """
      }
    }
  }
}  