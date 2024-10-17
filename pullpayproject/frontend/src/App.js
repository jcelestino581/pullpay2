import axios from 'axios';
import React from 'react';

class App extends React.Component {
  state = { details: [] };

  componentDidMount() {
    let data;
    axios.get('http://127.0.0.1:8000/home')
      .then(res => {
        data = res.data;
        this.setState({
          details: data
        });
      });
  }

  render() {
    return (
      <div>
        <header> Data Generated from Django </header>
        <hr></hr>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h2> {output.church_name_text} </h2>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
