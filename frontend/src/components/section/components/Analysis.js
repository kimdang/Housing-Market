import React from 'react'
import { connect } from 'react-redux';

import { Figure } from '../../common'
import _ from 'lodash'

class Analysis extends React.Component {
    constructor(props) {
        super(props)
        this.state = { city1: {}, city2: {} }        
    }
    componentWillReceiveProps(nextProps) {
        if (nextProps.analysis.city1.id != this.state.city1.id) {
            this.setState({
                city1: nextProps.analysis.city1
            })
        }
        if (nextProps.analysis.city2.id != this.state.city2.id) {
            this.setState({
                city2: nextProps.analysis.city2
            })
        }
    }

    renderFigure1() {
        if ( ! _.isEmpty(this.state.city1) ) {
            return <Figure  city={this.state.city1} />
        }
    }

    renderFigure2() {
        if ( ! _.isEmpty(this.state.city2) ) {
            return <Figure  city={this.state.city2} />
        }
    }

    render() {
        return (
            <div>
                <div style={analysisContainer}>
                    <div style={city1Container}>
                        {this.renderFigure1()}
                    </div>
                    <div style={city2Container}>
                        {this.renderFigure2()}
                    </div>
                </div>
            </div>
        )
    }
}

const analysisContainer = {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    height: '100%',
    width: '100%'
    // margin: 20,
    // paddingLeft: 10,
    // backgroundColor: 'white'
}

const city1Container = {
    width: '50%',
    padding: '5px'
}

const city2Container = {
    width: '50%',
    padding: '5px'
}

/** connect map state in store to props in component */
const mapStateToProps = (state) => {
    return{
        analysis:state.analysis
    }
}
  
export default connect(
    mapStateToProps,
)(Analysis);