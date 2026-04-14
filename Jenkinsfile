@Library('shared-library') _

if (env.BRANCH_NAME == 'dev') {
    devPipeline()
} else if (env.BRANCH_NAME == 'main') {
    preProdPipeline()
} else if (env.TAG_NAME != null) {
    prodPipeline()
} else {
    echo "No pipeline defined for this branch."
}
