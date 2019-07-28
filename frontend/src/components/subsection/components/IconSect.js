import React from 'react'
import { githubIcon, global } from '../../common'
const IconSect = () => {
    return (
        <div style={iconContainer}>
            <div style={githubContainer}>
                <a href={global.ghProject} target="_blank" > 
                    <img src={githubIcon}/>
                </a>
            </div>
        </div>
    )
}

const iconContainer = {
    width: "100%",
    display: "flex",
    flexDirection: "row",
    justifyContent: "flex-end",
}

const githubContainer = {
    width: 30,
    height: 30,
}

export default IconSect