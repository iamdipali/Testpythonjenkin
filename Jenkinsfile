pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                git url: 'https://github.com/iamdipali/Testpythonjenkin.git', branch: 'main'
            }
        }
        stage('Run Hello World Script') {
            steps {
                echo 'Running the Hello World Python script...'
                bat 'python Hellojentest.py'  // Use `python` or `python3` as appropriate based on your setup
            }
        }
    }
}
