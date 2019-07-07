import React from 'react'
import _ from 'lodash'
import { connect } from 'react-redux';

// import ReactDOM from 'react-dom'
import Button from '@material-ui/core/Button';

import { InputField, SelectedCityCard } from '../../common'

import { fetchFigure } from '../../../actions'

class CitySelector extends React.Component {
    constructor(props) {
        super(props)
        this.state = { city: '', state: '', analysis: {} }        
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.analysis !== this.state.analysis) {
            this.setState({
                analysis: nextProps.analysis
            })
        }
    }

    handleCityInput = (input) => {
        this.setState({ city: input })
    }
    
    handleStateInput = (input) => {
        this.setState({ state: input })
    }

    capitalizeFirstLetter = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1)
    }

    handleSubmit = () => {
        const city = this.capitalizeFirstLetter(this.state.city)
        const state = this.state.state.toUpperCase()
        this.props.getFigure(state,city)
    }

    renderCityCard1() {
        if ( ! _.isEmpty(this.state.analysis.city1) ) {
            return (
                <SelectedCityCard 
                    city= {this.state.analysis.city1.city}
                    state= {this.state.analysis.city1.state}
                />
            )
        }
    }
    renderCityCard2() {
        if ( ! _.isEmpty(this.props.analysis.city2) ) {
            return (
                <SelectedCityCard 
                    city= {this.props.analysis.city2.city}
                    state= {this.props.analysis.city2.state}
                />
            )
        }
    }

    render() {
        return (
            <div style={CitySelectorContainer} >
                <div style={inputContainer} >
                    <InputField label='City' inputValue={this.handleCityInput} />
                    <InputField label='State' inputValue={this.handleStateInput} />
                </div>
                <div style= {buttonContainer} >
                    <Button
                        variant="contained" 
                        color="primary" 
                        onClick={this.handleSubmit}>
                        Analyze
                    </Button>
                </div>
                <div style={cityCardContainer}>
                    {this.renderCityCard1()}
                    {this.renderCityCard2()}
                </div>
            </div>
        )
    }
}

const CitySelectorContainer = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    margin: 20,
    paddingLeft: 10,
    backgroundColor: 'white',
    boxShadow: '0 8px 6px -6px #9E9E9E',
    borderRadius: 5
}

const inputContainer = {
    height: 120,
    width: '100%',
}

const buttonContainer = {
    display: 'flex',
}

const cityCardContainer = {
    margin: 10
}

/** connect map state in store to props in component */
const mapStateToProps = (state) => {
    return{
      analysis:state.analysis
    }
  }

const mapDispatchToProps = dispatch => {
    return {
        getFigure: (city,state) => {
            dispatch(fetchFigure(city,state))
        },
    }
};
  
export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(CitySelector);