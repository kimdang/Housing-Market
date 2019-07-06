import _ from 'lodash'

const FETCH_FIGURE = 'FETCH_FIGURE'

const ANALYSIS = {
    'city1': {},
    'city2': {}
}

export default function (state= ANALYSIS, action) {
    switch (action.type) {
        case 'FETCH_FIGURE':
            if (_.isEmpty(state.city1)) {
                return {...ANALYSIS, 'city1': action.payload}
            }
            return {...state,'city2': action.payload}
        
        default: 
            return state
    }
}