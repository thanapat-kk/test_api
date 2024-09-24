pipeline {
    agent none
    stages {
        stage('Agent tester') {
            agent { label 'vm2-tester' }
            environment {
                DOCKER_IMAGE_NAME = ""
                DOCKER_IMAGE_TAG = "latest"
                GIT_CREDENTIALS = "github_user" 
                GIT_BRANCH = "main"
            }
            stages {
                stage("Clone repository into 'app' directory") {
                    steps {
                        script {
                            withCredentials([usernamePassword(
                                credentialsId: "github_user", 
                                usernameVariable: "GIT_USERNAME", 
                                passwordVariable: "GIT_PASSWORD")]) {
                                
                                if (fileExists('Jenkin')) {
                                    dir('Jenkin') {
                                        sh "git pull origin main"
                                    }
                                } else {
                                    sh "git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com/thanapat.pi1999/flask_api.git"
                                }   
                            }
                        }
                    }
                }
                
                stage("Unit Test") {
                    steps {
                        script {
                            dir('flask_api') {
                                sh '''
                                    . /home/test/path/to/venv/bin/activate
                                    python -m unittest  /home/test/flask_api/test_script.py
                                '''
                            }
                        }
                    }
                }
                
                stage("Build Docker Image") {
                    steps {
                        script {
                            dir("flask_api") {
                                sh "docker build -t plusapp ."
                            }
                        }
                    }
                }
                
                stage("Run Docker Container") {
                    steps {
                        script {
                            sh "docker ps -a -q -f name=plusapp | xargs -r docker rm -f"
                            sh "docker run -d --name plusapp -p 8080:5000 plusapp"
                        }
                    }
                }
                
                stage("Clone Repository From robot_test") {
                    steps {
                        script {
                            withCredentials([usernamePassword(
                                credentialsId: "gitlab-user", 
                                usernameVariable: "GIT_USERNAME", 
                                passwordVariable: "GIT_PASSWORD")]) {
                                
                                if (fileExists('robot_test')) {
                                    dir('robot_test') {
                                        sh "git pull origin main"
                                    }
                                } else {
                                    sh "git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com/thanapat.pi1999/robot_test.git"
                                }
                            }
                        }
                    }
                }
                
                stage("Run Robot-Test") {
                    steps {
                        script {
                            dir('robot_test') {
                                sh '''
                                    . /home/test/path/to/venv/bin/activate
                                    robot /home/test/robot_test/robot.robot
                                '''
                                sh "docker ps -q -f name=plusapp | xargs -r docker stop"
                            }
                        }
                    }
                }
                
                stage('Push Docker Image') {
                    steps {
                        script {
                            withCredentials([usernamePassword(
                                credentialsId: "github_user", 
                                usernameVariable: "GIT_USERNAME", 
                                passwordVariable: "GIT_PASSWORD")]) {
                                
                                sh "docker login -u ${GIT_USERNAME} -p ${GIT_PASSWORD} registry.gitlab.com"
                                sh "docker tag plusapp registry.gitlab.com/sdp4164938/robot_test:latest"
                                sh "docker push registry.gitlab.com/sdp4164938/robot_test:latest"
                            }
                        }
                    }
                }
            }
        }
        
        stage('Agent Pre-Prod Server') {
            agent { label "vm3-pred" }
            stages {
                stage("Pull Docker Image") {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: "github_user", 
                                                             usernameVariable: "GIT_USERNAME", 
                                                             passwordVariable: "GIT_PASSWORD")]) {
                                sh "docker login -u ${GIT_USERNAME} -p ${GIT_PASSWORD} registry.gitlab.com"
                                sh "docker pull registry.gitlab.com/sdp4164938/robot_test:latest"
                            }
                        }
                    }
                }

                stage("Run Docker Container") {
                    steps {
                        script {
                            sh "docker ps -a -q -f name=plusapp | xargs -r docker rm -f"
                            sh "docker run -d --name plusapp -p 8080:5000 registry.gitlab.com/sdp4164938/robot_test:latest"
                        }
                    }
                }
            }
        }
    }
}
