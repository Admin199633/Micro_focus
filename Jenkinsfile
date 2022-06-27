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
                  stage('Build:Flask.py') {
            steps {
                script {
                    bat 'start /min python Flask.py'
                    bat 'echo success Flask.py'
                }
            }
        }
        stage('Test:Backend_testing') {
            steps {
                script {
                    bat 'start Backend_testing.py'
		    bat 'call Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
	stage('Test:Fronted_testing') {
            steps {
                script {
                    bat 'start Fronted_testing.py'
                    bat 'echo success Fronted_testing'
                }
            }
        }
	stage('Test:clean_environemnt') {
            steps {
                script {
                    bat 'start/min clean_environemnt.py'
                    bat 'echo success clean_environemnt-1'
                 }
            }
        }    
	stage('Depoly:Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t \"$BUILD_NUMBER\" ."
                    bat "start/min docker run -p 8777:8777 $BUILD_NUMBER "
                }
            }
         }
	stage('Deploy: build and push image') {
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
	stage('set version') { 	
            steps {	
                bat "echo image_tag=${BUILD_NUMBER} > .env" 
		bat 'more .env'
	    }
         }
	stage ('Deploy&Operate HM'){
            steps{
                script{
		    bat 'minikube start'
		    bat 'kubectl create deployment %BUILD_NUMBER% --image="%BUILD_NUMBER%":latest'
		    bat 'helm install  test-%BUILD_NUMBER% ./micro --set image_tag=%BUILD_NUMBER%'
		    bat 'helm repo update'
		    bat 'helm list --all'
		    }  
                }
            }
	stage ('Deploy HELM'){
            steps{
                script{
                   bat """ start /min /b minikube service test-%BUILD_NUMBER% --url >  k8s_url-test.txt
		   ping -n 10 127.0.0.1 
                   (type  k8s_url-test.txt | findstr "^http") >  k8s_url.txt
                    type k8s_url.txt """		   
		    }  
                }
            }
	stage ('K8S_backend_testing.py'){
	    steps{
                script{
		    bat 'python K8S_Backend_testing.py'
		    bat 'echo succes K8S_backend_testing.py'
		   }
                }
	    }
    }
  }
