properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
        git "https://github.com/michaelvaknin/DevOps3006.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
