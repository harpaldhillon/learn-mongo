pipeline {
    agent any
    environment {
        MY_CREDENTIAL_ID = 'my-credential-id'
    }
    stages {
        stage('Use Credentials') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.MY_CREDENTIAL_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    echo "Username: ${env.USERNAME}"
                    // Do something with the credentials
                }
            }
        }
    }
}
