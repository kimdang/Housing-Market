import React from 'react'
// import ReactDOM from 'react-dom'
import {CitySelector, Analysis, Title} from './section'

// import store
import { createStore, applyMiddleware } from 'redux'
import rootReducer from '../reducers'
import { Provider } from 'react-redux'

// need redux thunk for async call
import thunk from 'redux-thunk'

const store = createStore(rootReducer,applyMiddleware(thunk))

class Homepage extends React.Component {
    render() {
        return (
            <Provider store={store}>
                <div style={homePageContainer}>
                    <div>
                        <Title />
                    </div>
                    <div style={bodyContainer} >
                        <div style={CitySelectorSection} >
                            <CitySelector />
                        </div>
                        <div style={AnalysisSection} >
                            <Analysis />
                        </div>
                    </div>
                </div>
            </Provider>
        )
    }
}

const homePageContainer = {
    height: '100%',
    width: '100%'
}

const bodyContainer = {
    backgroundColor: '#f8f8f8',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'flex-start',
    height: '100%',
    paddingLeft: 20
}

const CitySelectorSection = {
    width: '15%',
}

const AnalysisSection = {
    width: '80%'
}

export default Homepage