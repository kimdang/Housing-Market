import React from 'react'
import { global } from '../index'

const AnalysisHeader = ({ header }) => {
    return (
        <div>
            <div style={{ ...section1, height: global.maxHeightSubSection }} >
                <h3 style={textStyle}> {header} </h3>
            </div>
        </div>
    )
}

const section1 = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center'
}

const textStyle = {
    textAlign: 'center'
}

export default AnalysisHeader
