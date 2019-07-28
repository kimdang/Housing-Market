import React from 'react'
import { IconSect } from '../../subsection'
import { global } from '../../common'
const Title = () => {
    return (
        <div style={titleContainer} >
            <h1 style={header}> Housing Analysis </h1>
            <IconSect />
        </div>
    )
}

const titleContainer = {
    padding: 10,
    width: "100%",
    maxWidth: global.maxScreenWidth,
}

const header = {
    textAlign: 'center',
    marginTop: 30,
    color: 'white'
}

const githubContainer = {
    width: 30,
    height: 30,
}

export default Title