 node('builder'){
    docker.image('diogorac/rnc_builder').inside('--privileged') {
        checkout scm
        stage('Generating build') {
            sh 'mkdir -p build && cd build && cmake ../ -DTARGET_GROUP=test -DSTATIC_ANALYSIS=1  '
        }
        dir('build')
        {
            stage('Build') {
                sh 'make'
            }
            stage('Testing') {
                sh 'make check'
                sh 'xsltproc /opt/ctest/ctest2junix.xsl Testing/`head -n 1 < Testing/TAG`/Test.xml > CTestResults.xml'
                junit 'CTestResults.xml'
            }
        }
    }
}
