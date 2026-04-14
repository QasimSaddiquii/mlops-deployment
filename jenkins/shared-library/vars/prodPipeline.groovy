def call() {
    pipeline {
        agent any
        stages {
            stage('Assign Champion Alias') { steps { sh 'python3 src/promote.py Challenger-post-test Champion' } }
            stage('Production Deploy') { steps { echo 'Model ready for production!' } }
        }
    }
}
