 node('builder'){
    docker.image('diogorac/rnc_builder').inside('--privileged') {
        checkout scm
        stage('Generating build') {
            steps {
              sh 'mkdir -p build && cd build && cmake ../ -DTARGET_GROUP=test -DSTATIC_ANALYSIS=1  '
            }
        }
        stage('Build') {
            steps {
              sh 'make'
            }
        }
        stage('Testing') {
            steps {
              sh 'make check'
            }
        }
    }
}
