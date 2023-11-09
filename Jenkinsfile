pipeline {
  agent any

  parameters {
    choice(name: 'ReportSelection', choices: ['First_Report', 'Second_Report'], description: 'Please select a report to generate:')
    stashedFile(name: "ReportExtract", description: "Please add extract for report generation:")
  }

  stages {
    // ideally the agent would already have required dependencies, removing the need for this step
    stage('Agent Setup') {
      steps{
        script {
          sh "sudo pip3 install pandas xlrd openpyxl"
        }
      }
    }

    stage('Generate Report') {
      steps {
        script {
          unstash 'ReportExtract'
          def reportSelection = params.ReportSelection
          sh "python main.py ReportExtract ${reportSelection}"
        }
      }
    }

    stage('Create ZIP File') {
      steps {
        sh "zip -r ${reportSelection} ./*.xlsx"
      }
    }

    stage('Create Artifact') {
      steps {
        archiveArtifacts "**/*.zip"
      }
    }

    post {
      always {
        cleanWs()
      }
    }
  }
}
