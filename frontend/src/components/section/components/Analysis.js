import React from 'react'
import { connect } from 'react-redux';

import { AnalysisByCity, AnalysisHeader } from '../../common'
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
            return <AnalysisByCity city={this.state.city1} />
        }
    }

    renderFigure2() {
        if ( ! _.isEmpty(this.state.city2) ) {
            return <AnalysisByCity city={this.state.city2} />
        }
    }

    renderHeader() {
        if ( !_.isEmpty(this.state.city1) || ! _.isEmpty(this.state.city2) ) {
            return <AnalysisHeader />
        }
    }

    render() {
        return (
            <div style={analysisContainer}>
                <div style={cityContainer}>
                    {this.renderFigure1()}
                </div>
                <div style={descriptionContainer}>
                    {this.renderHeader()}
                </div>
                <div style={cityContainer}>
                    {this.renderFigure2()}
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

const descriptionContainer = {
    width: '20%',
    height: '100%',
    boxShadow: '0 8px 6px -6px #9E9E9E'
}

const cityContainer = {
    width: '40%',
    padding: '5px',
    flexDirection: 'column',
    display: 'flex',
    justifyContent: 'start'
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