import React from 'react'
import CardMedia from '@material-ui/core/CardMedia';
import { global } from '../index'

const Figure = ({ city }) => {
    return (
        <div style= {{...cardContainer, maxHeight: global.maxHeightSubSection}} >
            <CardMedia
                component = "img"
                src = {city.figure}
                style = {{ boxShadow: '0 8px 6px -6px #9E9E9E' }}
            />
        </div>
    )
}



const cardContainer = {
    // maxHeight: 430
}


export default Figure