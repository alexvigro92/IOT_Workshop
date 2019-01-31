angular.module('iotProyect').controller('chartController', ['$scope', '$http', function($scope, $http) {
  console.log('hello charts');

  $scope.tempValue;
  $scope.humValue;
  $scope.dateValue;
  $scope.timeValue;

  setInterval(function() {
    $http({
      method: 'GET',
      url: '/api/raspberry'
    }).then(function successCallback(response) {
      var responseJson = angular.fromJson(response.data.results);
      $scope.tempValue = parseInt(responseJson.temp, 10);
      $scope.humValue = parseInt(responseJson.hum, 10);
      $scope.dateValue = responseJson.date
      $scope.timeValue = responseJson.time

      if (myLineChartTemp.data.labels.length === 10) {

        // Data of temperature chart
        myLineChartTemp.data.datasets[0].data.shift();
        myLineChartTemp.data.labels.shift();
        myLineChartTemp.data.labels.push($scope.timeValue);
        myLineChartTemp.data.datasets[0].data.push($scope.tempValue);

        // Data of humidity chart
        myLineChartHum.data.datasets[0].data.shift();
        myLineChartHum.data.labels.shift();
        myLineChartHum.data.labels.push($scope.timeValue);
        myLineChartHum.data.datasets[0].data.push($scope.humValue);

      } else {

        // Data of temperature chart
        myLineChartTemp.data.labels.push($scope.timeValue);
        myLineChartTemp.data.datasets[0].data.push($scope.tempValue);

        // Data of humidity chart
        myLineChartHum.data.labels.push($scope.timeValue);
        myLineChartHum.data.datasets[0].data.push($scope.humValue);

      }
      myLineChartTemp.update();
      myLineChartHum.update();

    }, function errorCallback(response) {
      console.log("Fallo");
    });
  }, 3000);

  var canvasTemp = document.getElementById('myChartTemp');
  var data = {
    labels: [],
    datasets: [{
      label: "Temperature",
      fill: true,
      lineTension: 0.1,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 10,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 5,
      pointHitRadius: 10,
      data: [],
    }]
  };

  var option = {
    showLines: true
  };

  var myLineChartTemp = Chart.Line(canvasTemp, {
    data: data,
    options: option
  });

  var canvasHum = document.getElementById('myChartHum');
  var data = {
    labels: [],
    datasets: [{
      label: "Humidity",
      fill: true,
      lineTension: 0.1,
      backgroundColor: "rgba(255, 0, 0  ,0.4)",
      borderColor: "rgba(255, 0, 0,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 10,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(255, 0, 0,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(255, 0, 0  ,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 5,
      pointHitRadius: 10,
      data: [],
    }]
  };

  var option = {
    showLines: true
  };

  var myLineChartHum = Chart.Line(canvasHum, {
    data: data,
    options: option
  });

}]);
