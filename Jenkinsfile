pipeline {
	agent any
	environment {
		IMAGE='opancart_tests_image'
		CONTAINER='opancart_tests_container'
	}
	parameters{
        string name: 'URL', defaultValue: 'http://192.168.0.14', description: 'Opencart url'
        string name: 'PORT', defaultValue: ':8081', description: 'Opencart port'
        string name: 'EXECUTOR', defaultValue: '192.168.0.14', description: 'Selenoid IP'
        string name: 'THREADS', defaultValue: '1', description: 'Number of threads'
        string name: 'BROWSER', defaultValue: 'chrome', description: 'Browser name'
        string name: 'BROWSER_VERSION', defaultValue: '114.0', description: 'Browser version'
        booleanParam name: 'MOBILE', defaultValue: false, description: 'Run tests in mobile browser version'
        choice choices: ['Pixel 5', 'iPhone XR'], name: 'MOBILE_DEVICE', description: 'Choice mobile device. Use only with mobile browser version'
        string name: 'TEST_NAME', defaultValue: 'tests/', description: 'Run all tests or selected test'
	}
	stages {
		stage('Get tests') {
			steps {
				git branch: 'main', url: 'https://github.com/RandolphKarter/otus_opencart.git'
			}
		}
		stage('Build') {
			steps {
				sh 'docker build -t ${IMAGE} .'
			}
		}
		stage('Run tests') {
			steps {
			    script {
    			    if (params.MOBILE == true) {
    				    sh 'docker run --name ${CONTAINER} -t ${IMAGE} -k ${TEST_NAME} --headless --url ${URL} --port ${PORT} --executor ${EXECUTOR} -n ${THREADS} --browser ${BROWSER} --browser_version ${BROWSER_VERSION} --mobile "${MOBILE_DEVICE}"'
    			    } else {
    			        sh 'docker run --name ${CONTAINER} -t ${IMAGE} -k ${TEST_NAME} --headless --url ${URL} --port ${PORT} --executor ${EXECUTOR} -n ${THREADS} --browser ${BROWSER} --browser_version ${BROWSER_VERSION}'
    			    }
			    }
			}
		    post {
		        always {
		            sh 'docker cp ${CONTAINER}:/usr/src/app/allure-results .'
                    script {
                        allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-results']]
                        ])
                    }
                    sh 'docker stop ${CONTAINER}'
				    sh 'docker rm -f ${CONTAINER}'
                    sh 'docker rmi ${IMAGE}'
                    sh 'rm -r allure-results/*'
                }
			}
		}
	}
}