var fakeData =  [
{
  "January": 35,
  "February": 20,
  "March": 27,
  "April": 32,
  "May": 23,
  "June": 42
}
];
ReactDOM.render(
	<Griddle results={fakeData}/>,
	document.getElementById('table-content')
);
