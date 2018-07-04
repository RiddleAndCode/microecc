 node('builder'){
    docker.image('diogorac/rnc_builder').inside('--privileged') {
        checkout scm
        stage('Generating build') {
            sh 'mkdir -p build && cd build && cmake ../ -DTARGET_GROUP=test -DSTATIC_ANALYSIS=1  '
        }
        stage('Build') {
            sh 'cd build'
            sh 'make'
        }
        stage('Testing') {
            sh 'cd build'
            sh 'make check'
        }
    }
}
