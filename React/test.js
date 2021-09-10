import React from 'react';
import ReactDOM from 'react-dom';

//"Hello, 홍길동!"을 출력하는 코드

const App = ({name}) => <h1>Hello, {name}!</h1> //함수형 문법

class App extends React.Component { //클래스형 문법
  render() {
    return (
      <h1>Hello, {this.props.name}!</h1>
    )
  }
}

ReactDOM.render(<App name="홍길동" />, document.getElementById('root'));