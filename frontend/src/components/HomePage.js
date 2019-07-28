import React from 'react'
import { CitySelector, Analysis, Title } from './section'
import MediaQuery from 'react-responsive'
import { breakpoints, global } from '../components/common'

// import store
import { createStore, applyMiddleware } from 'redux'
import rootReducer from '../reducers'
import { Provider } from 'react-redux'

// need redux thunk for async call
import thunk from 'redux-thunk'

const store = createStore(rootReducer, applyMiddleware(thunk))

class Homepage extends React.Component {
  render() {

    return (
      <Provider store={store}>
          <MediaQuery maxDeviceWidth={breakpoints.phone}>
            <div style={mobile.homePageContainer}>
              <h1>
                Mobile view is comming...
              </h1>
              <h1>
                Pls view this app using at least 13 inch screen
              </h1>
              {/* <div style={laptop.titleSection}>
                <Title />
              </div>
              <div style={mobile.CitySelectorContainer} >
                <div style={mobile.CitySelectorSection}>
                  <CitySelector />
                </div>
              </div> */}
              {/* <div style={mobile.bodyContainer} >
                <div style={mobile.CitySelectorSection} >
                  <CitySelector />
                </div>
                <div style={mobile.AnalysisSection} >
                  <Analysis />
                </div>
              </div> */}
            </div>
          </MediaQuery>
          <MediaQuery minDeviceWidth={breakpoints.phone + 1} >
            <div style={laptop.homePageContainer}>
              <div style={laptop.CitySelectorContainer} >
                  <div style={laptop.titleSection}>
                    <Title />
                  </div>
                  <CitySelector />
              </div>
              <div style={laptop.bodyContainer} >

                <div style={laptop.AnalysisSection} >
                  <Analysis />
                </div>
              </div>
            </div>
          </MediaQuery>
      </Provider>
    )
  }
}



const mobile = {
  homePageContainer: {
    minHeight: '100vh',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
  },
  CitySelectorContainer: {
    width: '100%',
    height: 300 ,
    backgroundColor: '#323544',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center'
  },
  bodyContainer : {
    backgroundColor: '#f8f8f8',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    height: '100%',
    padding: 10
  },
  CitySelectorSection: {
    width: '100%',
  },
  AnalysisSection: {
    width: '100%'
  }
}


const laptop = {
  homePageContainer: {
    minHeight: '100%',
    width: '100%',
    maxWidth: 1400,
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'flex-start',
  },
  CitySelectorContainer: {
    width: '20%',
    maxWidth: 200,
    // backgroundColor: '#323544',
    display: 'flex',
    justifyContent: 'center',
    flexDirection: 'column',
  },
  bodyContainer : {
    minWidth: '80%',
    maxWidth: 1200,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    height: '100%',
  },
  titleSection: {
    backgroundColor: '#ea5a5a',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-around',
    boxShadow: 'rgb(158, 158, 158) 0px 8px 6px -6px',
    marginBottom: 30,
    borderRadius: 2,
  },
  AnalysisSection: {
    backgroundColor: '#f6f6f6',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center'
  }
}


export default Homepage