import {combineReducers} from 'redux';
import figures from './components/figures'

const rootReducer = combineReducers({
    analysis: figures
})

export default rootReducer