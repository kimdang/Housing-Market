import React from 'react'
import Chip from '@material-ui/core/Chip';
import { makeStyles } from '@material-ui/core/styles';


const SelectedCityCard = ({ city, state }) => {
    const selectedCity = `${city}, ${state}`

    function handleDelete() {
        alert ("you clicked delete")
    }

    return (
        <div style={ selectedCityContainer } >
            <div>
                <Chip
                    label={selectedCity}
                    onDelete={handleDelete}
                    color= "primary"
                />
            </div>
        </div>
    )
}

const selectedCityContainer = {
    display: 'flex',
    justifyContent: 'column',
    width: '100%'
}
  
  

export default SelectedCityCard