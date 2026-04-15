@Library('shared-library') _

node {
    try {
        stage('Run Logic') {
            if (env.BRANCH_NAME == 'dev') {
                devPipeline()
            } else if (env.BRANCH_NAME == 'main') {
                preProdPipeline()
            } else if (env.TAG_NAME != null) {
                prodPipeline()
            }
        }
    } finally {
        emailext (
            subject: "MLOps Notification: ${env.JOB_NAME} [${currentBuild.result ?: 'SUCCESS'}]",
            body: "The pipeline for ${env.BRANCH_NAME ?: env.TAG_NAME} has finished.\nResult: ${currentBuild.result ?: 'SUCCESS'}\nURL: ${env.BUILD_URL}",
            to: 'sikandar.hayat@uol.edu.pk'
        )
    }
}
