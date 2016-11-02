var LinkComponent = React.createClass({
  render: function(){
    url ="speakers/" + this.props.rowData.state + "/" + this.props.data;
    return <a href={url}>{this.props.data}</a>
  }
});


// this is what the example thing does...
.factory('unitTestService', function($http) {
  return {
    runUnitTests : function() {
      return $http.get('/run_tests').then(function(result){
        return result.data;
      });
    }
  }
}
