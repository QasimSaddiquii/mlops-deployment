@Library('shared-library') _

pipeline {
    agent any
    stages {
        stage('Run Pipeline Logic') {
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
    
    // --- YE WALA HISSA EMAIL KE LIYE HAI ---
    post {
        always {
            emailext (
                subject: "MLOps Notification: ${env.JOB_NAME} [${currentBuild.result}]",
                body: "Hello Sir,\n\nThe pipeline for ${env.BRANCH_NAME ?: env.TAG_NAME} has finished.\nResult: ${currentBuild.result}\nBuild URL: ${env.BUILD_URL}",
                to: 'apne_teacher_ki_email@uol.edu.pk'
            )
        }
    }
}
