pipeline {
    agent any
    stages {
        stage('List Credentials') {
            steps {
                script {
                    import jenkins.model.Jenkins
                    import com.cloudbees.plugins.credentials.CredentialsProvider
                    import com.cloudbees.plugins.credentials.domains.Domain

                    def jenkinsInstance = Jenkins.getInstance()
                    def credentialsStore = jenkinsInstance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

                    def allCredentials = credentialsStore.getCredentials(Domain.global())

                    println "Credential IDs:"
                    allCredentials.each { credential ->
                        println credential.id
                    }
                }
            }
        }
    }
}
