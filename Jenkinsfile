pipeline { 
    agent any
    environment { 
        registry = "photop/micro_focus" 
        registryCredential = 'dockerhub_id'
        dockerImage = ""
    } 
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
		git branch: 'main', url: 'https://github.com/Admin199633/Main.git'
            }
        }
                  stage('Flask.py') {
            steps {
                script {
		    bat 'echo "${BUILD_NUMBER}"'	 
		    bat 'pip install flask'
		    bat 'pip install pymysql'
		    bat 'pip install requests'
		    bat 'pip install selenium'
                    bat 'start /min python Flask.py'
                    bat 'echo success Flask.py'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'start Backend_testing.py'
		    bat 'call Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
	stage('Fronted_testing') {
            steps {
                script {
                    bat 'start Fronted_testing.py'
                    bat 'echo success Fronted_testing'
                }
            }
        }
	stage('clean_environemnt') {
            steps {
                script {
                    bat 'start/min clean_environemnt.py'
                    bat 'echo success clean_environemnt-1'
                 }
            }
        }    
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t \"$BUILD_NUMBER\" ."
                    bat "start/min docker run -p 8777:8777 $BUILD_NUMBER "
                }
            }
         }
	stage('build and push image') {
            steps {
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
		    bat 'echo success Build'
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
	       }
            }
         }     
      }
	stage ('Deploy HM'){
            steps{
                script{
		    bat 'minikube start'
		    bat 'kubectl create deployment k8s --image="${BUILD_NUMBER}":latest'
		    bat 'cd "${BUILD_NUMBER}"'
		    bat	'helm install ./'
		    bat 'helm repo update'
		    bat 'helm list --all'
		    }  
                }
            }
    }
  }

