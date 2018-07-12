node('builder'){
    docker.image('diogorac/rnc_builder').inside('--privileged') {
        
        scmv = checkout scm
        def server = Artifactory.server 'conan'
        def client = Artifactory.newConanClient()
        def serverName = client.remote.add server: server, repo: "conan-local"
        
        stage('Generating build') {
            // When making pull request make sure only develop and master push to conan
            client.run(command: "create . " + scmv.GIT_BRANCH + "/" + scmv.GIT_COMMIT.take(6))
            sh 'mkdir -p build && cd build && cmake ../ -DTARGET_GROUP=test -DSTATIC_ANALYSIS=1  '
        }
        stage('Coding Guideline') {
                sh 'astyle "src/*.c" "include/*.h" "tests/*.c" "tests/*.h" --style=google -s2'
                sh 'echo \'if [ $(find . -iname "*.orig" | wc -l) -eq 0 ]; then echo "According to guideline."; else echo "Not according to guideline" && exit 1; fi\' > guide && sh guide'
        }
        dir('build')
        {
            stage('Build') {
                sh 'make'
            }
            stage('Testing') {
                sh 'make check'
                sh 'xsltproc /opt/ctest/ctest2junix.xsl tests/Testing/$(head -1 tests/Testing/TAG)/Test.xml > CTestResults.xml '
                junit 'CTestResults.xml'
                cobertura coberturaReportFile: 'coverage.xml'
            }
        }
        stage('Pushing to Artifactory') {
            String command = "upload * --all -r ${serverName} --confirm"
            def b = client.run(command: command)
            server.publishBuildInfo b
        }
    }
}