import React from 'react'
import Chip from '@material-ui/core/Chip';
import { makeStyles } from '@material-ui/core/styles';


const SelectedCityCard = ({ id, city, state }) => {
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
    flexDirection: 'column',
    justifyContent: 'space-around',
    marginTop: 20,
    marginLeft: 20,
}
  
  

export default SelectedCityCard