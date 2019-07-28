import React from 'react'
import CardMedia from '@material-ui/core/CardMedia';
import { global } from '../index'

const Figure = ({ src }) => {
    const style = {
        width: '100%',
        maxWidth: global.laptop.maxSizeFigure,
        maxHeight: global.laptop.maxSizeFigure,
    }
    if (! src) {
        return (
            <div></div>
        )
    } 
    return (
        <div style= {style} >
            <CardMedia
                component = "img"
                src = {src}
                style = {{ boxShadow: '0 8px 6px -6px #9E9E9E' }}
            />
        </div>
    )
    
}





export default Figure