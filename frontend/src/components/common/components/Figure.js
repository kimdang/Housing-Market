import React from 'react'
import CardMedia from '@material-ui/core/CardMedia';

const Figure = ({ city }) => {
    return (
        <CardMedia
            component="img"
            src={city.figure}
        />
    )
}
export default Figure