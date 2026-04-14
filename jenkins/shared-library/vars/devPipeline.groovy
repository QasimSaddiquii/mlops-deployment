def call() {
    pipeline {
        agent any
        stages {
            stage('Data Ingest') { steps { sh 'python3 src/ingest.py' } }
            stage('Model Train & Register') { steps { sh 'python3 src/train.py' } }
            stage('Model Deploy') { steps { echo 'Deploying model via MLflow' } }
            stage('Model Test') { 
                steps { 
                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        sh 'python3 src/test.py'
                    }
                }
            }
        }
        post { failure { echo 'Send Email: Dev Pipeline Failed' } }
    }
}
