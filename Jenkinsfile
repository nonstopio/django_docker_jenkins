node {

    stage ("Get Latest Code") {
        checkout scm
    }

    stage ("Install Application Dependencies") {
        sh 'pip3 install -r requirements.txt'
    }

    stage('Build') {
        echo 'Building..'
        sh '''
            python3.5 manage.py makemigrations app
            python3.5 manage.py migrate
           '''
    }

    stage ("Run Unit/Integration Tests") {
        echo 'Testing..'

        def testsError = null
        try {
            sh '''
                python3.5 manage.py test
               '''
        }
        catch(err) {
            testsError = err
            currentBuild.result = 'FAILURE'
        }
        finally {
            junit 'reports/junit.xml'

            if (testsError) {
                throw testsError
            }
        }
    }

    stage('Deploy') {
        echo 'Deploying TBD....'
    }
}