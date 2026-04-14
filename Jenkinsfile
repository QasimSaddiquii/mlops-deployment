@Library('shared-library') _

pipeline {
    agent any
    stages {
        stage('Route Pipeline') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        devPipeline()
                    } else if (env.BRANCH_NAME == 'main') {
                        preProdPipeline()
                    } else if (env.TAG_NAME != null) {
                        prodPipeline()
                    } else {
                        echo "No pipeline defined for this branch."
                    }
                }
            }
        }
    }
}
