import React from 'react'
import { global } from '../index'

const AnalysisHeader = ({ }) => {
    return (
        <div>
            <div style={{ ...section1, height: global.maxHeightSubSection }} >
                <h3 style={textStyle}> Average House Value </h3>
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
