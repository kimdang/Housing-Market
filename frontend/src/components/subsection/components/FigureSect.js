import React from 'react'
import { Figure, AnalysisHeader, breakpoints, global } from '../../common'
import { FormHelperText } from '@material-ui/core';
import MediaQuery from 'react-responsive'

const heightFigureSection = global.laptop.heightFigSect


const FigureSect = ({ id, city1 = null, city2 = null, header=null, src1, src2=null, detail1=null, detail2=null }) => {
    return (
        <div>
            {/* <MediaQuery maxDeviceWidth={breakpoints.phone}>
                <div style={analysisContainer}>
                    <div style={mobile.headerContainer}>
                        {/* <AnalysisHeader header = {header} /> */}
                    {/* </div>   */}
                    {/* <div style={mobile.figureContainer}> */}
                        {/* <Figure city = {city1} />   */}
                    {/* </div>   */}
                    {/* <div style={mobile.figureContainer}> */}
                        {/* <Figure city = {city2} />   */}
                    {/* </div>   */}
                {/* </div> */}
            {/* </MediaQuery> */}
            <MediaQuery minDeviceWidth={breakpoints.phone}>
                <div style={{...laptop.figureContainer}}>
                    <div style={laptop.figure}>
                        <h3>{city1}</h3>
                        <Figure src = {src1} />  
                        <h4 style={{fontWeight: 600}}>{detail1}</h4>
                    </div>  
                    <div style={laptop.headerContainer}>
                        <div style={laptop.header}>
                            <AnalysisHeader header = {header} />
                        </div>
                    </div>
                    <div style={laptop.figure}>
                        <h3>{city2}</h3>
                        <Figure src = {src2} />  
                        <h4 style={{fontWeight: 600}}>{detail2}</h4>
                    </div>  
                </div>
            </MediaQuery>

        </div>
    )
}
const singpleCity = {
    figureContainer: {
        width: "100%",
        display: "flex",
        justifyContent: "column"
    },
    F_header: {
        width: "100%"
    },
    F_figure: {
        width: "100%"
    }
}
const analysisContainer = {
    width: "100%",
    height: "100%"
}
const mobile = {
    headerContainer: {
        width: '100%',
        height: 100
    },
    figureContainer: {
        marginTop: 10,
        width: '100%',
        height: 300
    }
}
const laptop = {
    headerContainer: {
        width: '15%',
        height: heightFigureSection,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-around'
    },
    header: {
        width: "100%",
    },
    figureContainer: {
        display:'flex',
        flexDirection: 'row',
        justifyContent: 'space-around'
    },
    figure: {
        marginTop: 10,
        width: '42.5%',
        height: heightFigureSection,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
    }
}

export default FigureSect