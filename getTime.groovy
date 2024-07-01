pipeline {
    agent any
    stages {
        stage('Get Timestamp Groovy') {
            steps {
                script {
                    def timestamp = new Date().format("yyyyMMddHHmmss")
                    echo "Current timestamp: ${timestamp}"
                }
            }
        }
        stage('Get Timestamp Bash') {
            steps {
                script {
                    def timestamp = sh(returnStdout: true, script: 'date +%Y%m%d%H%M%S').trim()
                    echo "Current timestamp: ${timestamp}"
                }
            }
        }
    }
}
