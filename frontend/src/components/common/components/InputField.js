import React from 'react'

import TextField from '@material-ui/core/TextField';
import { createMuiTheme,MuiThemeProvider } from '@material-ui/core'
import { WithStyles, makeStyles } from "@material-ui/styles";

const color = "#f00";

const listStates = [ "AK","AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]

const theme = createMuiTheme({
    overrides: {
      MuiInput: {
        underline: {
          "&:before": {
            borderBottom: `1px solid white`
          }
        }
      }
    }
  });

class InputField extends React.Component {
    constructor(props) {
        super(props)
        this.state = { input: '', clicked: false }
    }

    handleInputChange = (text) => {
		if (this.state.input === '') {
			this.setState({ clicked: false })
		}
		this.setState({ input: text })
        this.props.inputValue(text)
	}

	handleClick(state) {
		this.handleInputChange(state)
		this.setState({clicked: true})
	}
	
	renderStateSuggestion() {
		if (this.props.label != "State" || this.state.input === '' || this.state.clicked) {
			return (<div></div>)
		}
		const matchedStates = listStates.filter(item => item.startsWith(this.state.input.toLocaleUpperCase()))
		return matchedStates.map((state) => (
			<h5 key={state}
				onClick={() => this.handleClick(state)}>
					{state}
			</h5>
		))
	}

    render() {

        return (
            <div>
                <MuiThemeProvider theme={theme}>
                  <TextField 
						label={this.props.label}
						value={this.state.input}
						onChange={(event) => this.handleInputChange(event.target.value)}
						// autoFocus={true}
						placeholder= {`Name of ${this.props.label}`}
						InputLabelProps = {{ style: {color: 'white'}}}
						inputProps={{ style: {color: 'white'}}}
						InputProps={{
							color: 'white'
						}}
                  />
				  {/* <div style={suggestionContainer}>
				  	{this.renderStateSuggestion()}
				  </div> */}
                </MuiThemeProvider>
            </div>
        )
    }
}
const suggestionContainer = {
	background: 'green',
	position: 'absolute',
	width: 50, 
	textAlign: 'center',
}
export default InputField