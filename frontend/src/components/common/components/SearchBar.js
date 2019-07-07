import React from 'react'
import InputBase from '@material-ui/core/InputBase';
import SearchIcon from '@material-ui/icons/Search';

const SearchBar = ({ handleInput }) => {
    return (
        <div style={ searchBarContainer } >
            <div>
                <SearchIcon />
            </div>
            <div>
                <InputBase 
                    placeholder="Search...."
                    type="search"
                    onChange={(event) => handleInput(event.target.value)}
                />
            </div>
        </div>
    )
}

const searchBarContainer = {
    display: 'flex',
    justifyContent: 'row',
    width: '100%'
}


export default SearchBar