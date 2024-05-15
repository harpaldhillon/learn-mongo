pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                script{
                    println params['PATH']
                    println checkAplhebetic(params['PATH'])
                }
            }
        }
    }
}

def checkAplhebetic(variable){
    // Check if the variable contains only alphabetical characters
    if (variable ==~ /^[a-zA-Z]+$/) {
        return true
    } else {
        return false
    }   
}
