import React from 'react'
import { connect } from 'react-redux';

import { AnalysisByCity, AnalysisHeader, global } from '../../common'
import { FigureSect } from '../../subsection'
import _ from 'lodash'

const historical = "historical_data"
const forecast = "forecast"
const histogram = "histogram"
const heightFigureSection = global.laptop.heightFigSect
const histogramDetail = "The following plot illustrates the monthly percent change in home sale prices of city_name. The average monthly percent change is percent_average % with an error estimate of +/- standard_deviation %."
const forecastedDetail = "The home sale price is forecasted to be $ 5_year_price thousands in 2024 and $ 10_year_price thousands in 2029."

class Analysis extends React.Component {
    constructor(props) {
        super(props)
        this.state = { city1: {}, city2: {} }        
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.analysis.city1.location_id != this.state.city1.location_id) {
            this.setState({
                city1: nextProps.analysis.city1
            })
        }
        if (nextProps.analysis.city2.location_id != this.state.city2.location_id) {
            this.setState({
                city2: nextProps.analysis.city2
            })
        }
    }

    getHistogramDetail(city) {
        if (! _.isEmpty(city)) {
            let detail_data = histogramDetail.replace('percent_average', city.percent_average)
            detail_data = detail_data.replace('standard_deviation', city.standard_deviation)
            detail_data = detail_data.replace('city_name', this.getCityName(city))
            return detail_data
        }
        return null
    }

    getForecastedDetail(city) {
        if (! _.isEmpty(city)) {
            let detail_data = forecastedDetail.replace('5_year_price', city['5_year_price'])
            detail_data = detail_data.replace('10_year_price', city['10_year_price'])
            return detail_data
        }
        return null
    }

    getCityName(city) {
        if (! _.isEmpty(city)) {
            let cityName= `${city.city}, ${city.state}`
            return cityName
        }
        return null
    }

    renderAnalysis() {
        let histogamDetail_1 = this.getHistogramDetail(this.state.city1)
        let histogamDetail_2 = this.getHistogramDetail(this.state.city2)
        let forecastDetail_1 = this.getForecastedDetail(this.state.city1)
        let forecastDetail_2 = this.getForecastedDetail(this.state.city2)

        if (! _.isEmpty(this.state.city1)) {
            return (
                <div>
                    <div style={figureContainer}>
                        <FigureSect 
                            id = {1}
                            header= "Home Sale Price is the median sale price for various housing types. These values have been seasonally adjusted by Zillow."
                            src1 = {this.state.city1[historical]}
                            src2 = {this.state.city2[historical]}
                            city1 = {this.getCityName(this.state.city1)}
                            city2 = {this.getCityName(this.state.city2)}
                        />
                    </div>
                    <div style={figureContainer}>
                        <FigureSect 
                            id = {2}
                            header = "Histogram"
                            detail1 = {histogamDetail_1}
                            detail2 = {histogamDetail_2}
                            src1 = {this.state.city1[histogram]}
                            src2 = {this.state.city2[histogram]}

                        />
                    </div>
                    <div style={figureContainer}>
                        <FigureSect 
                            id = {3}
                            header = "Forecasted Value"
                            src1 = {this.state.city1[forecast]}
                            src2 = {this.state.city2[forecast]}
                            detail1 = {forecastDetail_1}
                            detail2 = {forecastDetail_2}
                        />
                    </div>
                </div>
            )
        }
        return (
            <div></div>
        )
    }
    render() {
        return (
            <div>
                <div style={analysisContainer}>
                    <div style={introContainer}>
                        <h3>
                        The following analysis was derived from Zillow Economic Data. These datasets can be downloaded via https://www.zillow.com/research/data/. The purpose of this project is to help individuals make an informed decision on where to invest in the US housing market. The main focus of this analysis is analyzing each city individually and compare them side-by-side. The real estate prediction portion was done using Prophet. 
                        </h3>
                    </div>
                    {this.renderAnalysis()}
                </div>
            </div>
        )
    }
}

const analysisContainer = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'start',
    minHeight: '100vh',
    width: '100%',
}

const introContainer = {
    boxShadow: 'rgb(158, 158, 158) 0px 8px 6px -6px',
    padding: global.padding,
    background: 'white'
}

const figureContainer = {
    width: '100%',
    height: heightFigureSection,
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