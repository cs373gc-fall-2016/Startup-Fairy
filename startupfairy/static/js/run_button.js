"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var RunButton = function (_React$Component) {
  _inherits(RunButton, _React$Component);

  function RunButton() {
    _classCallCheck(this, RunButton);

    return _possibleConstructorReturn(this, (RunButton.__proto__ || Object.getPrototypeOf(RunButton)).apply(this, arguments));
  }

  _createClass(RunButton, [{
    key: "getInitialState",
    value: function getInitialState() {
      return {
        isLoading: false
      };
    }
  }, {
    key: "render",
    value: function render() {
      var isLoading = this.state.isLoading;
      return React.createElement(
        "button",
        {
          className: "testButton",
          onClick: !isLoading ? this.handleClick : null },
        React.createElement(
          "h3",
          null,
          "Run Tests!"
        )
      );
    }
  }, {
    key: "handleClick",
    value: function handleClick() {
      var _this2 = this;

      this.setState({ isLoading: true });

      // This probably where you would have an `ajax` call
      setTimeout(function () {
        // Completed of async action, set loading state back
        _this2.setState({ isLoading: false });
      }, 2000);
    }
  }]);

  return RunButton;
}(React.Component);

var TestResults = function (_React$Component2) {
  _inherits(TestResults, _React$Component2);

  function TestResults() {
    _classCallCheck(this, TestResults);

    return _possibleConstructorReturn(this, (TestResults.__proto__ || Object.getPrototypeOf(TestResults)).apply(this, arguments));
  }

  _createClass(TestResults, [{
    key: "render",
    value: function render() {
      var results = '[Test Results Here]';
      return React.createElement(
        "div",
        null,
        React.createElement(
          "div",
          { className: "testPanel" },
          results
        )
      );
    }
  }]);

  return TestResults;
}(React.Component);

var Tester = function (_React$Component3) {
  _inherits(Tester, _React$Component3);

  function Tester() {
    _classCallCheck(this, Tester);

    return _possibleConstructorReturn(this, (Tester.__proto__ || Object.getPrototypeOf(Tester)).apply(this, arguments));
  }

  _createClass(Tester, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "div",
          { className: "testPanel" },
          React.createElement(TestResults, null)
        ),
        React.createElement(RunButton, null)
      );
    }
  }]);

  return Tester;
}(React.Component);

// ========================================

ReactDOM.render(React.createElement(Tester, null), document.getElementById('testSection'));
