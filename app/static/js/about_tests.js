var LinkComponent = React.createClass({
  render: function(){
    url ="speakers/" + this.props.rowData.state + "/" + this.props.data;
    return <a href={url}>{this.props.data}</a>
  }
});


// this is what the example run tests does,
// i'll need to modify it to work in React...
.factory('unitTestService', function($http) {
  return {
    runUnitTests : function() {
      return $http.get('/run_tests').then(function(result){
        return result.data;
      });
    }
  }
}


//this was in a python file and is what the thing up there is calling
# ---------
# run_tests
# ---------

@app.route('/run_tests')
def run_tests():
    output = subprocess.getoutput("python tests.py")
    return json.dumps({'output': str(output)})
