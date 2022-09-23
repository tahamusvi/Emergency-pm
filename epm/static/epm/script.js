(function() {
  var app = angular.module('chatApp', []);

  app.controller('MessageCtrl', function($scope) {
    $scope.messages = [{
      Name: 'George Clooney',
      Message: "The only failure is not to try"
    }, {
      Name: 'Seth Rogen',
      Message: "I grew up in Vancouver, man. That's where more than half of my style comes from."
    }, {
      Name: 'John Lydon',
      Message: "There's nothing glorious in dying. Anyone can do it."
    }];
  });

})();