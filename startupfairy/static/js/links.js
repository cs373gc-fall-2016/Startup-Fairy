var WebsiteLink = React.createClass({
  render: function(){
    if (this.props.data === undefined || this.props.data === null) {
      return <p>No website</p>
    }
    return <a href={this.props.data}>{this.props.data}</a>  
  }
});


var TwitterLink = React.createClass({
  render: function() {
    var name = this.props.data;
    if (name !== undefined && name != null) {
      var url = "http://twitter.com/" + name;
      return <a href={url}>@{name}</a>
    } else {
      return <p>No twitter</p>
    }
  }
});


var EntityLink = React.createClass({
  render: function(){
    var name = this.props.data;
    if (name !== undefined && name != null) {
      var url = this.props.metadata.customHeaderComponentProps.link + name;
      return <a href={url}>{this.props.data}</a>
    } else {
      return <p>No {this.props.metadata.customHeaderComponentProps.category} listed</p>
    }
  }
});

var SmallList = React.createClass({
  render: function() {
    var data = JSON.parse(this.props.data);
    var category = this.props.metadata.customHeaderComponentProps.category;
    if (data.length <= 0) {
      return <p>No {category}</p>
    }
    var entityArray = [];
    var max = data.length > 3 ? 3 : data.length;
    var listItems = [];
    if (data[0] instanceof Array) {
      var listItems = [];
      // TODO change to startupfair.com
      //if (category === 'financial organizations') {
      //  console.log("Had to change");
      //  category = 'financialorgs';
      //}
      var base_url = "http://localhost/category/" + category + "/";
      for (var i = 0; i < data.length; i++) {
        var url = base_url + data[i][1];
        if (data[i][0]!== undefined && data[i][0] !== null) {
          listItems.push(<li><a href={url}>{data[i][0]}</a></li>);
        }
      }
      listItems.splice(max);
    } else {
      entityArray = data.splice(max);
      var listItems = entityArray.map((number) =>
        <li>{number}</li>
      );
    }
    return <ul className="no-indent">{listItems}</ul>
  }
});


export {EntityLink, TwitterLink, WebsiteLink};