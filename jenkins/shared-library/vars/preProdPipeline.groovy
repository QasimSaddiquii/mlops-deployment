def call() {
    pipeline {
        agent any
        stages {
            stage('Assign Pre-test Alias') { steps { sh 'python3 src/promote.py Challenger Challenger-pre-test' } }
            stage('Model Test') { steps { sh 'python3 src/test.py' } }
            stage('Assign Post-test Alias') { steps { sh 'python3 src/promote.py Challenger-pre-test Challenger-post-test' } }
        }
        post { failure { echo 'Send Email: Pre-prod Failed' } }
    }
}
