import React from 'react'

import TextField from '@material-ui/core/TextField';

class InputField extends React.Component {
    constructor(props) {
        super(props)
        this.state = { input: '' }
    }

    handleInputChange = (text) => {
        this.setState({ input: text })
        this.props.inputValue(text)
    }

    render() {
        return (
            <div>
                <TextField 
                    label={this.props.label}
                    value={this.state.input}
                    onChange={(event) => this.handleInputChange(event.target.value)}
                    autoFocus={true}
                    placeholder= {`Name of ${this.props.label}`}
                />
            </div>
        )
    }
}

export default InputField