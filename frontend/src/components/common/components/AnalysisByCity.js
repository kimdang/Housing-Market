import React from 'react'
import { Figure } from '../index'
const AnalysisByCity = ({ city }) => {
    const cityName = `${city.city}, ${city.state} `
    return (
        <div>
            <h3 style={cityNameStyle} > {cityName} </h3>
            <Figure city={city} />
        </div>
    )
}

const cityNameStyle = {
    textAlign: 'center'
}
export default AnalysisByCity