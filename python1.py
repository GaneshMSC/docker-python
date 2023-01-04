pipeline {
  agent any 
  stages {
    stage(checkout) {
      steps {
      echo "this is the simple pipeline script"
      }
    }
  }
}
