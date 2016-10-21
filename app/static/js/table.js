var LinkComponent = React.createClass({
render: function(){
  url ="speakers/" + this.props.rowData.state + "/" + this.props.data;
  return <a href={url}>{this.props.data}</a>
}
});